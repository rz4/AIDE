#!/usr/bin/python3
'''
Project: PyAIDE
File: TicTacToeEnviro.py
Author: Rafael Zamora
Version: 1.0.0
Last Update: 7/20/2016

Change Log:
'''

from PyAIDE import Enviro
from random import randint

class TicTacToeEnviro(Enviro):
    """ TicTacToeEnviro is an environment made for two agents.
        It simulates a game of tic-tac-toe with the final two percepts
        being the current turn and state of the game.
    """

    def init_enviro(self):
        self.enviro_data["Legal_Acts"] = ["TOP_LEFT", "TOP_MID", "TOP_RIGHT",
                                          "MID_LEFT", "MID_MID", "MID_RIGHT",
                                          "BOTTOM_LEFT", "BOTTOM_MID", "BOTTOM_RIGHT"]
        self.state_data["Turn"] = randint(1,2)
        self.state_data["Game"] = [0,0,0,0,0,0,0,0,0,self.state_data["Turn"],0]
        self.state_data["Solution"] = (None, None, None, None, None, None, None, None, None, None, 2)
        self.enviro_data["Tasks"].append(self.state_data["Solution"])

    def percept_to_agent(self, agent):
        percept = tuple(self.state_data["Game"])
        agent.sense(percept)

    def act_to_enviro(self, agent):
        player = 0
        if self.state_data["Turn"] == 1:
            player = 1
            self.state_data["Turn"] = 2
        elif self.state_data["Turn"] == 2:
            player = 4
            self.state_data["Turn"] = 1
        act = agent.act()
        game = self.state_data["Game"]
        legal_acts = self.enviro_data["Legal_Acts"]
        for i in range(9):
            if act == legal_acts[i]:
                if game[i] == 0 and game[10] == 0:
                    game[i] = player
        for i in range(3):
            _sums = [0,0,0,0]
            _sums[0] = sum(game[3*i:(3*i)+3])
            _sums[1] = sum(game[i:8:3])
            _sums[2] = game[0] + game[4] + game[8]
            _sums[3] = game[2] + game[4] + game[6]
            if 12 in _sums:
                game[10] = 2
            if 3 in _sums:
                game[10] = 1
        game[9] = self.state_data["Turn"]

    def render(self, canvas, state_data):
        #Render Eight Puzzle Tiles
        tsize = (canvas.winfo_width() / 3)
        for i in range(9):
            x1, y1 = (tsize/15) + (int(i%3)*tsize), (tsize/15) + (int(i/3)*tsize)
            if state_data["Game"][i] == 1:
                canvas.create_rectangle(x1, y1, x1 + (9/10)*tsize, y1 + (9/10)*tsize, fill = "red")
                canvas_id = canvas.create_text(x1 + (1/10)*tsize, y1 + (3/10)*tsize, anchor="nw")
                canvas.itemconfig(canvas_id, text="X")
                canvas.insert(canvas_id, 12, "")
            elif state_data["Game"][i] == 4:
                canvas.create_rectangle(x1, y1, x1 + (9/10)*tsize, y1 + (9/10)*tsize, fill = "green")
                canvas_id = canvas.create_text(x1 + (1/10)*tsize, y1 + (3/10)*tsize, anchor="nw")
                canvas.itemconfig(canvas_id, text="O")
                canvas.insert(canvas_id, 12, "")
            else:
                canvas.create_rectangle(x1, y1, x1 + (9/10)*tsize, y1 + (9/10)*tsize, fill = "blue")
