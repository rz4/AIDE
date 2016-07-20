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
        self.state_data = {}
        self.state_datas = []
        self.enviro_data = {}
        self.enviro_data["Enviro"] = self.__class__.__name__
        self.enviro_data["Legal_Acts"] = None
        self.enviro_data["Tasks"] = []
        self.enviro_data["Agents"] = []
        self.enviro_data["Agents_Act_Count"] = {}

    def __str__(self):
        str_ = "State: \n" + dumps(self.state_data)[2:-2].replace(", \"", "\n") + "\n"
        return str_

    @abstractmethod
    def init_enviro(self):
        pass

    @abstractmethod
    def percept_to_agent(self, agent):
        pass

    @abstractmethod
    def act_to_enviro(self, agent):
        pass

    def render(self, canvas, state_data):
        return

    def run_enviro(self, filename = None, updates = None, verbose = False):
        if verbose: print("Running: " + self.__class__.__name__)
        self.init_enviro()
        print(self.enviro_data)
        self.__init_agents()
        i = 0
        while(self.__agents_active()):
            self.state_datas.append(deepcopy(self.state_data))
            self.__update_agents(i)
            if verbose: print(str(i) + ' ' + str(self))
            if updates != None and i > updates: break;
            i += 1
        if filename != None: self.__write_data(filename)
        if verbose: print("Done: " + self.__class__.__name__)

    def add_agent(self, agent):
        self.enviro_data["Agents"].append(agent)

    def __init_agents(self):
        for a in self.enviro_data["Agents"]:
            a.set_legal_acts(self.enviro_data["Legal_Acts"].copy())
            a.set_tasks(self.enviro_data["Tasks"].copy())
            a.init_agent()
            self.enviro_data["Agents_Act_Count"][a.__class__.__name__] = 0

    def __update_agents(self, count):
        for a in self.enviro_data["Agents"]:
            if a.active:
                self.percept_to_agent(a)
                a.compute()
                self.act_to_enviro(a)
                self.enviro_data["Agents_Act_Count"][a.__class__.__name__] += 1

    def __agents_active(self):
        flag = False
        for a in self.enviro_data["Agents"]:
            if a.active: flag = True
        return flag

    def __write_data(self, filename):
        json_file = open(filename, "w")
        self.enviro_data["Agents"] = [a.__class__.__name__ for a in self.enviro_data["Agents"]]
        json_data = dumps(self.enviro_data)
        json_file.write(json_data + "\n")
        for state_data in self.state_datas:
            json_data = dumps(state_data)
            json_file.write(json_data + "\n")
