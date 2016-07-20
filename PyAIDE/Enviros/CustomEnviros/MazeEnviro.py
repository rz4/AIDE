#!/usr/bin/python3
'''
Project: PyAIDE
File: MazeEnviro.py
Author: Rafael Zamora
Version: 1.0.0
Last Update: 7/17/2016

Change Log:
-ADDED set parameter functions v1.0.0
'''

from PyAIDE import Enviro
from random import seed, random, randint

class MazeEnviro(Enviro):

    """MazeEnviro is an environment made for multiple agents
    The only agent task is to reach the lower left tile of the maze.
    The agent is to do this using the up, down, left, and right actions.

    Mazes are to be loaded through the setMazeFile() function.
    A Maze file must be set before running.

    The following functions can be used to set parameters of the environment:
    * setInitialPos(x, y) - sets initial position of agents
    * setFinalPos(x, y) - sets final position of agents
    """

    def __init__(self):
        super().__init__()
        self.init_pos = (0,0)
        self.final_pos = None

    def init_enviro(self):
        self.enviro_data["Legal_Acts"] = ["LEFT", "RIGHT", "UP", "DOWN"]
        self.state_data["Maze"] = self.__load_maze()
        self.state_data["Width"] = len(self.state_data["Maze"])
        self.state_data["Height"] = len(self.state_data["Maze"][0])
        self.state_data["InitPos"] = self.init_pos
        if self.final_pos: self.state_data["FinalPos"] = self.final_pos
        else: self.state_data["FinalPos"] = (self.state_data["Width"]-1, self.state_data["Height"]-1)
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
        old_pos = list(agent_pos)
        legal_acts = self.enviro_data["Legal_Acts"]
        if act == legal_acts[0]: #LEFT
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
        if self.state_data["Maze"][agent_pos[0]][agent_pos[1]] == 1:
            agent_pos[0] = old_pos[0]
            agent_pos[1] = old_pos[1]

    def render(self, canvas, state_data):
        #Render Maze Tiles
        maze = state_data["Maze"]
        tsize = (canvas.winfo_width() / state_data["Width"]) - 0.02
        for x in range(len(maze)):
            for y in range(len(maze[x])):
                if maze[x][y] == 0:
                    x1, y1 = tsize/10 + (x*tsize), tsize/10 + (y*tsize)
                    canvas.create_rectangle(x1, y1, x1 + (9/10)*tsize, y1 + (9/10)*tsize, fill = "blue")

        #Render Final Position Tile
        x1, y1 = tsize/10 + (state_data["FinalPos"][0]*tsize) , tsize/10 +(state_data["FinalPos"][1]*tsize)
        canvas.create_rectangle(x1, y1, x1 + (9/10)*tsize, y1 + (9/10)*tsize, fill = "green")

        #Render Agent Position Tile
        for a in state_data["AgentsPos"]:
            agent_pos = state_data["AgentsPos"][a]
            y1, x1 = tsize/10 + (agent_pos[1]*tsize) , tsize/10 +(agent_pos[0]*tsize)
            canvas.create_rectangle(x1, y1, x1 + (9/10)*tsize, y1 + (9/10)*tsize, fill = "red")
            canvas_id = canvas.create_text(x1 + (1/10)*tsize, y1 + (3/10)*tsize, anchor="nw")
            canvas.itemconfig(canvas_id, text=a)
            canvas.insert(canvas_id, 12, "")

    def set_maze_file(self, filename):
        self.maze_filename = filename

    def __load_maze(self):
        maze_file = open(self.maze_filename, "r")
        maze = []
        for maze_str in maze_file:
            m = [int(s) for s in maze_str.split(",")]
            maze.append(m)
        return maze

    def set_initial_pos(self, x, y):
        self.init_pos = (x,y)

    def set_final_pos(self, x, y):
        self.final_pos = (x,y)
