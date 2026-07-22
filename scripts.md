# Beyond Loop Engineering — Spoken Script

Target: ~20–30 minutes core talk, plus demo and discussion.
Style: conversational, knowledge-sharing, not a product pitch.
Cadence: natural spoken English — full sentences you can say out loud, easy to remember.

## Deck order (enabled slides)

1. Beyond Loop Engineering
2. Why We’re Here
3. More Productive. More Drained.
4. Where We Are Stuck
5. Agents: From ReAct to Coding Agents
6. Harness: What Makes an Agent Real
7. Loop Engineering
8. Patterns of Today
9. Claude Code: Multi-Agent as One Agent’s Tools (screenshot)
10. What Makes Outer-Loop Automation Possible
11. Yet It's Still Hard
12. When Understanding Falls Behind
13. A Different Path to Autonomy
14. AdaL Engineer — Our First Experiment
15. What the Experiment Is Testing
16. When to Use Loops — and When Not
17. AdaL Builder / Evaluator Screenshot
18. Demo Comparison
19. Measure Autonomy
20. What Will Humans Do Next?
21. References

## Narrative spine

1. More productive and more drained (trust–verification gap)
2. Model capability ≠ autonomy
3. Layers: Model → Agent+Harness → Loop Engineering (workflow)
4. Building blocks exist; the system around them is still hard
5. Understanding falls behind: cognitive debt, surrender, orchestration tax
6. Different path: engineer-layer agent above workers, not a fatter coding agent
7. AdaL Engineer = first experiment — maintain docs, deliver structured output
8. Close: agency stays human; engineers move to higher leverage

---

/title: Beyond Loop Engineering

Hi everyone. I’m Li Yin — co-founder and CEO of AdaL, and the creator of AdalFlow.

Today I want to talk about what happens beyond prompting, and beyond the first generation of coding agents.

---

/title: Why We’re Here

I’m an ex-AI researcher at Meta AI. For the last three years I’ve been working on LLM harnesses, including AdalFlow — the open-source library for building and auto-optimizing LLM applications. One of the earliest lessons AdalFlow taught me is that model intelligence alone is never enough.

About a year ago we started building AdaL from those internal lessons. AdaL is an AI research lab, and our focus is autonomy — especially agents and memory.

This field is still young, and nobody has all the answers yet. The teams shipping coding agents, the people writing about loop engineering, and the engineers babysitting agents every day are all discovering the shape of this problem in real time.

That’s why I’m here today with Akshay — to share what we’ve learned as builders, put language around the problems we keep running into, and think with you about where autonomy goes next.

Along the way, I’d like us to hold a few questions together. First: why isn’t model capability the same as autonomy? Second: what comes after today’s coding agents? Third: when should we push for more autonomous loops, and when should we keep the human deeply in the creative loop? And finally: if work becomes more autonomous, what do engineers do next — and how is that different from agency?

Let’s start with the feeling a lot of us already have.

---

/title: More Productive. More Drained.

Coding agents have made developers more productive, and that part is real. We plan faster, scaffold faster, implement faster, and get to a first draft of a change much sooner than before.

Sonar’s 2026 State of Code report found that about 42% of committed code is AI-generated. Creation got cheaper, and the scarce resources became human review, validation, understanding, and ownership.

Addy Osmani has a useful framing here: generation moved faster than control. That’s the trust-verification gap. We can produce more, but we still have to watch it, correct it, and answer for the result.

Midjourney’s founder put the human cost bluntly: these tools make engineers more productive — and “extremely drained.”

So if agents are so good, why are we babysitting coding agents twelve hours a day?

You say, “Please fix A,” and it fixes A — but also changes B. Or it solves the problem in a way that doesn’t fit the rest of your codebase — alien code, as I call it. Or it gets halfway through the task and needs you to take over again.

---

/title: Where We Are Stuck

So we are stuck.

Think about what it takes to deliver one pull request from start to finish. You have to understand the problem, plan the change, write the code, test it, review it, fix what broke, and iterate until it’s actually ready.

Today’s agents can already perform many of those steps. They can search a codebase, edit files, run commands, open a browser, and even draft a PR.

But humans are still connecting the workflow.

**There are three reasons this becomes babysitting.**

First, we still drive the outer loop of the dev lifecycle. It’s still manual across local, cloud, and GitHub environments — allocating and monitoring agents across stages.

