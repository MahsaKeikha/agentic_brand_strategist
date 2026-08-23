# F121 | Agentic Brand Strategist | L3 Gold Standard | v1.0

A governed five-agent reference architecture for brand strategy across research, audience understanding, positioning, messaging architecture, differentiation, claim substantiation, evidence provenance, reputational risk, and qualified human brand approval.

F121 is decision-support only. It can structure evidence, hypotheses, positioning options, message systems, tradeoffs, and review packages, but it cannot autonomously publish brand claims, approve positioning, authorize public messaging, launch campaigns, approve comparative claims, or make external publications.

## Brand strategy lifecycle

```text
Research Context
    -> Audience Evidence
    -> Positioning Architecture
    -> Messaging Architecture
    -> Claims and Risk Review
    -> Evidence and Provenance Review
    -> Qualified Human Brand Approval
```

The workflow is fail closed. Missing research evidence, unverified audience assumptions, unsupported positioning or claims, unresolved legal or reputational risks, missing provenance, deceptive identity risk, or missing qualified approval prevent release.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Research Agent | Collects and structures market, company, product, category, customer, and competitor evidence | What evidence actually supports the brand strategy? |
| Audience Agent | Develops audience segments, needs, tensions, behaviors, contexts, and evidence-backed insights | Who is the brand trying to serve, and what is known versus assumed? |
| Positioning Agent | Develops category frame, value proposition, differentiation, reasons to believe, and strategic alternatives | Why should the intended audience choose or remember this brand? |
| Messaging Agent | Builds message hierarchy, proof points, tone, narrative, objection handling, and channel adaptations | How should the positioning be expressed consistently without overstating evidence? |
| Review Agent | Performs independent evidence, claim, legal, reputational, and governance review | Is the strategy package sufficiently reviewed for qualified human approval? |

Agents support strategic analysis. They do not replace brand leadership, product leadership, marketing leadership, legal counsel, communications teams, research professionals, or authorized organizational decision makers.

## Repository structure

