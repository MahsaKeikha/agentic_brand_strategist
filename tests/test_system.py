from orchestration.orchestrator import run
from safety.policy import PROTECTED_ACTIONS, REQUIRED_REVIEWS, authorize


def approved_context():
    return {key: True for key in REQUIRED_REVIEWS}


def test_orchestrator_runs_five_agents_and_fails_closed():
    result = run({"objective": "brand strategy"})
    for key in ("research", "audience", "positioning", "messaging", "review"):
        assert key in result
    assert result["released"] is False


def test_missing_reviews_fail_closed():
    result = authorize("release_support_package", {})
    assert result["allowed"] is False
    assert len(result["missing"]) == 8


def test_reviewed_package_can_release():
    assert authorize("release_support_package", approved_context())["allowed"] is True


def test_unverified_audience_assumption_blocks():
    context = approved_context() | {"audience_assumption_unverified": True}
    assert authorize("release_support_package", context)["allowed"] is False


def test_unsupported_claim_blocks():
    context = approved_context() | {"message_claim_unsupported": True}
    assert authorize("release_support_package", context)["allowed"] is False


def test_legal_reputational_risk_blocks():
    context = approved_context() | {"legal_reputational_risk": True}
    assert authorize("release_support_package", context)["allowed"] is False


def test_provenance_gap_blocks():
    context = approved_context() | {"evidence_provenance_gap": True}
    assert authorize("release_support_package", context)["allowed"] is False


def test_protected_actions_never_autonomously_release():
    context = approved_context()
    for action in PROTECTED_ACTIONS:
        assert authorize(action, context)["allowed"] is False
