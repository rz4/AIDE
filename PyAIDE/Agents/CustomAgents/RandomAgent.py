#!/usr/bin/python3
'''
Project: PyAIDE
File: RandomAgent.py
Author: Rafael Zamora
Version: 1.0.0
Last Updated: 7/17/2016

Change Log:
'''
from PyAIDE import Agent
from random import seed, choice

class RandomAgent(Agent):
    """ RandomAgent is a agent which selects a random actions
    from list of legal actions. The agent will become inactive
    once any task is met.

    """

    def compute(self):
        seed()
        self.nextAct = choice(self.legalActs)
        flag = True
        for t in self.tasks:
            if self.nextPercept != t: flag = False
        if flag:
            self.active = False
            self.nextAct = None
