# Beyond Loop Engineering — Spoken Script

Target: ~20–30 minutes core talk, plus demo and discussion.
Style: conversational, knowledge-sharing, not a product pitch.

## Deck order (enabled slides)

1. Beyond Loop Engineering
2. Why We’re Here
3. More Productive. More Drained.
4. Where We Are
5. Agents: From ReAct to Coding Agents
6. Harness: What Makes an Agent Real
7. Loop Engineering
8. Why Loops Became Possible
9. Loops of Today
10. Yet It's Still Hard
11. A Different Path to Autonomy
12. AdaL Engineer — Our First Experiment
13. What the Experiment Is Testing
14. When to Use Loops — and When Not
15. AdaL Builder / Evaluator Screenshot
16. Demo Comparison
17. Measure Autonomy
18. What Will Humans Do Next?
19. References

## Narrative spine

1. More productive and more drained (trust–verification gap)
2. Model capability ≠ autonomy
3. Layers: Model → Agent+Harness → Loop Engineering (workflow)
4. Building blocks exist; the system around them is still hard
5. Different path: engineer-layer agent above workers, not a fatter coding agent
6. AdaL Engineer = first experiment
7. Close: agency stays human; engineers move to higher leverage

---

/title: Beyond Loop Engineering

Hi everyone. I’m Li Yin — co-founder and CEO of AdaL, and the creator of AdalFlow.

Today is about what happens beyond prompting, and beyond the first generation of coding agents.

---

/title: Why We’re Here

I am an ex-AI researcher at Meta AI. For about three years I worked on building LLM harnesses—the systems that turn a raw model into something that can actually do work. That work became AdalFlow, an open-source library for building and auto-optimizing LLM applications. I’m proud of that lineage, because it taught me something early: model intelligence alone is never enough. You need the system around the model.

About a year ago, we started building AdaL from the internal lessons behind AdalFlow. AdaL is an AI research lab. Our focus is autonomy—especially agents and memory.

We care deeply about this problem. This field is still young. Nobody has all the answers yet. The teams shipping coding agents, the people writing about loop engineering, and the engineers babysitting agents every day are all discovering the shape of this problem in real time.

That is why I am here today with Akshay — another well-known educator and builder — to sit down and discuss. I want to share what we have learned as builders, put language around the problems we keep running into, and think with you about where autonomy goes next.

Along the way, I want us to hold a few questions together:

First: why isn’t model capability the same as autonomy?
Second: what is the next stage of autonomy after today’s coding agents?
Third: when should we push for more autonomous loops — and when should we keep the human deeply in the creative loop?
And finally: if work becomes more autonomous, what do engineers do next — and how is that different from agency?

I don’t think these have one final answer yet. But they are the right questions if we want the future to feel exciting instead of exhausting.

So let’s start with the feeling a lot of us already have.

---

/title: More Productive. More Drained.

Coding agents have made developers more productive. That part is real. We plan faster, scaffold faster, implement faster, and get to a first draft of a change much sooner than before.

But many of us also feel more drained. Midjourney’s founder put it bluntly: these tools make engineers more productive — and “extremely drained.”

This is no longer a niche habit. Sonar’s 2026 State of Code report found that about 42% of committed code is AI-generated or significantly AI-assisted. Creation got cheaper. The scarce resources became human review, validation, understanding, and ownership.

Addy Osmani’s framing is useful here: generation moved faster than control. That is the trust-verification gap. We can produce more, but we still have to watch, correct, and answer for the result.

If models are already so good at coding, why are we still babysitting our coding agents twelve hours a day?

You say, “Please fix A,” and it fixes A—but also changes B. Or it solves the problem in a way that does not fit the rest of your codebase — alien code. Or it gets halfway through the task and needs you to take over again.

So the experience is strange. These systems can feel extremely capable at generating code, and still surprisingly limited when we try to trust them with the full job. The hard question is no longer only whether an agent can produce code. It is whether we can trust it to deliver the right outcome.

---

/title: Where We Are

The next question is structural: where are we stuck?

Think about what it takes to deliver one pull request from start to finish. You have to understand the problem, plan the change, write the code, test it, review it, fix what broke, and iterate until it is actually ready.

Today’s agents can already perform many of those steps. They can search a codebase, edit files, run commands, open a browser, and even draft a PR.

But humans are still connecting the workflow.

There are three reasons this becomes babysitting.

