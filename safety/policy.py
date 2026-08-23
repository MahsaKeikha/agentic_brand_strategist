"""Fail-closed brand-strategy governance for F121."""

PROTECTED_ACTIONS = {
    "publish_brand_claim",
    "approve_positioning",
    "approve_public_message",
    "launch_campaign",
    "approve_comparative_claim",
    "external_publication",
}

REQUIRED_REVIEWS = (
    "research_evidence_reviewed",
    "audience_evidence_reviewed",
    "positioning_reviewed",
    "messaging_reviewed",
    "claims_substantiation_reviewed",
    "legal_reputational_risk_reviewed",
    "evidence_provenance_reviewed",
    "qualified_brand_approval",
)


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in PROTECTED_ACTIONS:
        return {"allowed": False, "reason": "binding brand publication authority is outside reference-system scope"}

    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required brand review", "missing": missing}

    blockers = []
    if context.get("research_evidence_gap"):
        blockers.append("brand research evidence is incomplete")
    if context.get("audience_assumption_unverified"):
        blockers.append("material audience assumption remains unverified")
    if context.get("positioning_conflict"):
        blockers.append("positioning conflicts with reviewed evidence or brand constraints")
    if context.get("message_claim_unsupported"):
        blockers.append("message or brand claim exceeds reviewed evidence")
    if context.get("comparative_claim_risk"):
        blockers.append("comparative claim requires qualified substantiation review")
    if context.get("legal_reputational_risk"):
        blockers.append("material legal or reputational risk remains unresolved")
    if context.get("evidence_provenance_gap"):
        blockers.append("brand evidence provenance is incomplete")
    if context.get("identity_or_deception_risk"):
        blockers.append("identity, attribution, or deceptive-representation risk remains unresolved")

    if blockers:
        return {"allowed": False, "reason": "brand-strategy governance blocker", "blockers": blockers}

    return {"allowed": True, "reason": "brand-strategy support package approved after qualified human review"}


def review_required(action: str) -> bool:
    return action in PROTECTED_ACTIONS


def enforce(action: str, approved: bool) -> None:
    if review_required(action) and not approved:
        raise PermissionError("Qualified human approval is required for this action.")