Second, humans are still the glue of long-term context. We carry context between agents, we approve the risky actions, and we decide when to continue, correct, escalate, or stop.

Third, faster generation creates more judgment work — more output, more alien code, and more micro-decisions.

That’s the deeper exhaustion. For one feature, there may be a hundred plausible implementations, and only a few truly fit this codebase, this architecture, these product constraints, and the decisions your team has already made. An agent can generate options quickly, but the developer still has to choose, review, and correct. Faster generation can multiply the decision burden and the review burden at the same time.

**The first point of the talk today: model capability is not autonomy.**

The model asks: can it reason and produce strong work?
Autonomy asks: can the system carry responsibility from a goal to a verified outcome?

We can visualize this in three layers. Existing agent plus harness is L1 autonomy — generate and act in an environment. If we can achieve a well-defined goal with a desired outcome that fits the codebase and the developer’s requirements, fully autonomously, we move toward L2 autonomy.

The agent and harness are infrastructure that acts in a real environment — tools, files, browser, runtime. Agents are the arms.

The third layer is still mostly the human manual workflow: the outer loop on the slide — understand, plan, build, test, review, iterate, deliver. Humans still own context, handoffs, judgment, and when to stop.

Which leads to one question: is loop engineering the answer?

Before we define loop engineering, we need two pieces of builder vocabulary: agents, and the harness around them.

---

[can try to be quick]

/title: Agents: From ReAct to Coding Agents

Agents started even before ChatGPT — in 2022. The original ReAct paper showed a simple pattern: reason, act, observe, and repeat. At first, agents could only take a few steps.

Today, with better models, tool calling, longer context, and stronger systems around them such as constrained decoding, agents can run for hundreds of steps, call tools in parallel, support hundreds of tools, search codebases, use browsers, and complete substantial parts of a task.

The most powerful everyday example is coding agents. And if we think about subagents, they are often just another tool in that loop — a specialized worker the main agent can call.

**So let’s be clear: today’s agents are already useful. They already have meaningful task-level ability. They can be designed to be secure and robust — and still require constant human input to complete a full task. The problem is that executing steps is not the same as owning the full engineering workflow.**

---

/title: Harness: What Makes an Agent Real

Just a quick intro to the terminology.

A harness is the code that takes a model and turns it into an agent system in a real environment. Claude Code is a harness. Codex, OpenCode, and AdaL are all harnesses. The harness is the infrastructure that lets the model act.

So how do prompt engineering and context engineering fit in?

The original ReAct paper’s source code was an early harness, where prompt engineering played the biggest role: simple tool calls, and the prompt largely decided the system’s output — especially in 2023 and 2024.

As context windows grew — from tens of thousands of tokens toward hundreds of thousands and a million — the harness had to grow too. It’s no longer only a simple prompt. It includes tools and MCP, skills, file and image inputs, compaction, prompt structure and caching, and the runtime environment. “Context engineering” as a term really emerged in 2025, and it’s used to describe an agent’s context structure.

---

/title: Loop Engineering

Loop engineering has become the talk of the town.

Developers are tired of manually gluing the workflow together. Addy Osmani, Andrew Ng, Akshay, Karpathy’s LOOPS.md — people have been naming this direction from different angles, but they all agree on one sentence: instead of prompting, build loops that prompt the system.

“Loop engineering” is still an emerging term. Here’s our definition, and I think it’s easier to build upon.

A goal-driven system that coordinates multiple agents to a verified outcome — autonomously, without humans in the loop.

Autonomous for us means the outer loop can run toward a verified outcome without a human glued inside every step.

**Humans may still set the goal, the quality bar, and the stop conditions — and keep agency over what ships. But the loop itself should not require constant human orchestration to keep moving.**

---

/title: Patterns of Today

The field is shipping patterns.

On the single-agent side, we already have recurring workflows and scheduled goals — `/goal`, `/loop` in Claude Code, `/cron` in AdaL. We also have more autonomous permission modes — things like `--yolo`, or `dangerously-skip-permissions` — where you can let the agent operate with no interruption. The point is simple: one agent, with more freedom to keep going.

That helps. It’s also too simple, because you still have one trajectory and one context. A single long context fails in three ways: agentic laziness — it reviews thirty-five of fifty files and stops; self-preferential bias — it grades its own work too kindly; and goal drift — compaction quietly changes the mission.