```text
AGENTS/
├── research_agent.py
├── audience_agent.py
├── positioning_agent.py
├── messaging_agent.py
└── review_agent.py

SKILLS/
├── evidence_discipline.py
├── audience_reasoning.py
├── positioning_reasoning.py
├── messaging_reasoning.py
└── review_reasoning.py

TOOLS/
├── evidence_register.py
├── audience_map.py
├── positioning_map.py
├── message_matrix.py
└── review_gate.py

orchestration/
memory/
observability/
evals/
benchmarks/
examples/
docs/
prompts/
config/
safety/
tests/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

The architecture separates brand reasoning from deterministic evidence, audience, positioning, and message structures plus governance, evaluation, memory, and observability.

## Research evidence

Brand strategy should begin with evidence rather than slogans.

Relevant evidence can include:

- customer research
- interviews
- surveys
- usage data
- product evidence
- category research
- competitor materials
- sales feedback
- support data
- pricing evidence
- market trends
- brand tracking
- search behavior
- channel performance

The policy requires `research_evidence_reviewed`.

`research_evidence_gap` blocks release when material research support is incomplete.

## Evidence hierarchy

Not all evidence has equal strength.

F121 should distinguish among:

```text
verified customer evidence
observed behavioral evidence
product or company fact
third-party market evidence
competitor public claim
internal stakeholder assertion
strategic hypothesis
system inference
```

A strategic hypothesis should never be presented as established audience truth merely because it sounds plausible.

## Evidence provenance

`SKILLS/evidence_discipline.py` and `TOOLS/evidence_register.py` support traceability.

The policy requires `evidence_provenance_reviewed`.

Evidence metadata can include:

```text
evidence_id
source
date
market
segment
method
sample
owner
version
limitations
review_state
```

`evidence_provenance_gap` blocks release.

F121 must never fabricate research, testimonials, competitor data, market share, customer quotes, product capabilities, legal clearance, or executive approval.

## Audience architecture

`SKILLS/audience_reasoning.py` and `TOOLS/audience_map.py` support structured audience analysis.

An audience map can include:

```text
segment
role
context
job_to_be_done
need
pain_point
desired_outcome
barrier
belief
trigger
channel
proof_needed
source_evidence
confidence
```

The policy requires `audience_evidence_reviewed`.

`audience_assumption_unverified` blocks release when a material audience belief or need remains unsupported.

## Segmentation

Segmentation can use factors such as:

- behavior
- need state
- job to be done
- use case
- maturity
- industry
- company size
- role
- geography
- lifecycle stage
- value sensitivity

F121 should avoid stereotypes or unsupported demographic assumptions.

## Personas

Personas are synthesis tools, not real people.

A governed persona should distinguish evidence-backed attributes from illustrative details. The system should not fabricate quotes, histories, personal identities, or motivations and then present them as real customer research.

## Jobs to be done

Jobs-to-be-done reasoning can help identify what progress an audience seeks in a particular context.

F121 should preserve the difference between an observed job, an inferred job, and a speculative strategic hypothesis.

## Customer tensions

Strong positioning often reflects a meaningful tension between current-state frustration and desired progress.

The system can map tensions, barriers, anxieties, habits, and tradeoffs while preserving the evidence that supports each one.

## Positioning architecture

`SKILLS/positioning_reasoning.py` and `TOOLS/positioning_map.py` support structured positioning.

A positioning package can include:

```text
target_audience
category_or_frame
problem_or_tension
value_proposition
primary_benefit
differentiator
reason_to_believe
proof
competitive_alternative
tradeoffs
limitations
```

The policy requires `positioning_reviewed`.

`positioning_conflict` blocks release when proposed positioning conflicts with product reality, evidence, legal constraints, or other reviewed brand requirements.

## Category framing

Category framing affects what audience expectations and competitors become salient.

F121 can compare category options, but it should not claim category leadership, category creation, or market dominance without evidence.

## Value proposition

A value proposition should explain a relevant benefit supported by credible proof.

The system should distinguish among:

- feature
- functional benefit
- emotional benefit
- social benefit
- economic value
- strategic value

Benefit claims should remain proportionate to evidence.

## Differentiation

Differentiation can derive from product, process, experience, service, business model, access, expertise, brand meaning, community, ecosystem, or another defensible advantage.

F121 should not manufacture differentiation by mischaracterizing competitors or exaggerating small feature differences.

## Reasons to believe

Reasons to believe can include:

- product capability
- design evidence
- expertise
- data
- customer outcomes
- operational proof
- certifications
- partnerships
- research
- proprietary assets

Every material proof point should have provenance.

## Competitive intelligence boundaries

F121 can analyze public competitor positioning and evidence.

It should not invent competitor weaknesses, use confidential competitor information without authorization, impersonate competitors, or present rumor as fact.

## Comparative claims

`approve_comparative_claim` is protected.

Comparative claims can create legal and reputational risk. They should preserve comparison basis, evidence date, scope, methodology, relevant competitors, and material qualifications.

`comparative_claim_risk` blocks release when substantiation requires qualified review.

## Messaging architecture

`SKILLS/messaging_reasoning.py` and `TOOLS/message_matrix.py` support message design.

A message hierarchy can include:

```text
core_positioning
brand_promise
primary_message
supporting_messages
proof_points
objection_responses
call_to_action
tone
channel_adaptations
```

The policy requires `messaging_reviewed`.

## Message consistency

Messaging can vary by audience and channel while preserving the same strategic core.

F121 should identify contradictions across homepage, sales, product, investor, recruitment, customer-support, and partner communications when they create material brand confusion.

## Tone and voice

Tone and voice can be modeled across dimensions such as:

- formal versus conversational
- technical versus accessible
- bold versus restrained
- warm versus neutral
- visionary versus practical

Tone should support the brand strategy without becoming a substitute for evidence.

## Brand narrative

A brand narrative can structure:

- context
- tension
- change
- point of view
- role of the brand
- proof
- invitation

F121 should avoid fictionalizing company history, customer outcomes, founder stories, or social impact as factual narrative.

## Claims substantiation

The policy requires `claims_substantiation_reviewed`.

A claim record can include:

```text
claim
claim_type
intended_audience
channel
evidence
source
scope
qualification
risk
reviewer
status
```

`message_claim_unsupported` blocks release when a claim exceeds reviewed evidence.

## Claim types

Potential claim categories include:

- factual product claims
- performance claims
- comparative claims
- customer outcome claims
- market leadership claims
- sustainability claims
- health-related claims
- financial claims
- social impact claims
- testimonial claims

Different categories can require different evidence and specialist review.

## Puffery versus factual claims

Brand language can include subjective expressions, but factual or measurable representations require substantiation.

F121 should flag statements that sound aspirational but are likely to be interpreted as objective fact.

## Testimonials and endorsements

Testimonials should be real, attributable where required, appropriately permissioned, and representative within applicable policy and law.

The system should not fabricate customer quotes, influencer endorsements, expert endorsements, ratings, or user experiences.

## Legal and reputational risk

The policy requires `legal_reputational_risk_reviewed`.

Potential risk areas include:

- false or misleading advertising
- comparative claims
- trademark risk
- copyright risk
- privacy
- endorsements
- regulated product claims
- discriminatory messaging
- defamatory statements
- unsupported market claims
- reputational inconsistency

`legal_reputational_risk` blocks release when material risk remains unresolved.

## Trademark and naming boundaries

Brand naming can implicate trademark availability, domain availability, linguistic meaning, cultural context, and category confusion.

F121 can organize naming options and screening questions, but it cannot provide binding trademark clearance.

## Identity and attribution

`identity_or_deception_risk` blocks release.

The system should not support brand communications that impersonate individuals, fabricate executives, conceal material sponsorship where disclosure is required, or falsely attribute endorsements.

## Brand authenticity

Brand authenticity should be grounded in actual company behavior, product reality, values, and customer experience.

F121 should surface gaps between stated values and available evidence rather than polishing them into unsupported brand promises.

## Brand purpose

Purpose statements can guide brand strategy when tied to real organizational commitments.

The system should distinguish a desired purpose narrative from evidence of actual organizational behavior and impact.

## Brand values

Values can be translated into observable behaviors, product choices, service principles, hiring practices, or operating standards.

A value should not be treated as credible solely because it appears in a brand document.

## Brand promise

A brand promise creates expectations. F121 should test whether the organization can consistently deliver it across product, service, operations, and customer experience.

## Brand architecture

F121 can support decisions among:

- branded house
- house of brands
- endorsed brands
- sub-brands
- product brands
- service brands

Brand architecture should reflect portfolio strategy, audience clarity, equity, operational complexity, and legal constraints.

## Naming systems

A naming system can define principles for products, tiers, features, programs, and services.

The system should preserve consistency, scalability, usability, accessibility, and legal-review needs.

## Visual identity boundary

F121 can define strategic inputs for visual identity, such as positioning, tone, audience, differentiation, and brand principles.

It does not independently approve logos, packaging, typography, imagery, or other visual assets unless those outputs pass the appropriate design and human-review process.

## Accessibility and inclusive communication

Brand messaging should avoid unnecessary exclusion and support accessible communication where relevant.

Review can consider:

- plain language
- readability
- inclusive terminology
- translation quality
- alt text
- accessibility of digital communications
- cultural interpretation

Accessibility should not be treated as a cosmetic afterthought.

## Cultural and linguistic review

Words, symbols, idioms, colors, humor, and narratives can vary across markets.

F121 should flag localization risk when a strategy created for one market is transferred to another without review.

## Localization versus translation

Translation preserves language. Localization adapts meaning, cultural relevance, examples, claims, tone, and sometimes positioning.

The system should not assume literal translation preserves strategic intent.

## International brand consistency

Global consistency should be balanced against local relevance and regulatory requirements.

F121 can identify what must remain invariant versus what can adapt locally.

## Channel strategy boundary

F121 can recommend how messaging should adapt across channels, but it does not autonomously allocate media spend, launch campaigns, send communications, or publish content.

`launch_campaign` is protected.

## Public messaging boundary

`approve_public_message` is protected.

A message may be strategically sound and still require legal, product, executive, regulatory, or communications review before publication.

## Brand claim publication boundary

`publish_brand_claim` is protected.

F121 can prepare claims and evidence packages but cannot autonomously publish them to websites, ads, social media, packaging, investor materials, press releases, or sales collateral.

## Positioning approval boundary

`approve_positioning` is protected.

The system can compare positioning alternatives but cannot make a binding organization-wide positioning decision.

## External publication boundary

`external_publication` is protected.

F121 cannot autonomously publish or distribute brand materials to external audiences.

## Product truth

Brand strategy should remain aligned with product and operational reality.

The system should identify when marketing language promises capabilities, service levels, outcomes, access, or experiences that the organization cannot reliably deliver.

## Customer experience alignment

A strong brand is reinforced or weakened by actual customer experience.

F121 can map critical moments across acquisition, onboarding, usage, support, renewal, referral, and exit to test whether positioning and brand promise are operationally credible.

## Employee brand alignment

Internal teams often deliver the external promise.

Brand strategy can consider employee understanding, enablement, incentives, and service behavior without turning brand messaging into employment surveillance or hidden worker evaluation.

## Sales enablement

F121 can translate positioning into sales messages, objection handling, proof points, and competitive narratives while preserving substantiation and legal boundaries.

It should not fabricate case studies, pricing advantages, competitor defects, or customer commitments.

## Investor and corporate messaging

Investor and corporate communications can involve financial, legal, and securities considerations.

F121 should route material financial, forward-looking, governance, or regulated claims to qualified specialists rather than treating them as ordinary marketing copy.

## Regulated-domain claims

Healthcare, finance, insurance, education, legal, environmental, political, and other regulated domains can impose specific communication requirements.

The brand system should recognize when domain-specific review is required and should not infer legal permissibility from strategic fit.

## Brand differentiation testing

Positioning alternatives can be evaluated for:

- relevance
- distinctiveness
- credibility
- memorability
- defensibility
- strategic fit
- scalability
- customer comprehension

Scores are decision aids, not proof that the market will respond as predicted.

## Message testing

Message testing can use interviews, surveys, experiments, concept tests, usability tests, sales feedback, or campaign evidence.

F121 should preserve sample, method, audience, test context, and uncertainty.

## Brand tracking

Brand tracking can monitor awareness, consideration, preference, associations, trust, recall, and other measures over time.

Metric changes should be interpreted with methodology, sample, market context, and confidence in mind.

## Attribution limits

A change in brand metrics may reflect product launches, pricing, media, news, competition, seasonality, distribution, economic conditions, or measurement changes.

F121 should not automatically attribute every metric movement to a brand strategy intervention.

## Competitive differentiation over time

Competitors change. Positioning should be monitored for convergence, imitation, category shifts, and changes in customer expectations.

A positioning advantage should not be assumed permanent.

## Brand drift

Brand drift can occur when teams, channels, or markets gradually diverge from reviewed positioning and message architecture.

F121 can identify inconsistencies and route them for review rather than automatically rewriting public communications.

## Change control

Material changes in product, audience, market, pricing, strategy, regulation, competitors, or company capabilities should trigger brand impact review.

Prior approvals should not silently carry forward after major changes.

## Versioning

Brand records should preserve versions of:

- research
- audience maps
- positioning
- proof points
- claims
- message hierarchy
- tone guidance
- competitive evidence
- legal review
- approval state

Versioning enables traceability and prevents outdated claims from being reused accidentally.

## Memory and state

The `memory/` layer can preserve structured workflow context across agents.

State should distinguish source evidence, hypotheses, strategy options, selected recommendations, claims, risks, and human decisions.

Sensitive customer, employee, partner, or internal strategy data should be retained only according to legitimate organizational need.

## Observability

The `observability/` layer supports traceability across the workflow.

Useful telemetry includes:

- evidence completeness
- audience confidence
- positioning alternatives
- claim support
- message consistency
- comparative claim risk
- legal or reputational flags
- provenance gaps
- qualified approval state
- governance blockers
- protected-action attempts

Observability supports accountability but does not create publication authority.

## Required reviews

The implemented safety policy requires all eight conditions:

```text
research_evidence_reviewed
audience_evidence_reviewed
positioning_reviewed
messaging_reviewed
claims_substantiation_reviewed
legal_reputational_risk_reviewed
evidence_provenance_reviewed
qualified_brand_approval
```

Missing any required review fails closed.

## Fail-closed governance

The implemented policy blocks release when:

- brand research evidence is incomplete
- a material audience assumption remains unverified
- positioning conflicts with reviewed evidence or brand constraints
- a message or brand claim exceeds reviewed evidence
- a comparative claim requires unresolved substantiation review
- material legal or reputational risk remains unresolved
- evidence provenance is incomplete
- identity, attribution, or deceptive-representation risk remains unresolved
- any required review is missing
- qualified brand approval is missing

The system should expose the blocker rather than manufacture a polished but unsupported strategy.

## Protected actions

The safety policy permanently protects:

```text
publish_brand_claim
approve_positioning
approve_public_message
launch_campaign
approve_comparative_claim
external_publication
```

These actions remain outside autonomous authority even when every review condition is satisfied.

## Human authority boundaries

F121 must not autonomously:

- publish brand claims
- approve organization-wide positioning
- authorize public messaging
- launch campaigns
- approve comparative claims
- publish external materials
- fabricate customer evidence
- invent testimonials or endorsements
- misrepresent competitors
- provide binding legal clearance
- conceal material uncertainty or claim limitations

Final strategy, claims, publication, legal review, campaign launch, and external communication authority remains with qualified humans and authorized organizations.

## Qualified brand approval

The final review should involve personnel competent for the strategy and associated risk.

Depending on the case, this can include brand, marketing, product, research, sales, communications, legal, compliance, design, executive, or domain-specific specialists.

## Separation of strategy and publication

The architecture intentionally separates analytical strategy from external execution.

```text
evidence -> strategy -> message -> review -> authorized publication
```

A compelling message is not automatically a safe, substantiated, or approved public claim.

## Explicit failure states

Useful explicit states include:

```text
RESEARCH EVIDENCE GAP
AUDIENCE ASSUMPTION UNVERIFIED
POSITIONING CONFLICT
MESSAGE CLAIM UNSUPPORTED
COMPARATIVE CLAIM REVIEW REQUIRED
LEGAL OR REPUTATIONAL RISK
EVIDENCE PROVENANCE GAP
IDENTITY OR DECEPTION RISK
QUALIFIED BRAND APPROVAL REQUIRED
BRAND CLAIM PUBLICATION PROHIBITED
POSITIONING APPROVAL PROHIBITED
PUBLIC MESSAGE APPROVAL PROHIBITED
CAMPAIGN LAUNCH PROHIBITED
COMPARATIVE CLAIM APPROVAL PROHIBITED
EXTERNAL PUBLICATION PROHIBITED
```

F121 must never fabricate research, claims evidence, testimonials, endorsements, market facts, competitor facts, legal approval, or qualified-human decisions.

## End-to-end reference workflow

A typical F121 workflow follows this sequence:

1. Define the business, product, market, decision, and brand objective.
2. Collect and register source evidence.
3. Map audiences, needs, tensions, behaviors, and confidence levels.
4. Develop positioning alternatives and differentiation hypotheses.
5. Map reasons to believe and proof points.
6. Build message hierarchy and channel adaptations.
7. Review claims and comparative statements for substantiation.
8. Review legal, reputational, cultural, and identity risks.
9. Preserve evidence provenance, limitations, and versions.
10. Perform independent brand readiness review.
11. Apply fail-closed governance gates.
12. Require explicit qualified-human brand approval.
13. Keep positioning approval, public-message approval, campaign launch, comparative-claim approval, claim publication, and external publication outside autonomous authority.

## Evaluation and held-out governance suite

The repository contains evaluation logic under `evals/` and benchmark cases under `benchmarks/`.

Evaluation should test both strategic usefulness and governance behavior, including:

- evidence completeness
- audience-assumption discipline
- positioning consistency
- message substantiation
- comparative-claim escalation
- legal and reputational risk handling
- provenance enforcement
- deceptive-representation detection
- qualified-human approval enforcement
- protected-action enforcement

The behavioral verification layer includes eight direct governance tests and a 10-scenario held-out brand-governance suite.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

These gates verify syntax-critical linting, fail-closed governance, held-out brand scenarios, and execution of the governed reference workflow.

## Reproducibility

Install development dependencies as appropriate for the reference repository, then run:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

Reproducibility also depends on preserving evidence, audience maps, positioning versions, claims, message matrices, review states, and source provenance.

## Extension points

Organization-specific implementations can add governed integrations for:

- customer research repositories
- CRM systems
- market-research platforms
- analytics systems
- brand asset management
- content management systems
- competitive intelligence repositories
- product-information systems
- campaign planning tools
- legal-review workflows
- design systems

Integrations should preserve provenance, permissions, versioning, qualified review, and strict separation between recommendation and publication authority.

## Example applications

Potential governed uses include:

- brand positioning development
- audience segmentation
- message architecture
- value proposition development
- competitive differentiation analysis
- naming and portfolio strategy support
- brand refresh planning
- product launch messaging
- claims substantiation preparation
- brand governance training and simulation

F121 is not an autonomous brand authority, advertising approver, legal clearance system, campaign launcher, or external publishing system.

## Design principles

F121 follows these principles:

1. Evidence before positioning.
2. Separate observed audience insight from strategic hypothesis.
3. Keep differentiation grounded in product and market reality.
4. Require substantiation for factual and comparative claims.
5. Preserve evidence provenance and uncertainty.
6. Surface legal, cultural, reputational, and identity risks.
7. Separate strategy generation from public execution.
8. Fail closed when material evidence or review is incomplete.
9. Keep claims, positioning approval, campaign launch, and publication under qualified human authority.

## Scope statement

F121 demonstrates a governed multi-agent architecture for brand-strategy support. It combines specialized agents, deterministic audience, positioning, message, and evidence tools, structured claim review, observability, evaluation, and fail-closed governance while preserving strict human authority over brand decisions and external publication.

It is a reference implementation for governed brand strategy engineering, not a substitute for qualified strategic, research, legal, communications, or executive judgment.

Author: Mahsa Keikha
