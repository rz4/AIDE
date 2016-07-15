#!/usr/bin/python3
"""
Project: AIDE
File: Agent.py
Author: Rafael Zamora
Version: 0.01
Date Updated: 3/10/2016
"""
from abc import ABCMeta, abstractmethod

class Agent:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.legalActs = None
        self.tasks = None
        self.nextAct = None
        self.nextPercept = None
        self.active = False

    def init_Agent(self):
        self.nextAct = None
        self.nextPercept = None
        self.active = True

    def setLegalActs(self, acts):
        self.legalActs = acts

    def setTasks(self, tasks):
        self.tasks = tasks

    def sense(self, percept):
        self.nextPercept = percept

    def act(self):
        return self.nextAct

    @abstractmethod
    def compute(self):
        pass