Then multi-agents showed up, and there are really two different patterns here. Dynamic workflows and agent teams are both defined for task parallelization and to fight context rot.

Dynamic workflows build an agent-compiled workflow: a control plan or graph whose topology is generated by an agent early in an episode, and thereafter largely executed as a bound artifact, with each run using a clean context window.

Agent teams are similar in spirit: the main coding agent decides dynamically what to spawn next based on what comes back. The key property is that parallel peer agents can message each other — not only report up. But coordination gets expensive, and transparency drops fast.

**So the pattern set today is not enough. Single-agent is too simple. Multi-agent is too opaque, too complex, and non-transparent. Both lean parallel. Real outer-loop engineering is mostly iterative. That is the gap.**

---

/title: Claude Code multi-agent screenshot

A quick product example helps make the architecture concrete.

I asked Claude Code a simple question: can you use dynamic workflows and agent teams?

What it showed me was really useful. In its own UI, agent teams show up as the Agent tool. Dynamic workflows show up as the Workflow tool. Forks, explore, plan, pipeline, parallel work, SendMessage — these are all capabilities available inside the same coding-agent session.

So when we say “multi-agent” today, a lot of what we mean is still one coding agent coordinating work through tools. That is a real step forward. It is also a specific design choice: multi-agent as part of one agent’s toolbelt.

I’m not saying that is wrong. I’m saying it is worth naming clearly. Later, when we talk about AdaL Engineer, the distinction will be easier to see: a separate engineer-layer agent above workers, versus multi-agent tools inside one coding agent.

---

/title: What Makes Outer-Loop Automation Possible

So why are we even talking about automating the outer loop now?

Two capability shifts finally make it possible in principle — especially for a complicated product development lifecycle, not just a one-shot coding task.

First: self-validation. Browser use and computer use are still new, and they are only starting to get mature enough that agents can close the test loop. They can check their own work with evidence — not only claim success. Build something, open it, click through it, inspect the machine, recover when it breaks.

Second: separated roles — and this is where people say “context rot.”

That’s not a universal, standardized definition. The practical meaning is simple: as the context starts to grow, the model becomes increasingly unreliable. It may miss what is already in the window, over-weight the wrong parts, forget earlier constraints, or get too confident about its own prior work. The best research anchor here is still *Lost in the Middle* — Liu et al., 2023 — which showed that even when the answer is in the prompt, long-context models often fail depending on where that information sits.

In agent terms, that is basically the same family of failure that pushed Claude Code toward dynamic workflows: agentic laziness on long checklists, self-preferential bias when one agent grades its own output, and goal drift as the conversation is compacted. Isolation and role separation are the structural response — Builder and Evaluator in separate context, independent review. One agent should not grade its own homework.

Those two shifts matter. They make autonomous outer loops possible. They do not yet make them reliable, cheap, or productized.

---

/title: Yet It's Still Hard

But the surrounding system is still hard.

Just because the conditions exist — or because you can turn on `/yolo` or `dangerously-skip-permissions` — does not mean you automatically get production-quality autonomy.

High complexity. Which agents should participate? What context does each one need, and when? How do they hand work off? How is quality evaluated independently — testing, review, recovery — without the same agent grading its own homework? How do you keep documentation and long-term state coherent as the work changes? Those choices differ by company, by role, and even by codebase.

High cost — tokenmaxxing. More agents, more context, more validation, and repeated iterations all compound runtime cost. Autonomy is not free just because permissions are loose.

The Codex team is a really good example. They’ve shown that a lot is possible — even toward zero manually written lines — but it still takes a whole team and a carefully designed system around the agents: documentation, context, review, and the harness.

So the real challenge is not just having the building blocks. It’s building the system around them — an engineer-layer runtime that can carry that outer loop without a human team glued inside every step. That is the door into AdaL Engineer.

---

/title: When Understanding Falls Behind

Addy Osmani names three dangers that show up as soon as generation outruns comprehension.

First: cognitive debt. The repository grows faster than anyone’s mental model. A build can pass and a PR can merge while the team quietly loses the ability to explain — and maintain — the system it ships.

