#!/usr/bin/python3
"""
Project: AIDE
File: Enviro.py
Author: Rafael Zamora
Version: 1.55
Date Updated: 6/18/2016

Change Log:
-FIXED Save State Bug
-ADDED EnviroData Class imbedded to Enviro
-ADDED Logging Capabilities for GUI Replay
"""

from abc import ABCMeta, abstractmethod
from copy import deepcopy

'''
$Design Concepts$
Properties of Enviros:
-Discrete/Continuous
-Observable/Partially Observable
-Static/Dynamic
-Single agent/Multiple agent *
-Accessible/Inaccessible
-Deterministic/Non-deterministic
-Episodic/Non-episodic
'''
class Enviro:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.state = {}
        self.states = []
        self.legalActs = None
        self.tasks = []
        self.agents = []
        self.agentsActCount = {}

    def __str__(self):
        str_ = "State\n" + self.writeState(self.state)
        str_= str_.replace(" | ", "\n").replace(" > ", ": ") + "\n"
        return str_

    @abstractmethod
    def initEnviro(self):
        pass

    @abstractmethod
    def percept_to_Agent(self, agent):
        pass

    @abstractmethod
    def act_to_Enviro(self, agent):
        pass

    @abstractmethod
    def render(self, gui, state):
        pass

    @abstractmethod
    def writeState(self, state):
        pass

    @abstractmethod
    def readState(self, str_):
        pass

    def runEnviro(self, filename = None, updates = None, verbose = False):
        self.initEnviro()
        if verbose: print("Running: \n" + self.__getEnviroVars())
        self.__initAgents()
        for a in self.agents: self.agentsActCount[a] = 0
        i = 0
        while(self.__agentsActive()):
            self.states.append(deepcopy(self.state))
            self.__updateAgents(i)
            if verbose: print(str(i) + ' ' + str(self))
            i += 1
            if updates != None and i > updates: break;
        if verbose: print("Done: \n" + self.__getEnviroVars())
        if filename != None:
            self.__writeEnviro(filename)

    def addAgent(self, agent):
        self.agents.append(agent)

    def __initAgents(self):
        for a in self.agents:
            a.setLegalActs(self.legalActs.copy())
            a.setTasks(self.tasks.copy())
            a.init_Agent()

    def __updateAgents(self, count):
        for a in self.agents:
            if a.active:
                self.percept_to_Agent(a)
                a.compute()
                self.act_to_Enviro(a)
                self.agentsActCount[a] += 1

    def __agentsActive(self):
        flag = False
        for a in self.agents:
            if a.active: flag = True
        return flag

    def __getEnviroVars(self):
        stats = "Enviro: / " + self.__class__.__name__ + "\n"
        str_ = "Agents: / "
        for a in self.agents: str_ += a.__class__.__name__ + " / "
        stats += str_[0:-3]+"\n"
        str_ = "Legal_Acts: / "
        for a in self.legalActs: str_ += str(a) + " / "
        stats += str_[0:-3]+"\n"
        str_ = "Tasks: / "
        for t in self.tasks: str_ += str(t) + " / "
        stats += str_[0:-3]+"\n"
        str_ = "Action_Counts: / "
        for a in self.agentsActCount:
            str_ += "( " + a.__class__.__name__
            str_ += " , " + str(self.agentsActCount[a]) + " ) / "
        stats += str_[0:-3] + "\n"
        return stats

    def __writeEnviro(self, filename):
        enviro_file = open(filename, "w")
        enviro_file.write(self.__getEnviroVars()+"\n")
        for s in self.states:
            enviro_file.write("State: / " + str(self.writeState(s)) + "\n")
