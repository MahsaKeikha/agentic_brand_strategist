"""Held-out governance scenarios for F121."""
from safety.policy import REQUIRED_REVIEWS, authorize


def base():
    return {key: True for key in REQUIRED_REVIEWS}


SCENARIOS = [
    ({}, False),
    (base(), True),
    (base() | {"research_evidence_gap": True}, False),
    (base() | {"audience_assumption_unverified": True}, False),
    (base() | {"positioning_conflict": True}, False),
    (base() | {"message_claim_unsupported": True}, False),
    (base() | {"comparative_claim_risk": True}, False),
    (base() | {"legal_reputational_risk": True}, False),
    (base() | {"evidence_provenance_gap": True}, False),
    (base() | {"identity_or_deception_risk": True}, False),
]


def main():
    for index, (context, expected) in enumerate(SCENARIOS, 1):
        actual = authorize("release_support_package", context)["allowed"]
        assert actual is expected, f"scenario {index}: expected {expected}, got {actual}"
    print(f"F121 held-out governance: {len(SCENARIOS)}/{len(SCENARIOS)} passed")


if __name__ == "__main__":
    main()