Second: cognitive surrender. That is not delegation. Delegation means: do the work, then show me enough evidence that I can still form a judgment. Surrender means accepting the agent’s answer before you form an opinion — borrowed confidence. A Wharton study is the warning shot: when AI was wrong, 73% of people still chose the wrong answer and felt more confident.

Third: orchestration tax. Agents parallelize. Human attention does not. Every extra loop creates more decisions to route, merge, verify, and integrate. More running agents do not create more human bandwidth.

So the rule is simple, and hard: explain it or don’t ship it. Ownership without understanding is just deferred risk.

That is why the next slide is not “make the coding agent fatter.” It is about who keeps the system understandable while work is running.

---

/title: A Different Path to Autonomy

One path is: keep stuffing the product lifecycle into today’s coding agent — longer runs, more tools, more multi-agent bolted on.

I don’t think that’s the right primary path.

Coding agents are still mainly single-agent systems. Agent teams and dynamic workflows are tools on that same session. One role is being asked to be autonomous, multi-agent, and manual collaborator at once. That’s too much — and that seat was never designed to own the outer loop: allocate work, carry context, evaluate, and drive the lifecycle.

Keep the worker clean. A worker has a well-defined infra scope: tools, context, permissions, harness. Coding agents are already excellent when humans work with them by hand. Don’t ruin the worker by forcing it to also be the engineer.

So model loop engineering from what engineers still do: set the bar, allocate workers, hold memory, evaluate, stop or escalate — and leave documentation and structured handoff so the next human or agent can review without surrendering judgment.

Babysitting is that runtime run by hand. Autonomy rises when we automate the engineer layer — not when we overload a single worker.

---

/title: AdaL Engineer — Our First Experiment

AdaL Engineer is our first experiment. Notice the identity: not a coding agent with multi-agent tools bolted on — an agent in the engineer seat. It uses today’s workers the way a human does: allocate, prompt, check, revise, hand off.

The near-term goal is bounded: one engineering task end-to-end at human-level quality.

This is an experiment, not a finished answer. It will fail in places — context, memory, eval, safety, judgment. That’s the point. Inspect the diagram, the goal, and later the loop — don’t take a pitch on faith.

---

/title: What the Experiment Is Testing

If AdaL Engineer is sitting in the engineer seat, what is the experiment actually testing?

Five parts of the engineer runtime.

First: operate workers — allocate, prompt, and monitor the right agents.

Second: engineer memory — persistent long-term memory. Carry progress, decisions, and context across iterations, and keep them alive beyond the current chat.

Third: agentic workflow. Independent build/eval is one pattern — useful, but only one form. The engineer can run flexible multi-agent workflows under its control: clearer structure than today’s opaque dynamic workflows, with the main agent remaining agentic about which pattern to use, when to fan out, when to verify, and when to iterate. Not a fixed recipe bolted onto a coding agent.

Fourth: adaptive autonomy — run autonomously. Humans can take over anytime, or collaborate at the same time — correct, redirect, multi-task — without forcing a “bound the loop / stop and escalate” gate as the product. If the loop is always waiting on a human stop condition, it collapses back into a simple single-worker session with a babysitter.

Fifth: avoid cognitive debt — keep the work in a clear structure, and leave a handover that is easy to walk through. Plans, decisions, evidence, and current state should be reviewable without forcing a human to surrender judgment or reverse-engineer the whole run.

---

/title: When to Use Loops — and When Not

Now that you’ve seen what the experiment is testing, one boundary matters.

Loop engineering only makes sense when the outcome is clear enough to delegate.

Use loops when the goal can be verified: a concrete outcome, success criteria you can check, scope and stop conditions, and you’re ready to hand off execution. A good fit is shipping a scoped PR to green with a known quality bar.

Do not force loops when you’re still discovering the goal. If the idea is unclear or evolving, if you want to brainstorm, design, or stay deep in the creative process, today’s agents as collaborators are the right tool. That is not a failure of autonomy. That is the right interaction model for discovery work.

The sharp anti-example: “Make a billion dollars. Make no mistakes.” That is motion without a stop condition. Don’t put a loop on that.

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

On the other side, this is AdaL’s view: most engineers will move to higher-leverage decision points. They get time back from babysitting intermediate steps, and they can spend more of that time deciding what to build and why — researching new opportunities, talking with users, exploring product needs, brainstorming with teammates, and taking clearer ownership of metrics and product impact.

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
