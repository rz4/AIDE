#!/usr/bin/python3
'''
Project: PyAIDE
File: EightPuzzleEnviro.py
Author: Rafael Zamora
Version: 1.0.0
Last Update: 7/17/2016

Change Log:
'''

from PyAIDE import Enviro
from random import shuffle

class EightPuzzleEnviro(Enviro):
    """
    EightPuzzleEnviro is an environment made for one agent.
    The only agent task is to rearrange the puzzle to the solution order.
    The agent is to do this using the push-up, push-down, push-left, and push-right actions.

    """
    def initEnviro(self):
        self.legalActs = ["PUSHLEFT", "PUSHRIGHT", "PUSHUP", "PUSHDOWN"]
        self.state["Player"] = self.agents[0].__class__.__name__
        self.state["Puzzle"] = [i for i in range(9)]
        shuffle(self.state["Puzzle"])
        self.state["Solution"] = (0,1,2,3,4,5,6,7,8)
        self.tasks.append(self.state["Solution"])

    def percept_to_Agent(self, agent):
        percept = tuple(self.state["Puzzle"])
        agent.sense(percept)

    def act_to_Enviro(self, agent):
        if self.state["Player"] != agent.__class__.__name__: return
        act = agent.act()
        puzzle = self.state["Puzzle"]
        i = puzzle.index(0)
        temp = i
        if act == self.legalActs[0]:#LEFT
            if i % 3 != 2:
                i += 1
        elif act == self.legalActs[1]:#RIGHT
            if i % 3 != 0:
                i -= 1
        elif act == self.legalActs[2]:#UP
            if i / 3 < 2:
                i += 3
        elif act == self.legalActs[3]:#DOWN
            if i / 3 > 1:
                i -= 3
        puzzle[temp] = puzzle[i]
        puzzle[i] = 0

    def render(self, canvas, state):
        tsize = (canvas.winfo_width() / 3)
        for i in range(9):
            if state["Puzzle"][i] != 0:
                x1, y1 = (tsize/15) + (int(i%3)*tsize), (tsize/15) + (int(i/3)*tsize)
                canvas.create_rectangle(x1, y1, x1 + (9/10)*tsize, y1 + (9/10)*tsize, fill = "blue")
                canvas_id = canvas.create_text(x1 + (1/10)*tsize, y1 + (3/10)*tsize, anchor="nw")
                canvas.itemconfig(canvas_id, text=str(state["Puzzle"][i]))
                canvas.insert(canvas_id, 12, "")
