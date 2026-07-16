# slide 1: 1. the buzz of loop engineering

"instead of prompting, lets build loops that prompt it" 




# slide 2: 2. agentic engineering of today. 


## 2.1 coding agent is a model in a tool call loop.

1. it can come with simple subagent like agentic search, it is literally a tool itself

2. it builds on the concept of prompt engineering and harness engineering as the context window has increased 


As context windows grew, agent systems expanded from prompt engineering to context and harness engineering. 

prompt engineering = context engineering [anything that goes into the agent] + prompt caching. we call it context engineering as the context becomes bigger and it makes it more complicated, it includes sytem prompt, tool defintion, mcp tools, skills, conversation history, user inputs, user follow ups. tool observation, and sometimes model reasoning traces. 

and the user query can be quite complicated, @ file, added images. 

harness engineering = all the code that leads to the context change: tool call execution, skill system, compactor system, mcp system, @ , image upload, runtime environment

thats why getting an agent to work robustly and efficiently is not easy, itss a combination of understading ai system and engineering system. 



(the diagram of prompt engineering, harness engineering. )

## slide 3 2.2  The pain of the developers today



## Slide 4. 2.3 the manual outer loop 

using coding agent requires a manual outerloop to cover the the iterate dev lifecycle 

This is why everyone is saying" instead of prompting, lets build loops that prompt it" 

you see people sharing claude setups, most of them are either on skills, or part of this loops, or prompts. 


## slide 5: loop engineering

## slide 6: loops.md 

## slide 7: loops of today. 


## slide 8: adal engineer 


## slide 9: autonomy metrics. [look ahead]

How adal meausres 



# 4. What is loop engineering


context engineering = one agent + subagent (subagent is a simpel tool)

A circle. 

A dev lifecycle.  -> deliver one task/feature end to end 

Step1:
- capability.  naturally, it requires multiple models, multiple-agents.  [model + single agent harness]
- to do it better, it requires loops, of multiple iterations. [the outerloop] [agent-> subagent]


we are doing the outer loop manually. [mutiple windows, claude code, code-review agents spreading across different surfaces, locally, in the cloud, in teh github ]

- its frustrating, [use midjoury' founder' words we are exhuasted. ]

loop.md is the best content on loop engineering.

the core principle 
- goal driven 
- close the loop of self-validation [testing], this is impossible before browser use and computer use 
- multi-agents: evaluator and builder. different context, same/diff model. [code-review] - specialized prompt 


loop engineering is about automate the outerloop. 





# Look ahead, whats after the loop engineering. 

who has the most content on whats after loop engineering.


# Lets put it simply, agentic engineering is two dimension: autonomy vs model capability.


on the y, 

L1: context/harness engineering (approvals all steps).  often one agent has to sepcialize something, hard to do a whole dev-lifecycle. 

L2: 