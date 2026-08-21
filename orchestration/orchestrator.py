from AGENTS import research_agent,audience_agent,positioning_agent,messaging_agent,review_agent

def run(ctx):
 return {'research':research_agent.run(ctx),'audience':audience_agent.run(ctx),'positioning':positioning_agent.run(ctx),'messaging':messaging_agent.run(ctx),'review':review_agent.run(ctx)}
