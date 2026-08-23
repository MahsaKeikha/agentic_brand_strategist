from AGENTS import audience_agent, messaging_agent, positioning_agent, research_agent, review_agent
from safety.policy import authorize


def run(ctx: dict) -> dict:
    analyses = {
        "research": research_agent.run(ctx),
        "audience": audience_agent.run(ctx),
        "positioning": positioning_agent.run(ctx),
        "messaging": messaging_agent.run(ctx),
        "review": review_agent.run(ctx),
    }
    governance = authorize("release_support_package", ctx.get("governance", {}))
    return {**analyses, "governance": governance, "released": governance["allowed"]}
