#!/usr/bin/python3
'''
Project: PyAIDE
File: BoardEnviro.py
Author: Rafael Zamora
Version: 1.0.0
Last Update: 7/17/2016

Change Log:
-ADDED set parameter functions v1.0.0
'''

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

    def __init_enviro(self):
        self.enviro_data["Legal_Acts"] = ["LEFT", "RIGHT", "UP", "DOWN"]
        self.state_data["Width"] = self.width
        self.state_data["Height"] = self.length
        self.state_data["InitPos"] = self.init_pos
        self.state_data["FinalPos"] = self.final_pos
        self.state_data["AgentsPos"] = {}
        for a in self.enviro_data["Agents"]:
            self.state_data["AgentsPos"][a.__class__.__name__] = list(self.state_data["InitPos"])
        self.enviro_data["Tasks"].append(self.state_data["FinalPos"])

    def __percept_to_agent(self, agent):
        percept = tuple(self.state_data["AgentsPos"][agent.__class__.__name__])
        agent.sense(percept)

    def __act_to_enviro(self, agent):
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

    def render(self, canvas, state):
        #Render Board Tiles
        tsize = (canvas.winfo_width() / state["Width"]) - 0.02
        for x in range(state["Width"]):
            for y in range(state["Height"]):
                x1, y1 = tsize/10 + (x*tsize), tsize/10 + (y*tsize)
                canvas.create_rectangle(x1, y1, x1 + (9/10)*tsize, y1 + (9/10)*tsize, fill = "blue")

        #Render Final Position Tile
        x1, y1 = tsize/10 + (state["FinalPos"][0]*tsize) , tsize/10 +(state["FinalPos"][1]*tsize)
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
