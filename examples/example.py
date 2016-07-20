from PyAIDE import BoardEnviro
from PyAIDE import RandomAgent

agent = RandomAgent()

enviro = BoardEnviro()
enviro.add_agent(agent)
enviro.runEnviro(filename = "data.txt",updates = 5000, verbose = True)