First, we still drive the outer loop of the dev lifecycle. It is still manual: understand, plan, build, test, review, iterate, deliver — across local, cloud, and GitHub environments — allocating and monitoring agents across stages.

Second, humans are still the glue of long-term context. We carry context between agents. We approve the risky actions. We decide when to continue, correct, escalate, or stop.

Third, faster generation creates more judgment work. More output. More alien code. More micro-decisions.

That is the deeper exhaustion. For one feature, there may be a hundred plausible implementations. Only a few truly fit this codebase, this architecture, these product constraints, and the decisions your team has already made. An agent can generate options quickly. The developer still has to choose what fits, review more, and correct what does not. Faster generation can multiply the decision burden and the review burden at the same time.

**So this is the first counterintuitive point of the talk: model capability is not autonomy.**

Model asks: can it reason and produce strong work?
Autonomy asks: can the system carry responsibility from a goal to a verified outcome?

We can visualize it in three layers. Existing agent + harness is L1 autonomy — generate and act in an environment. If we can achieve a well-defined goal with a desired outcome that fits the codebase and the developer’s requirements, fully autonomously, we move toward L2 autonomy.

The agent and harness are infrastructure that acts in a real environment — tools, files, browser, runtime. Agents are the arms.

The third layer is still mostly the human manual workflow: the outer loop on the slide — understand, plan, build, test, review, iterate, deliver. Humans still own context, handoffs, judgment, and when to stop.

Generate. Act. Still babysit the outer loop.

Which leads to one question:

Is loop engineering the answer?

Before we define loop engineering, we need two pieces of builder vocabulary: agents, and the harness around them.

---

/title: Agents: From ReAct to Coding Agents

Agents started even before ChatGPT — in 2022. The original ReAct paper showed a simple pattern: reason, act, observe, and repeat. At first, agents could only take a few steps.

Today, with better models, tool calling, longer context, and stronger systems around them such as constrained decoding, agents can run for many steps, call tools in parallel, support hundreds of tools, search codebases, use browsers, and complete substantial parts of a task.

The most powerful everyday example is coding agents.

And if we think about subagents, they are often just another tool in that loop — a specialized worker the main agent can call.

**So let’s be clear: today’s agents are already useful. They already have meaningful task-level ability. They can be designed to be secure and robust — and still require constant human input to complete a full task. The problem is that executing steps is not the same as owning the full engineering workflow.**

---

/title: Harness: What Makes an Agent Real

A harness is the code that takes a model and turns it into an agent system in a real environment. Claude Code is a harness. Codex, OpenCode, AdalFlow, and AdaL are all harnesses. The harness is the infrastructure that lets the model act.

So how do prompt engineering and context engineering fit in?

The original ReAct paper’s source code was an early harness, where prompt engineering played the biggest role: simple tool calls, and the prompt largely decided the system’s output — especially in 2023 and 2024.

As context windows grew — from tens of thousands of tokens toward hundreds of thousands and a million — the harness had to grow too. It is no longer only a simple prompt. It includes tools and MCP, skills, file and image inputs, compaction, prompt structure and caching, and the runtime environment. “Context engineering” as a term really emerged in 2025.

**But even a strong harness does not automatically automate the human outer loop. That is the gap we are naming with loop engineering.**

---

/title: Loop Engineering

This is where loop engineering enters the conversation.

Developers are tired of manually gluing the workflow together. The industry shift is simple to say out loud: instead of prompting, build loops that prompt the system.

“Loop engineering” is still an emerging term. People we respect — Addy Osmani, Andrew Ng, Akshay, Karpathy’s LOOPS.md — have been naming this direction from different angles. We are very much aligned with that direction.

As builders, we use a working definition that makes the outer-loop claim cleaner and precise enough to build against:

A goal-driven system that coordinates multiple agents to a verified outcome — autonomously, without humans in the loop.

That last part matters. Not “helps you prompt faster.” Not “stays useful while you babysit.” Autonomous means the outer loop can run toward a verified outcome without a human glued inside every step.

Humans may still set the goal, the quality bar, and the stop conditions — and keep agency over what ships. But the loop itself should not require constant human orchestration to keep moving.

---

/title: Why Loops Became Possible

Two capability shifts made the outer loop automatable in principle.

First: self-validation. Browser use and computer use let agents close the test loop. They can check their own work with evidence — not only claim success.

