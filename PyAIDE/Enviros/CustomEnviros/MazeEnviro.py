#!/usr/bin/python3
"""
Project: PyAIDE
File: MazeEnviro.py
Author: Rafael Zamora
Version: 1.0.0
Date Updated: 7/16/2016

Change Log:
-ADDED Load maze from file functions.
-ADDED Description of class.
-UPDATED Interface with AIDEGUI
-REMOVED Random Generation
"""
from PyAIDE import Enviro
from random import seed, random, randint

'''
MazeEnviro is an environment made for one agent.
The only agent task is to reach the lower left tile of the maze.
The agent is to do this using the up, down, left, and right actions.

Mazes are to be loaded through the setMazeFile() function.
A Maze file must be set before running.

Note: The current task is hardcoded at (width-1, height-1) coordinates.
      This can be changes by changing self.state["FinalPos"].
'''
class MazeEnviro(Enviro):

    def initEnviro(self):
        self.legalActs = ["LEFT", "RIGHT", "UP", "DOWN"]
        self.state["Maze"] = self.__load_maze()
        self.state["Width"] = len(self.state["Maze"])
        self.state["Height"] = len(self.state["Maze"][0])
        self.state["InitPos"] = (0,0)
        self.state["FinalPos"] = (self.state["Width"]-1,self.state["Height"]-1)
        self.state["AgentsPos"] = {}
        for a in self.agents: self.state["AgentsPos"][a.__class__.__name__] = list(self.state["InitPos"])
        self.tasks.append(self.state["FinalPos"])

    def percept_to_Agent(self, agent):
        percept = tuple(self.state["AgentsPos"][agent.__class__.__name__])
        agent.sense(percept)

    def act_to_Enviro(self, agent):
        act = agent.act()
        agentPos = self.state["AgentsPos"][agent.__class__.__name__]
        oldPos = list(agentPos)
        if act == self.legalActs[0]: #LEFT
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
        if self.state["Maze"][agentPos[0]][agentPos[1]] == 1:
            agentPos[0] = oldPos[0]
            agentPos[1] = oldPos[1]

    def render(self, gui, state):
        maze = state["Maze"]
        tsize = (gui.screen.get_height() / state["Width"]) - 0.02
        for x in range(len(maze)):
            for y in range(len(maze[x])):
                if maze[x][y] == 0:
                    rect = gui.pygame.Rect(tsize/10 + (y*tsize) , tsize/10 +(x*tsize), (9/10)*tsize, (9/10)*tsize)
                    gui.pygame.draw.rect(gui.screen, (0, 200, 255), rect)
        rect = gui.pygame.Rect(tsize/10 + (state["FinalPos"][1]*tsize) , tsize/10 +(state["FinalPos"][0]*tsize), (9/10)*tsize, (9/10)*tsize)
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
        str_ += " | Maze > " + self.maze_filename
        return str_

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
        var = data[5].split(" > ")
        self.maze_filename = var[1]
        state[var[0]] = self.__load_maze()
        return state

    def setMazeFile(self, filename):
        self.maze_filename = filename

    def __load_maze(self):
        maze_file = open(self.maze_filename, "r")
        maze = []
        for maze_str in maze_file:
            m = [int(s) for s in maze_str.split(",")]
            maze.append(m)
        return maze
