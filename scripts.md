# Beyond Loop Engineering — Script Structure

/title: Beyond Loop Engineering

- Introduce Li Yin: co-founder and CEO of SylphAI, creator of AdalFlow, and former AI researcher at Meta.
- SylphAI studies autonomy through agents and memory.
- This is an emerging field. The session is an invitation to examine the problem honestly and explore the future together.

/title: More Productive. More Drained.

- Coding agents have made developers more productive.
- But many developers feel increasingly drained.
- Opening question: If coding agents are already so capable, why are we still babysitting them 12 hours a day?
- The challenge is no longer whether agents can produce code. It is whether we can trust them to deliver the right outcome.

/title: Why Are We Still Babysitting?

- Delivering one PR requires understanding, planning, building, testing, reviewing, and iterating.
- Current agents can perform many of these steps, but humans still connect them.
- Humans carry context between agents, tabs, environments, and stages.
- Humans decide when to approve, correct, continue, escalate, or stop.

/title: The 100 Plausible Solutions Problem

- A feature may have 100 plausible implementations.
- Only a few truly fit the codebase, architecture, product constraints, and past decisions.
- Agents generate work faster, but developers still choose what is right and review what does not fit.
- Faster output can therefore create more decisions and more review—not reliable delegation.

/title: Model Capability Is Not Autonomy

- A model may be highly capable while the surrounding system still requires constant supervision.
- Model capability asks: can it reason and produce strong work?
- Autonomy asks: can the system carry responsibility from a goal to a verified outcome?
- Better intelligence alone does not automatically create higher autonomy.

/title: From Models to Agents

- Models provide reasoning and generation.
- ReAct introduced the basic agent loop: reason → act → observe → repeat.
- Modern agent harnesses connect models to tools, files, browsers, permissions, context, and working environments.
- Agents already have meaningful task-level autonomy and can complete substantial parts of a task.

/title: Humans Still Own the Workflow

- Today’s agents can execute steps; humans still own the full workflow.
- The developer remains the manual scheduler and integration layer.
- They coordinate planning, coding, browser testing, review, documentation, and delivery.
- The missing capability is not simply another tool. It is reliable ownership of the workflow.

/title: The Three Layers of Autonomy

- Model intelligence: can reason and generate.
- Agent + harness: can work inside an environment.
- Loop engineering: can carry an expert’s goal, context, quality bar, memory, and evaluation toward a verified outcome.
- Computing analogy: CPU → operating system → application.

/title: The Emerging Idea of Loop Engineering

- Developers are tired of manually gluing the workflow together.
- “Loop engineering” is an emerging term for making the workflow itself more autonomous.
- The definition is not settled; the industry is still experimenting.
- Addy Osmani names it briefly as the step after harnesses: systems that keep prompting, checking, remembering, and deciding what happens next.
- Our working definition: a system that coordinates work toward a goal, verifies progress, recovers from failure, and stops when the outcome is achieved.
- Reference: Addy Osmani, AI Engineer 2026 / Own the Outer Loop.

/title: What Is Starting to Emerge?

- Goal-driven: define success and stop conditions.
- Multi-agent: use specialized agents across a complex workflow.
- Evaluated: verify work independently instead of trusting self-reported success.
- Stateful: preserve progress, decisions, and context across iterations.
- Bounded: enforce permissions, budgets, safeguards, and escalation.
- The primitives exist; the challenge is assembling them into a reliable system.

/title: A Good Loop Starts With a Good Goal

- Loop engineering begins with an outcome clear enough to delegate.
- The goal must define a concrete outcome, verifiable success, scope, constraints, and stop conditions.
- Without a clear goal, the system cannot reliably know what to optimize or when to stop.
- Proposed new supporting slide.

/title: When Not to Use Loop Engineering

- Today’s agents remain extremely useful as collaborative tools.
- If the goal is unclear or still evolving, use the agent to brainstorm, explore alternatives, and clarify what you want.
- If the human wants to participate actively in a creative process—such as shaping a presentation, design, or new idea—keeping the human in the loop is valuable.
- Use loop engineering when the outcome is clear enough to delegate; use today’s agents when discovering the goal is part of the work.

/title: The System Is the Hard Part

- Which agents should participate?
- What context does each agent need, and when?
- How do agents communicate and hand work off?
- How is quality evaluated independently?
- How does the system recover, update documentation, and know when to stop?
- OpenAI’s Codex example shows that even with capable agents, a team still has to build and maintain this surrounding system.

/title: Our Thesis — Workflow Infrastructure for Autonomy

- The next-generation autonomous agent is not simply a better coding agent.
- It is infrastructure for operating existing capable agents inside a role-specific workflow.
- The workflow carries expert context, memory, safeguards, evaluation, and quality standards.
- Each company or codebase may configure this workflow differently.
- The unit of autonomy is not only the agent; it is the workflow around the agents.

/title: AdaL Engineer — Our First Experiment

- AdaL Engineer is SylphAI’s first experiment with this thesis.
- It works with existing coding, browser, research, and review agents.
- It allocates, prompts, coordinates, safeguards, and monitors them.
- It carries codebase context, documentation, decisions, and persistent work state.
- Its near-term goal is to deliver one engineering task end-to-end at human-level quality.

/title: An Experiment, Not a Finished Answer

- AdaL Engineer is not a finished answer.
- It lets people directly experience the potential of workflow-level autonomy.
- It also exposes the remaining gaps in context, memory, evaluation, safety, and judgment.
- We want practitioners to help identify those gaps and build this future with us.
- Proposed new supporting slide or spoken transition into the demo.

/title: Demo — A Visible, Verifiable Workflow

- Begin with a clear goal, scope, and quality bar.
- Show AdaL Engineer selecting and coordinating workers.
- Show the builder, evaluator, feedback, correction, and retained state.
- End with evidence—not only an agent claiming that the work is complete.
- Ask the interviewer to challenge unclear requirements and request proof.

/title: What Will Humans Do Next?

- Loop engineering does not remove humans from the loop.
- Left / Addy Osmani (we agree): humans keep the agency—accountability and answerability for what ships. Agents can run more of the inner loop; humans still own the outer-loop verdict.
- Right / AdaL (our view): most engineers move to higher-leverage decision points, with more time freed for deciding what to build and why.
- That higher-leverage work includes:
  - researching new opportunities
  - talking with users
  - exploring product needs and leads
  - brainstorming with teammates
- Human attention moves closer to metrics, user outcomes, and product impact—not away from responsibility.
- Autonomy and agency stay paired: autonomy is how much work the system can carry; agency is who remains answerable.
- Our builder angle: workflow infrastructure raises autonomy so agency can stay high-leverage instead of becoming 12 hours of babysitting.

/title: Beyond Engineering

- The same infrastructure could support other professional workflows.
- An autonomous designer could coordinate research, UI generation, browser evaluation, and brand context.
- An autonomous video producer could coordinate scripts, assets, editing, review, and publishing.
- The underlying agents may be similar; the workflow, context, memory, and quality bar make the role different.
- Proposed new supporting slide.

/title: What Future Are We Building?

- The goal is not to remove experts.
- It is to stop requiring experts to carry every intermediate step manually.
- Combined belief: humans keep agency—accountability and answerability—while most engineering time moves to higher-leverage decisions about what to build.
- That includes research, user conversations, product exploration, and team brainstorming, with clearer ownership of metrics and impact.
- Osmani is a useful external reference for outer-loop ownership. Our contribution is workflow infrastructure that makes higher autonomy real without drowning people in orchestration.
- The invitation: experience the first experiment, identify the gaps, and help build this future together.
