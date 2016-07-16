#!/usr/bin/python3
"""
Project: AIDE
File: BoardEnviro.py
Author: Rafael Zamora
Version: 1.0
Date Updated: 3/24/2016

Change Log:
-ADDED Interface with AIDEGUI
"""
from PyAIDE import Enviro

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
