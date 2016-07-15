#!/usr/bin/python3
"""
Project: AIDE
File: Agent.py
Author: Rafael Zamora
Version: 0.01
Date Updated: 3/10/2016
"""
from PyAide.Agents.Agent import Agent
from random import seed, choice

class RandomAgent(Agent):

    def compute(self):
        seed()
        self.nextAct = choice(self.legalActs)
        flag = True
        for t in self.tasks:
            if self.nextPercept != t: flag = False
        if flag:
            self.active = False
            self.nextAct = None
