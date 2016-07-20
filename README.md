![AIDE Logo](images/AIDE_logo.png)
# PyAIDE - Python A.I. Development Environment
![Current Version](https://img.shields.io/badge/version-1.0.0-green.svg)

Last Updated: **July 20, 2016**

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

**Agents** can be implemented by importing and extending the `Agent` class.
**Agents** will be provided with the following information:
- A list of legal *Actions* for the **Environment**.
- A list of *Tasks* for the **Environment**.
- *Percepts* passed from the **Environment** each update cycle.

Using this input information, the **Agents** should decide what
*Action* from the list of legal *Actions* to take.

**Environments** can be implemented by importing and extending the `Enviro`
class. **Environments** will have the following functions in relation
to **Agents**:
- Pass current information of the environment to the **Agents** each
update cycle in the form of a *Percept* tuple.
- Update environment according to *Action* passed from **Agents**.

These functions will need to be defined in addition to defining a list
of legal *Actions* and a list of *Tasks*.

**AIDE**'s goal is to create a simple framework for defining **Agent**
and **Environment** behavior and relations.

## Code Example
### Agents
The following is code used to define a **Random Agent**:

*RandomAgent.py*
```python
from PyAIDE import Agent
from random import seed, choice

class RandomAgent(Agent):

    def compute(self):
        seed()
        self.next_act = choice(self.legal_acts)
        flag = True
        for t in self.tasks:
            if self.next_percept != t: flag = False
        if flag:
            self.active = False
            self.next_act = None
```
All agent behavior should be defined in the `compute()` method.
This method will be called during the simulation, after the
environment has passed `nextPercept` to the agent and before the
environment updates using the agent's`nextAct`.

In this code example, the **Random Agent** selects a random
action from `legalActs`. The environment will continue to
update the agent as long as the agent is active.
The `flag` is used to check the tasks against
the percepts. If any goal is met, the agent will be set inactive.
### Environments
The following code is used to define a **Board Environment**:

*BoardEnviro.py*
```python
from PyAIDE import Enviro

class BoardEnviro(Enviro):
    """ BoardEnviro is an environment made for multiple agents.
    The only agent task is to reach the FinalPos.
    The agent is to do this using the up, down, left, and right actions.

    The following functions can be used to set parameters of the environment:
    * setBoardSize(length, width) - sets dimensions of board
    * setInitialPos(x, y) - sets initial position of agents
    * setFinalPos(x, y) - sets final position of agents

    """

    def __init__(self):
        super().__init__()
        self.width = 25
        self.length = 25
        self.init_pos = (0,0)
        self.final_pos = (self.width-1, self.length-1)

    def init_enviro(self):
        self.enviro_data["Legal_Acts"] = ["LEFT", "RIGHT", "UP", "DOWN"]
        self.state_data["Width"] = self.width
        self.state_data["Height"] = self.length
        self.state_data["InitPos"] = self.init_pos
        self.state_data["FinalPos"] = self.final_pos
        self.state_data["AgentsPos"] = {}
        for a in self.enviro_data["Agents"]:
            self.state_data["AgentsPos"][a.__class__.__name__] = list(self.state_data["InitPos"])
        self.enviro_data["Tasks"].append(self.state_data["FinalPos"])

    def percept_to_agent(self, agent):
        percept = tuple(self.state_data["AgentsPos"][agent.__class__.__name__])
        agent.sense(percept)

    def act_to_enviro(self, agent):
        act = agent.act()
        agent_pos = self.state_data["AgentsPos"][agent.__class__.__name__]
        legal_acts = self.enviro_data["Legal_Acts"]
        if act == legal_acts[0]:#LEFT
            if agent_pos[0] > 0:
                agent_pos[0] -= 1
        elif act == legal_acts[1]:#RIGHT
            if agent_pos[0] < self.state_data["Width"]-1:
                agent_pos[0] += 1
        elif act == legal_acts[2]:#UP
            if agent_pos[1] > 0:
                agent_pos[1] -= 1
        elif act == legal_acts[3]:#DOWN
            if agent_pos[1] < self.state_data["Height"]-1:
                agent_pos[1] += 1

    def render(self, canvas, state_data):
        #Render Board Tiles
        tsize = (canvas.winfo_width() / state_data["Width"]) - 0.02
        for x in range(state_data["Width"]):
            for y in range(state_data["Height"]):
                x1, y1 = tsize/10 + (x*tsize), tsize/10 + (y*tsize)
                canvas.create_rectangle(x1, y1, x1 + (9/10)*tsize, y1 + (9/10)*tsize, fill = "blue")

        #Render Final Position Tile
        x1, y1 = tsize/10 + (state_data["FinalPos"][0]*tsize) , tsize/10 +(state_data["FinalPos"][1]*tsize)
        canvas.create_rectangle(x1, y1, x1 + (9/10)*tsize, y1 + (9/10)*tsize, fill = "green")

        #Render Agent Position Tile
        for a in state_data["AgentsPos"]:
            agent_pos = state_data["AgentsPos"][a]
            x1, y1 = tsize/10 + (agent_pos[1]*tsize) , tsize/10 +(agent_pos[0]*tsize)
            canvas.create_rectangle(x1, y1, x1 + (9/10)*tsize, y1 + (9/10)*tsize, fill = "red")
            canvas_id = canvas.create_text(x1 + (1/10)*tsize, y1 + (3/10)*tsize, anchor="nw")
            canvas.itemconfig(canvas_id, text=a)
            canvas.insert(canvas_id, 12, "")

    def set_board_dimen(self, length, width):
        self.length = length
        self.width = width

    def set_initial_pos(self, x, y):
        self.init_pos = (x,y)

    def set_final_pos(self, x, y):
        self.final_pos = (x,y)
```

### Running a Simulation
The following code is used to define a **Test Simulation** for
a **Random Agent** interfaced with a **Board
Environment**:

*example.py*
```python
from PyAIDE import BoardEnviro
from PyAIDE import RandomAgent

agent = RandomAgent()

enviro = BoardEnviro()
enviro.add_agent(agent)
enviro.run_enviro(filename = "data.txt",updates = 5000, verbose = True)
```
In this code example, a new **Board Environment** object is created, and a new
**Random Agent** is added through the `addAgent()` method. A
The **Board Environment** is run using the `runEnviro()` method with
the output filename for the result data, the number of times the environment
will be simulated as the parameters, and whether to print state to console as
parameters.

## Features

### Current: ver. 1.0.0
- Create custom Environments.
- Create custom Agents.
- Four Environments implemented: BoardEnviro, MazeEnviro, EightPuzzleEnviro, TicTacToeEnviro
- Random Agent implemented.
- Human Agent implemented.
- AIDE GUI simulation playback.

### Future:
- Simulation result analysis tools.
- Custom batch simulation runner.
- Foreign Agent/Environment interfaces.
- Shell for testing.

## Motivation

This project is designed with the intention of rapid prototyping
agents and environments for A.I. research. The project will be
used to facilitate Artificial General Intelligence research by
creating a simple framework for agents to be tested in multiple
unique and unknown environments.

## Installation and Dependencies

### Dependencies:

Requires Python 3.5.

### Installation:

The following ***Pip*** command can be used to install **PyAIDE**:
```
pip install git+https://github.com/rz4/PyAIDE
```

## TO-DO

## License

This project is licensed under the [GNU General Public License](LICENSE).
