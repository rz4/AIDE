#!/usr/bin/python3
'''
Project: PyAIDE
File: Agent.py
Author: Rafael Zamora
Version: 1.0.0
Last Update: 7/17/2016

Change Log:
-ADDED documentation v1.0.0
'''
from abc import ABCMeta, abstractmethod

class Agent:
    """ Agent is an abstract class used to define intelligent agents.

    The PyAIDE agent-enviro update cycle consists of the following
    functions in order:
    * Enviro's percept_to_Agent() function - Builds percept tuple
    * Agent's sense() function - Passes percept tuple to agent
    * Agent's compute() function - Agent behavior
    * Agent's act() function - Passes action to enviro
    * Enviros's act_to_Enviro() function - Updates enviro with action

    The compute() function should be used to define agent behavior.
    The following variables can be used to define agent behavior:
    * legalActs - list of legal actions available in the environment
    * tasks - list of percept tuples which are goal percepts
    * nextAct - action which will be passed to environment
    * nextPercept - percept tuple which is passed from environment
    * active - determines whether agent is active in environment

    """

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
