#!/usr/bin/python3
'''
Project: PyAIDE
File: HumanAgent.py
Author: Rafael Zamora
Version: 1.0.0
Last Updated: 7/20/2016

Change Log:
'''

from PyAIDE import Agent

class HumanAgent(Agent):
    """ HumanAgent is an agent which allows a human user
    to initerface with PyAIDE Environments.

    """

    def compute(self):
        print("Current Percept: " + str(self.next_percept))
        print("Current Tasks: " + str(self.tasks))
        print("Enter Digit for Action:")
        print("0 SET INACTIVE")
        for i in range(len(self.legal_acts)):
                print(str(i+1) + " " + str(self.legal_acts[i]))
        sel = input("\n")

        try:
            sel = int(sel)
            if sel == 0:
                self.active = False
            elif sel < len(self.legal_acts)+1:
                self.next_act = self.legal_acts[sel-1]
            else:
                self.next_act = None
        except:
            self.next_act = None