Second: multi-agent roles. We understand context rot better now — performance degrades, format slips, the agent forgets state, gets too optimistic about its own work. So we separate roles: Builder and Evaluator, isolated context, specialized prompts, independent review.

Those two shifts matter. They make autonomous loops possible.

They do not yet make the full human outer loop reliable.

---

/title: Loops of Today

What’s exciting is that a lot of the building blocks for loops already exist today.

We have recurring workflows and scheduled goals — `/goal`, `/loop` in Claude Code, `/cron` in AdaL — systems that can keep going until a task is complete. We have dynamic workflows that adapt as they run, and agent teams that can parallelize work. We also have more autonomous permission modes — things like `/yolo`, or the very funny but very real `dangerously-skip-permissions` mode — where you can let the agent operate with much less interruption.

So the primitives for loops are starting to become real. The field is already shipping pieces. We’re still trying.

---

/title: Yet It's Still Hard

But the key point is: the surrounding system is still hard.

Just because you can turn on `/yolo` or `dangerously-skip-permissions` doesn’t mean you automatically get production-quality autonomy.

High complexity. Which agents should participate? What context does each one need, and when? How do they hand work off? How is quality evaluated independently — testing, review, recovery — without the same agent grading its own homework? How do you keep documentation and long-term state coherent as the work changes? Those choices differ by company, by role, and even by codebase.

High cost — tokenmaxxing. More agents, more context, more validation, and repeated iterations all compound runtime cost. Autonomy is not free just because permissions are loose.

The Codex team is a really good example. They’ve shown that a lot is possible — even toward zero manually written lines — but it still takes a whole team and a carefully designed system around the agents: documentation, context, review, and the harness.

So the real challenge is not just having the building blocks. It’s building the system around them.

---

/title: A Different Path to Autonomy

This is the key slide of the talk. So I want to take it from a slightly different angle.

One path is: keep building on coding agents of today. Make the single agent smarter, longer-running, more autonomous. Stuff more of the product lifecycle into that one trajectory.

I don’t think that’s the right primary path.

Today’s coding agents are still mainly single-agent systems. Yes — Claude agent teams are multi-agent, but they are aiming at parallel work: more workers side by side. That is not the same as what the engineer is doing today with coding agents — owning the outer loop, allocating work, carrying context, evaluating, and driving the lifecycle across stages.

Real product development is multi-stage — understand, plan, build, test, review, iterate, deliver. If you push that whole outer loop into the worker stack, you complicate an already well-defined infra scope: tools, context, permissions, the harness that makes the agent real.

And coding agents are already excellent workers when humans want to work with them manually. That collaboration mode should stay clean and simple. Don’t ruin the worker by forcing it to also be the engineer.

So instead, we model loop engineering from what the engineer still does today.

Go back to the third layer — the human outer loop. That is still mostly human: set the goal and quality bar, allocate and prompt the right workers, carry context and long-term memory, evaluate independently and recover, know when to stop or escalate.

Babysitting is what it feels like when a human is still running that runtime by hand.

The move is: replace that engineer role with another agent — not instead of coding agents, but above them. Let this engineer-level agent model the behaviors of existing engineers, and work with the coding agents, browser agents, research agents, and review agents of today.

Keep the workers as workers. Automate the engineer layer.

We don’t need a better coding agent alone.
We need an agent that can sit in the engineer seat and operate today’s agents toward a verified outcome.

Autonomy rises when we automate the engineer layer — not when we overload a single worker.

---

/title: AdaL Engineer — Our First Experiment

This is the visualization of that path.

AdaL Engineer is our first experiment with the previous slide’s thesis. Look at the diagram: one engineer-level agent above today’s workers — coding, browser use, deep research, code review. Not a bigger coding agent. A separate layer that operates the workers.

Our near-term goal is practical and bounded: deliver one engineering task end-to-end at human-level quality.

And I want to be honest about where we are. This is not a finished answer. It will fail in places. It will expose gaps in context, memory, evaluation, safety, and judgment. That is part of the point of an experiment.

We are not asking you to believe a pitch. We are asking you to inspect the diagram, inspect the goal, and later inspect the loop.

---

/title: What the Experiment Is Testing

If AdaL Engineer is sitting in the engineer seat, what is the experiment actually testing?

Five parts of the engineer runtime.

First: operate workers — allocate, prompt, and monitor the right agents.

Second: retain state — carry progress, decisions, and context across iterations.

