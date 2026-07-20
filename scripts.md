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
11. What the Engineer Still Does
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
5. AdaL Engineer = experiment in workflow infrastructure
6. Close: agency stays human; engineers move to higher leverage

---

/title: Beyond Loop Engineering

Hi everyone. I’m Li Yin — co-founder and CEO of AdaL, and the creator of AdalFlow.

Today is about what happens beyond prompting, and beyond the first generation of coding agents.

---

/title: Why We’re Here

I am an ex-AI researcher at Meta AI. For about three years I worked on building LLM harnesses—the systems that turn a raw model into something that can actually do work. That work became AdalFlow, an open-source library for building and auto-optimizing LLM applications. I’m proud of that lineage, because it taught me something early: model intelligence alone is never enough. You need the system around the model.

About a year ago, we started building AdaL from the internal lessons behind AdalFlow. AdaL is an AI research lab. Our focus is autonomy—especially agents and memory.

We care deeply about this problem. This field is still young. Nobody has all the answers yet. The teams shipping coding agents, the people writing about loop engineering, and the engineers babysitting agents every day are all discovering the shape of this problem in real time.

That is why I am here today with Akshay — another well-known educator and builder — to sit down and discuss. Not to claim that we have finished the future, but to share what we have learned as builders, put language around the problems we keep running into, and think with you about where autonomy goes next.

Along the way, I want us to hold a few questions together — in the same order we’ll explore them tonight:

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

This is no longer a niche habit. Sonar’s 2026 State of Code report found that about 42% of committed code is AI-generated or significantly AI-assisted. Creation got cheaper. The scarce resources became review, validation, understanding, and ownership.

Addy Osmani’s framing is useful here: generation moved faster than control. That is the trust-verification gap. We can produce more, but we still have to watch, correct, and answer for the result.

If models are already so good at coding, why are we still babysitting our coding agents twelve hours a day?

You say, “Please fix A,” and it fixes A—but also changes B. Or it solves the problem in a way that does not fit the rest of your codebase — alien code. Or it gets halfway through the task and needs you to take over again.

So the experience is strange. These systems can feel extremely capable at generating code, and still surprisingly limited when we try to trust them with the full job. The hard question is no longer only whether an agent can produce code. It is whether we can trust it to deliver the right outcome.

---

/title: Where We Are

After the drained feeling, the next question is structural: where are we stuck?

Think about what it takes to deliver one pull request from start to finish. You have to understand the problem, plan the change, write the code, test it, review it, fix what broke, and iterate until it is actually ready.

Today’s agents can already perform many of those steps. They can search a codebase, edit files, run commands, open a browser, and even draft a PR.

But humans are still connecting the workflow.

There are three reasons this becomes babysitting.

First, humans are still the glue. We carry context between agents, tabs, environments, and stages. We approve the risky actions. We decide when to continue, correct, escalate, or stop.

Second, the outer loop is still manual: understand, plan, build, test, review, iterate, deliver.

Third, faster generation creates more judgment work. More output. More alien code. More micro-decisions.

That is the deeper exhaustion. For one feature, there may be a hundred plausible implementations. Only a few truly fit this codebase, this architecture, these product constraints, and the decisions your team has already made. An agent can generate options quickly. The developer still has to choose what fits, review more, and correct what does not. Faster generation can multiply the decision burden and the review burden at the same time.

So this is the first counterintuitive point of the talk: model capability is not autonomy.

Model capability asks: can it reason and produce strong work?
Autonomy asks: can the system carry responsibility from a goal to a verified outcome?

Those are not the same question. You can have a brilliant model inside a fragile workflow and still babysit it all day.

I find it useful to separate three layers.

First, model intelligence: it can reason and generate.

Second, the agent and harness: infrastructure that acts in a real environment — tools, files, browser, runtime. Agents are the arms.

Third, today, is still mostly a human manual workflow. That is the outer loop on the slide: understand, plan, build, test, review, iterate, deliver. Humans still own context, handoffs, judgment, and when to stop.

Generate. Act. Still babysit the outer loop.

Which leads to one question:

Is loop engineering the answer?

Not “do we need better models?”
Not “can agents write code?”
But: can we automate more of this workflow layer — without removing human agency?

Before we answer that, let’s fix the terminology — as builders and as scientists — so loop engineering has a clear place in the stack.

Before we define loop engineering, we need two pieces of builder vocabulary: agents, and the harness around them.

---

/title: Agents: From ReAct to Coding Agents

Agents are not brand new. In 2022, ReAct showed a simple pattern: reason, act, observe, and repeat. At first, agents could only take a few steps.

Today, with better models, tool calling, longer context, and stronger systems around them, agents can run for many steps, call tools in parallel, search codebases, use browsers, and complete substantial parts of a task.

The most powerful everyday example is coding agents.

And if we think about subagents, they are often just another tool in that loop — a specialized worker the main agent can call.

So let’s be clear: today’s agents are already useful. They already have meaningful task-level ability. The problem is not that agents can do nothing. The problem is that executing steps is not the same as owning the full engineering workflow.

