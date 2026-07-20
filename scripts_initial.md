/title: Beyond Loop Engineering

Hi everyone, I’m Li Yin, co-founder and CEO of SylphAI and creator of AdalFlow.

I’m a PhD dropout. I did AI research at Meta and spent about three years building LLM harnesses—including AdalFlow, an open-source library for building and auto-optimizing LLM applications.

At SylphAI, we have been exploring autonomy through agents and memory. This is still a new field: no one has all the answers, and that is why I want to use this session to think with people building in the field and discuss the problems honestly.

/title: More Productive. More Drained.

If models are already so good at coding, why are we still babysitting our coding agents 12 hours a day?

You say, “Please fix A,” and it fixes A—but also changes B. Or it solves the problem in a way that is inconsistent with the rest of your codebase. Or it gets halfway through the task and needs you to take over.

So the experience is strange: these systems can feel extremely intelligent at generating code, but surprisingly limited at autonomy. The answer lies in the system around the model—and potentially beyond it.



Writing alien code. 

Hook:

models are really good, right? Better code than human, but we're still babysitting them. 12 hours a day and we feel it's smart in model capability and writing the code, but it's stupid when it comes to autonomy. So you keep repeating the same context, and you keep getting frustrated, uh, to not do what they want. They change when you ask, hey, they might do A, but they also change B, or they might do it in a way that's not consistent with your code base .

In this session, I'm honored to sit down to go through everything on loop engineering. Akshay wrote amazing content on this topic in June. one of the earliest articles. I'm pretty sure, we all have a lot of questions. What exactly is loop engineering? Will loop engineering be the answer to the issues I'm having with coding agents or any agent? If so, how can I use it, and when should I use it? I’ll try my best to answer that. And even explore what's next in autonomy after the loop engineering. 


Agents: 

Before diving into it, before loop engineering, we already have agents since 2022 on GPT-3 at a paper called React. Even before ChatGPT. 

React represents reasoning and acting, it runs on a loop of call tools and getting the observation, and then taking the next actions.  3 years ago, agents just did 2-3 steps.  As the context increases and the ability to call functions in json/xml format typically, with constrained decoding, it can
Now agents can run hundreds of steps in one turn to solve very complicated tasks.  (2) it can also do complicated parallel tool calls and can learn how to use hundreds of tools at once.  
The most powerful example is coding agents. 

And if we have to think about sub agents, it's simply another cool tool. 


Prompts to harness: 

Harness is the code that takes a model and makes it into an agent system. The original react papers source code is the first harness. Which represents more about the riginal harness. 

And claude code source code is a harness, opencode is harness and our adal codebase is the harness. 

The complexity goes up because the context window has gone from 10k, 28k, 100k, 200k, all the way to 1m.  In the first harness codebase, the most important part is prompt, as it does not support any tool, like mcp. Skills, subagents or customized tools, so everything is just programmed for one use case.  

As the context window goes up, the more we have to structure.  We are fitting a long chat history, with the context structure becoming way more complicated, and longer, we need dedicated engineering for it, called context engineering, to manage the context structure the model sees. 

Prompt caching is important, to save cost.  All these are making the agents of today's codebase complicated. To deal with long-running tasks, we need compaction too. When context is too long, we have pros and cons, it experiences context-rot, it does tasks with less performance. And the following structure is worse. 

Agentic engineering of today: more productive more drained. 

Software engineers have all been using coding agents. We can't live without it. We do feel like 10x more productive, but at the same time, we feel we are 10x more drained. 

Why?  We are stuck baby sitting agents/ 

The manual outer loop  and multi-tasking
Even though Agents can technically complete a task end to end all by itself without u in the loop but u dont feel comfortable and instead u babysite. , you need to approve each action, for reasons, like 
It has no big picture of our codebase like human engineers do. There are 10 ways to build any thing, but there is a particular way ur codebase need based on the design 
It can be risky. What if it deletes all the code, what if it leaks my keys. 
If it goes wrong, it can waste tokens. 