Third: evaluate independently — a Builder implements; an Evaluator does not grade its own homework. That separation is the science beat. Same family of idea as adversarial training: one side produces, another side checks.

Fourth: bound the loop — know when to stop, escalate, or hand the work back to a human.

Fifth: adaptive autonomy — orchestrate the workflow autonomously, but allow seamless manual takeover when you need to correct, redirect, or multi-task. Autopilot when it should run; human hands back on the controls when it shouldn’t.

---

/title: When to Use Loops — and When Not

Now that you’ve seen what the experiment is testing, one boundary matters.

Loop engineering only makes sense when the outcome is clear enough to delegate.

Use loops when the goal can be verified: a concrete outcome, success criteria you can check, scope and stop conditions, and you’re ready to hand off execution. A good fit is shipping a scoped PR to green with a known quality bar.

Do not force loops when you’re still discovering the goal. If the idea is unclear or evolving, if you want to brainstorm, design, or stay deep in the creative process, today’s agents as collaborators are the right tool. That is not a failure of autonomy. That is the right interaction model for discovery work.

The sharp anti-example: “Make a billion. Make no mistakes.” That is motion without a stop condition. Don’t put a loop on that.

Use loop engineering when the outcome is clear enough to delegate.
Use today’s agents when discovering the goal is part of the work.

---

/title: AdaL Builder / Evaluator Screenshot

Here’s what that looks like in practice — not a polished product shot, just evidence of the loop.

You’ll see Builder and Evaluator workers in the wild: work happening, review happening, state being carried. Hold the standard we set earlier: not whether the system claims success, but whether you can see the workflow.

---

/title: Demo Comparison

In the demo, I do not want you to watch magic. I want you to watch a loop.

We will start with a clear goal, a clear scope, and a clear quality bar. Then we will show AdaL Engineer selecting and coordinating workers. You should see building, evaluation, feedback, correction, and retained state.

If we show a comparison, treat it as one experimental run — not a leaderboard. Same class of task, browser use to check work, multiple iterations. The question is what the loop did with evidence, not who “won.”

At the end, challenge it. Ask what the goal was. Ask what was verified. Ask what would make us stop or escalate. That is the standard this system should be held to.

---

/title: Measure Autonomy

If we take this seriously, we also need a way to talk about progress without collapsing everything into model benchmarks.

Model capability can keep rising while engineering autonomy stays low — that’s the babysitting regime. Loop engineering is an attempt to climb the autonomy axis: from heavy supervision, toward single-task delivery, toward multi-task coordination, and eventually toward team-level workflow systems.

AdaL Engineer sits on that curve as a near-term experiment: deliver a task end-to-end. The farther points — continuous learning memory, a company brain — are direction, not claims of arrival.

---

/title: What Will Humans Do Next?

So if more of the workflow becomes autonomous, what do humans do next?

We do not remove humans from the loop.

On one side, we agree with Addy Osmani: humans keep the agency. Agents can run more of the inner execution loop, but people still own accountability and answerability for what ships. Someone still has to stand behind the evidence, the risk, and the production decision.

On the other side, this is AdaL’s view: most engineers will move to higher-leverage decision points. They get time back from babysitting intermediate steps, and they can spend more of that time deciding what to build and why.

That higher-leverage work includes researching new opportunities, talking with users, exploring product needs, brainstorming with teammates, and taking clearer ownership of metrics and product impact.

Autonomy and agency are not the same thing.
Autonomy is how much work the system can carry.
Agency is who remains answerable.

Our builder belief is that workflow infrastructure can raise autonomy so human agency can stay high-leverage, instead of collapsing into twelve hours of supervision.

If this pattern is real, it will not stop at software engineering. The same infrastructure could support other professional workflows — a designer, a video producer — each coordinating capable agents around that expert’s workflow and quality bar. Not one magical general agent for every profession, but role-level systems.

---

/title: References

I’ll leave the references on screen. The goal is not to remove experts. The goal is to stop requiring experts to carry every intermediate step manually.

Humans keep agency — accountability and answerability. Engineering attention moves upward, toward what to build, why it matters, and whether we can answer for it.

I am proud of what AdaL is trying to do as a research lab. I am also here with humility. This field is unfinished. The best thing we can do is make the experiment legible, tell the truth about the gaps, and build the next layer together.

Thank you. Let’s keep the conversation going.