---

/title: Harness: What Makes an Agent Real

A harness is the code that takes a model and turns it into an agent system in a real environment.

The original ReAct paper’s source code was an early harness. Claude Code is a harness. Open-source coding agents are harnesses. AdalFlow was our early work in this layer. AdaL continues that work.

As context windows grew — from tens of thousands of tokens toward hundreds of thousands and a million — the harness had to grow too. It is no longer only a prompt. It includes tools and MCP, skills, file and image inputs, compaction, prompt structure and caching, and the runtime environment.

That is why people started talking about prompt engineering, then context engineering, then harness engineering. The model is the intelligence. The harness is the infrastructure that lets it act.

But even a strong harness does not automatically automate the human outer loop. That is the gap we are naming with loop engineering.

---

/title: Loop Engineering

This is where loop engineering enters the conversation.

Developers are tired of manually gluing the workflow together. The industry shift is simple to say out loud: instead of prompting, build loops that prompt the system.

“Loop engineering” is still an emerging term. The definition is not settled. Addy Osmani, Andrew Ng, Akshay, Karpathy’s LOOPS.md — people are naming the same direction from different angles. We think that direction is right, and still incomplete.

So this is AdaL’s opinion of how loop engineering should be judged:

A goal-driven system that coordinates multiple agents to a verified outcome — autonomously, without humans in the loop.

Not a better one-shot prompt. Not a longer chat. A system that can carry work toward a verified result.

---

/title: Why Loops Became Possible

Two capability shifts made the outer loop automatable in principle.

First: self-validation. Browser use and computer use let agents close the test loop. They can check their own work with evidence — not only claim success.

Second: multi-agent roles. We understand context rot better now — performance degrades, format slips, the agent forgets state, gets too optimistic about its own work. So we separate roles: Builder and Evaluator, isolated context, specialized prompts, independent review.

Those two shifts matter. They make autonomous loops possible.

They do not yet make the full human outer loop reliable.

---

/title: Loops of Today

And the field is already shipping pieces. We’re still trying.

Claude Code, AdaL, agent teams — real attempts at goals, schedules, permissions, and parallel work.

You can already see the building blocks:

Repeat and schedule — `/goal`, `/loop` in Claude Code; `/cron` in AdaL.

Permission modes — `--dangerously-skip-permissions`, `--yolo` — more autonomy, more risk.

Dynamic workflows — agents that adapt the plan as they run.

Agent teams — parallel full agents for execution at scale.

So the problem is no longer that models cannot write code or use tools. The primitives exist. People are putting loops in production today.

---

/title: Yet It's Still Hard

Yet it’s still hard.

Building blocks exist. The system around them is still hard.

OpenAI’s Codex example is the clean proof point. It took a whole Codex team to reach zero manually written lines — and a full engineering team still maintains documentation, context, review, and the harness.

High complexity. High cost.

Which agents should participate? What context does each one need, and when? How do they hand work off? How is quality evaluated independently? How does the system recover, update documentation, and know when to stop?

Those choices differ by company, by role, and even by codebase. Capable agents alone are not enough.

---

/title: What the Engineer Still Does

So what exactly is still hard?

It’s not that workers can’t code. Coding agents, browser agents, research agents, review agents — they already execute steps.

What’s still mostly human is the engineer role: the runtime that turns those workers into a shipped outcome.

The engineer still sets the goal and the quality bar. Allocates and prompts the right workers. Carries codebase and product context, and long-term memory across the work. Evaluates independently and recovers when things fail. Decides when to stop — or when to escalate.

That is the outer job. Babysitting is what it feels like when a human is still doing that runtime by hand.

So here is the belief, stated cleanly:

We don’t need a better coding agent alone.
We need to automate more of the engineer role around today’s agents.

Autonomy rises when the workflow role is automated — not when one worker gets smarter.

The next-generation system is not simply a smarter worker. It is infrastructure for operating existing capable agents inside a role-specific workflow. The unit of autonomy is not only the agent. It is the configured workflow around the agents.

Near-term bar, kept honest: deliver one engineering task end-to-end at human-level quality.

---

/title: AdaL Engineer — Our First Experiment

This is where AdaL Engineer comes in—and I want to introduce it carefully.

It is our first experiment with the thesis on the previous slide. Not the whole future. Our first attempt to automate the engineer role — by operating today’s workers inside a higher-level workflow.

It works with existing coding, browser, research, and review agents. It allocates, prompts, coordinates, safeguards, and monitors them. It carries codebase context, documentation, decisions, and persistent work state.

Near-term goal, kept practical and bounded: deliver one engineering task end-to-end at human-level quality.

We built coding agents and harnesses for years. AdaL Engineer is the next step: not replacing those agents, but sitting in the engineer seat above them.

I want to be honest. It is not a finished answer. It will fail in places. It will expose gaps in context, memory, evaluation, safety, and judgment. That is part of the point.

We are not asking you to believe a pitch. We are asking you to inspect an experiment.

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
