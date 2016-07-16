from PyAide import BoardEnviro
from PyAide import RandomAgent

agent = RandomAgent()

enviro = BoardEnviro()
enviro.addAgent(agent)
enviro.runEnviro(filename = "data.txt",updates = 5000, verbose = True)
