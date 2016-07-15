![AIDE Logo](images/AIDE_logo.png)
# PyAIDE - Python A.I. Development Environment
Version 0.9.1

Last Updated: **July 15, 2016**

Lead Maintainer: [Rafael Zamora](https://github.com/rz4)

**PyAIDE** is a Python (3.5) library for the development and testing of
intelligent agents. It is used to create and interface custom
agents and environments. It also contains tools for running
simulations and gathering result data.

### Overview

Typical use involves defining the decision behavior of **Agents**
based on the input information provided by **Environments**. In
addition, new **Environments** can be defined in order to test the
decision behavior of **Agents**.

**Agents** can be implemented by extending the `Agent` class.
**Agents** will be provided with the following information:
- A list of legal *Actions* for the **Environment**.
- A list of *Goals* for the **Environment**.
- *Percepts* passed from the **Environment** each update cycle.

Using this input information, the **Agents** should decide what
*Action* from the list of legal *Actions* to take.

**Environments** can be implemented by extending the `Enviro`
class. **Environments** will have the following functions in relation
to **Agents**:
- Pass current information of the environment to the **Agents** each
update cycle.
- Update environment according to *Actions* passed from **Agents**.

These functions will need to be defined in addition to defining a list
of legal *Actions* and a list of *Goals*.

**AIDE**'s goal is to create a simple framework for defining **Agent**
and **Environment** behavior and relations.

## Code Example
### Agents
The following is code used to define a **Random Agent**:

```python
from PyAide import Agent
from random import seed, choice

class RandomAgent(Agent):

    def compute(self):
        seed()
        self.nextAct = choice(self.legalActs)
        flag = True
        for t in self.tasks:
            if self.nextPercept != t: flag = False
        if flag:
            self.active = False
            self.nextAct = None
```
All agent behavior should be defined in the `compute()` method.
This method will be called during the simulation, after the
environment has passed `nextPercept` to the agent and before the
environment updates using the agent's`nextAct`.

In this code example, the **Random Agent** selects a random
action from `legalActs`. The environment will continue to
update the agent as long as the agent is active.
The `flag` is used to check the goals against
the percepts, setting it inactive if any have been met.
If any goal is met, the agent will be set inactive.
### Environments
The following code is used to define a **Board Environment**:

```python
class BoardEnviro(Enviro):

    def initEnviro(self):
        self.legalActs = ["LEFT", "RIGHT", "UP", "DOWN"]
        self.state["Width"] = 25
        self.state["Height"] = 25
        self.state["InitPos"] = (0,0)
        self.state["FinalPos"] = (24,24)
        self.state["AgentsPos"] = {}
        for a in self.agents: self.state["AgentsPos"][a.__class__.__name__] = list(self.state["InitPos"])
        self.tasks.append(self.state["FinalPos"])

    def percept_to_Agent(self, agent):
        percept = tuple(self.state["AgentsPos"][agent.__class__.__name__])
        agent.sense(percept)

    def act_to_Enviro(self, agent):
        act = agent.act()
        agentPos = self.state["AgentsPos"][agent.__class__.__name__]
        if act == self.legalActs[0]:#LEFT
            if agentPos[0] > 0:
                agentPos[0] -= 1
        elif act == self.legalActs[1]:#RIGHT
            if agentPos[0] < self.state["Width"]-1:
                agentPos[0] += 1
        elif act == self.legalActs[2]:#UP
            if agentPos[1] > 0:
                agentPos[1] -= 1
        elif act == self.legalActs[3]:#DOWN
            if agentPos[1] < self.state["Height"]-1:
                agentPos[1] += 1

    def render(self, gui, state):
        tsize = (gui.screen.get_height() / state["Width"]) - 0.02
        for x in range(state["Width"]):
            for y in range(state["Height"]):
                rect = gui.pygame.Rect(tsize/10 + (x*tsize) , tsize/10 +(y*tsize), (9/10)*tsize, (9/10)*tsize)
                gui.pygame.draw.rect(gui.screen, (0, 200, 255), rect)
        rect = gui.pygame.Rect(tsize/10 + (state["FinalPos"][0]*tsize) , tsize/10 +(state["FinalPos"][1]*tsize), (9/10)*tsize, (9/10)*tsize)
        gui.pygame.draw.rect(gui.screen, (255, 0, 0), rect)
        gui.drawString("Initial Position: " + str(state["InitPos"]),602,194)
        gui.drawString("Final Position: " + str(state["FinalPos"]),602,212)
        gui.drawString("Agent Positions:",602,230)
        i = 0
        for a in state["AgentsPos"]:
            agentPos = state["AgentsPos"][a]
            rect = gui.pygame.Rect(tsize/10 + (agentPos[1]*tsize) , tsize/10 +(agentPos[0]*tsize), (9/10)*tsize, (9/10)*tsize)
            gui.pygame.draw.rect(gui.screen, (0, 0, 255), rect)
            gui.drawString(a,rect.centerx,rect.centery,centered = True)
            gui.drawString(a + " at " + str(state["AgentsPos"][a]),612,248 + 18*i)
            i += 1

    def writeState(self, state):
        str_ = "Width > " + str(state["Width"]) + " | "
        str_ += "Height > " + str(state["Height"]) + " | "
        str_ += "InitPos > " + str(state["InitPos"][0]) + " , " + str(state["InitPos"][1]) + " | "
        str_ += "FinalPos > " + str(state["FinalPos"][0]) + " , " + str(state["FinalPos"][1]) + " | "
        str_ += "AgentsPos > "
        for a in state["AgentsPos"]:
            str_ += a + " < " + str(state["AgentsPos"][a][0]) + " , " + str(state["AgentsPos"][a][1]) + " < "
        return str_[0:-3]

    def readState(self, str_):
        state = {}
        data = str_.split(" | ")
        var = data[0].split(" > ")
        state[var[0]] = int(var[1])
        var = data[1].split(" > ")
        state[var[0]] = int(var[1])
        var = data[2].split(" > ")
        varr = var[1].split(" , ")
        state[var[0]] = (int(varr[0]),int(varr[1]))
        var = data[3].split(" > ")
        varr = var[1].split(" , ")
        state[var[0]] = (int(varr[0]),int(varr[1]))
        var = data[4].split(" > ")
        state[var[0]] = {}
        varr = var[1].split(" < ")
        for i in range(int(len(varr)/2)):
            varrr = varr[i*2+1].split(" , ")
            state[var[0]][varr[i*2]] = [int(varrr[0]),int(varrr[1])]
        return state
```

### Running a Simulation
The following code is used to define a **Test Simulation** for
a **Random Agent** interfaced with a **Board
Environment**:
```python
from PyAide import BoardEnviro
from PyAide import RandomAgent

agent = RandomAgent()

enviro = BoardEnviro()
enviro.addAgent(agent)
enviro.runEnviro(filename = "data.txt",updates = 5000, verbose = True)
```
In this code example, a new **Board Environment** object is created, and a new
**Random Agent** is added through the `addAgent()` method. A
The **Board Environment** is run using the `runEnviro()` method with
the output filename for the result data, the number of times the environment
will be simulated as the parameters, and whether to print state to console as
parameters.

## Motivation

This project is designed with the intention of rapid prototyping
agents and environments for A.I. research. The project will be
used to facilitate Artificial General Intelligence research by
creating a simple framework for agents to be tested in multiple
unique and unknown environments.

## Installation

**PyAIDE**'s gui playback feature requires **PyGame** to run.

The following ***Pip*** command can be used to install **PyAIDE**:
```
pip install git+https://github.com/rz4/PyyAIDE
```

## License

This project is licensed under the [GNU General Public License](LICENSE).
