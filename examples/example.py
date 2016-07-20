from PyAIDE import BoardEnviro
from PyAIDE import RandomAgent

agent = RandomAgent()

enviro = BoardEnviro()
enviro.add_agent(agent)
enviro.run_enviro(filename = "data.txt",updates = 5000, verbose = True)
