#!/usr/bin/python3
"""
Project: AIDE
File: Enviro.py
Author: Rafael Zamora
Version: 1.0
Date Updated: 6/20/2016
"""
from PyAide.Enviros.Enviro import Enviro
from random import shuffle

class EightPuzzleEnviro(Enviro):

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
        print(act)
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

    def render(self, gui, state):
        tsize = (gui.screen.get_height() / 3)
        for i in range(9):
            if state["Puzzle"][i] != 0:
                rect = gui.pygame.Rect((tsize/15) + (int(i%3)*tsize) , (tsize/15) + (int(i/3)*tsize), (9/10)*tsize, (9/10)*tsize)
                gui.pygame.draw.rect(gui.screen, (0, 200, 255), rect)
                gui.drawString(str(state["Puzzle"][i]),rect.centerx,rect.centery,centered = True)
        gui.drawString("Player: " + str(state["Player"]),602,194)
        gui.drawString("Puzzle: " + str(state["Puzzle"]),602,212)
        gui.drawString("Solution: " + str(state["Solution"]),602,230)

    def writeState(self, state):
        str_ = "Player > " + str(state["Player"]) + " | "
        str_ += "Puzzle > "
        for p in state["Puzzle"]:
            str_ += str(p) + " , "
        str_ = str_[0:-3] + " | Solution > "
        for s in state["Solution"]:
            str_ += str(s) + " , "
        return str_[0:-3]

    def readState(self, str_):
        state = {}
        data = str_.split(" | ")
        var = data[0].split(" > ")
        state[var[0]] = var[1]
        var = data[1].split(" > ")
        varr = var[1].split(" , ")
        state[var[0]] = [int(v) for v in varr]
        var = data[2].split(" > ")
        varr = var[1].split(" , ")
        state[var[0]] = tuple(int(v) for v in varr)
        return state
