#!/usr/bin/python3
'''
Project: PyAIDE
File: Enviro.py
Author: Rafael Zamora
Version: 1.0.0
Date Updated: 7/17/2016

Change Log:
'''

from abc import ABCMeta, abstractmethod
from copy import deepcopy
from json import dumps

class Enviro:
    """Enviro class is an abstract class used to define environments.

    The PyAIDE agent-enviro update cycle consists of the following
    functions in order:
    * Enviro's percept_to_Agent() function - Builds percept tuple
    * Agent's sense() function - Passes percept tuple to agent
    * Agent's compute() function - Agent behavior
    * Agent's act() function - Passes action to enviro
    * Enviros's act_to_Enviro() function - Updates enviro with action

    The following three functions must be defined in child class:
    * initEnviro() - function should initialize state variables and enviro variables
                     legalActs and tasks should be defined in this function.
    * percept_to_Agent() - function should build percept tuple that will be passed to agents.
    * act_to_Enviro() - function should update environment depending on action from agents.

    The render() funtion defines what will be rendered on PyAIDEGUI's tkinter canvas.
    This function can be overriden to display a custom graphical representation
    of the environment.

    """
    __metaclass__ = ABCMeta

    def __init__(self):
        self.state = {}
        self.states = []
        self.legalActs = None
        self.tasks = []
        self.agents = []
        self.agentsActCount = {}

    def __str__(self):
        str_ = "State: \n" + dumps(self.state)[2:-2].replace(", \"", "\n") + "\n"
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

    def render(self, canvas, state):
        return

    def runEnviro(self, filename = None, updates = None, verbose = False):
        self.initEnviro()
        if verbose: print("Running: " + self.__class__.__name__)
        self.__initAgents()
        for a in self.agents: self.agentsActCount[a.__class__.__name__] = 0
        i = 0
        while(self.__agentsActive()):
            self.states.append(deepcopy(self.state))
            self.__updateAgents(i)
            if verbose: print(str(i) + ' ' + str(self))
            i += 1
            if updates != None and i > updates: break;
        if verbose: print("Done: " + self.__class__.__name__)
        if filename != None:
            self.__writeData(filename)

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
                self.agentsActCount[a.__class__.__name__] += 1

    def __agentsActive(self):
        flag = False
        for a in self.agents:
            if a.active: flag = True
        return flag

    def __writeData(self, filename):
        enviro_file = open(filename, "w")
        enviroVars = {}
        enviroVars["Enviro"] = self.__class__.__name__
        enviroVars["Agents"] = [a.__class__.__name__ for a in self.agents]
        enviroVars["Legal_Acts"] = self.legalActs
        enviroVars["Tasks"] = self.tasks
        enviroVars["Action_Counts"] = self.agentsActCount
        data = enviroVars
        data_json = dumps(data)
        enviro_file.write(data_json + "\n")
        for state in self.states:
            data = state
            data_json = dumps(data)
            enviro_file.write(data_json + "\n")
