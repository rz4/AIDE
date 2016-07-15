import pkgutil
print([name for _, name, _ in pkgutil.iter_modules(['testpkg'])])

from Enviros.Enviro import Enviro
from Agents.Agent import Agent
from Enviros.CustomEnviros.BoardEnviro import BoardEnviro
from Enviros.CustomEnviros.MazeEnviro import MazeEnviro
from Enviros.CustomEnviros.EightPuzzleEnviro import EightPuzzleEnviro
from Agents.CustomAgents.RandomAgent import RandomAgent
from Tools.AIDEGUI import AIDEGUI