Now engineers do multi-tasking, and are required to constantly switch between different coding agents tabs, it's common when u hear people ask “how many sessions, whats ur number” at a SF party. 

One task to go to pr, requires multiple stages. And different stages need different agent capabilities across local, cloud, and GitHub environments, forcing developers to manually run the iterative dev loop.

As time goes, all the pride becomes emotionally drained and burned out. Agents are hard to control. You repeat the same context, ask it to do a, it does b, as it to only change a, it changes b and c. and also now we have to make 10x more hard decisions on each problem. 

Agents can run 24X7, even endless sessions, but human times are bounded. 

Slide 6: loop engineering

The simple definition: instead of prompting, lets build loops that prompt it, can it free us from babysitting? 

I think a better definition, which is more aligned with Andrew Ng, Andrej karpathy, and me. Can we just give it a task, one query, and it can ship a pr till green, till production autonomously? To be more accurate, can we complete a full dev life cycle autonomously? 

Instead of just a loop to create a pr non-stop, can we really automate the output loop of the iterative life dev cycle?  We had created autopilot with AdaL 5 months ago, you can just label an issue with auto-pilot, it will create a pr, but we never really used it.  Because of the reasons that made us babysit at the first place. 

Until today, we are gonna try that again.


Slide 7: what makes loops possible  ->


Explain context rot: the performance cna degrad, stop follwng hte format, or do tasks with less accuracy, or forget context. Or nto honest or get too optimistic of its work. 

Context rot is the progressive degradation of an agent’s ability to retrieve relevant information, maintain a coherent task state, and make correct decisions as its active context accumulates over a long-running trajectory.

We  start to understand the context rot better and start the multi-agent, and each is responsible for a stage of the tasks, like code review, coding, brower use,  and sometimes even parallel agents, two builders. 


This gives us the infra to close the loop of dev lifecycle. 



Slide 8: Loops of today. 

We have all the primitives and building blocks

The good news is that many of the primitives already exist.  
We can run repeated work through loops and scheduled jobs. We can use permission modes for more autonomous execution. Agents can adapt workflows as they run. And agent teams let us parallelize work.  
So the problem is no longer that models cannot write code or use tools.  
The problem is how to turn these individual building blocks into a reliable system that can keep working, validating itself, recovering, and eventually shipping.




Slide 9: what makes loop engineering in accessible


Even if we have all the primitives and building blocks. It took a whole codex team to achieve a software product with  0 lines of manually written code . 


But it took a whole engineering team to build and maintain the harness: 

The loop:  how many workers to spawn, how they communicate, when they hand work off, how they evaluate one another, how they recover from failures, and when to stop the loop. How to manage the states, what model to use, what agent capabilities. 
The context: documentation, when to fit in the right context automatically
Still human code-review.  

That is the important lesson. The hard part is not only the coding agent. The hard part is the system around the coding agent.  

It is high complexity: you must coordinate context, tasks, tools, validation, recovery, and review.  
And it is high cost: more agents, more context, more validation, and repeated iterations all compound runtime cost.


Slide 9: the real challenges of loop engineering

How can we replicate the current human engineer? Their high-level, and long-term understanding of the codebase, architecture, the prompt they sent to babysit the code agents that eventually made pr into production.  Their judgement on the architecture design, coding style 

Slide 8: AdaL engineers:

Our mission is to make that harness accessible—by replicating what a human engineer does around today’s coding agents. 
It allocates, prompts, and monitors coding agents for you to deliver secure, autonomous, and high-quality results. 

Allocates, prompts, monitors, fetches the right context at the right time, maintains documentation, and has a long-term persist worklog. 


Slide 9:  Inside AdaL Engineer: Runs the iterative full dev lifecycle



Slide 9: when we need loop engineering and when not. 

Slide 10: what would humans do if work is automated?








When to do loop engineering and when not to? 
One overall principle. 
Good example. 
Bad example 
Make 1billon, make no mistake.  -> best example not use loop engineering  


Autonomy - the point of achievement? 
Everyone can think what to build next in different ways. 
U can do more interesting work? 
Or ta
Together, we can delegate the idea to the agents e
