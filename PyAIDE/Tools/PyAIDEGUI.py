#!/usr/bin/python3
'''
Project: PyAIDE
File: PyAIDEGUI.py
Author: Rafael Zamora
Version: 1.0.0
Date Updated: 7/18/2016

Change Log:
'''

import tkinter
from json import loads

class PyAIDEGUI:
    """PyAIDEGUI is PyAIDE tool used to replay a simulation's data file.

    PyAIDEGUI is built using Tkinter in order to provide accesability.

    State data is displayed in string form. A graphical representation
    is displayed if defined in the enviro's render() function. Four controls
    in the form of buttons are available: Pause/Play, Previous, Next, and Reset.

    """

    def __init__(self):
        # Data parameters
        self.iter = 0
        self.pause = True
        self.json_data = []
        self.enviro = None

        # Root frame parameters
        self.root = tkinter.Tk()
        self.root.wm_title("PyAIDE-GUI v1.0.0")
        self.root.minsize(900, 600)

        # Frames, buttons, canvas parameters
        info_frame = tkinter.Frame(self.root)
        button_frame = tkinter.Frame(info_frame)
        _pause = tkinter.Button(button_frame, text ="Play/Pause", command = self.pauseIter)
        _next = tkinter.Button(button_frame, text ="Next", command = self.incrIter)
        _prev = tkinter.Button(button_frame, text ="Prev", command = self.decrIter)
        _reset = tkinter.Button(button_frame, text ="Reset", command = self.resetIter)
        self.canvas = tkinter.Canvas(self.root, bg = "black")
        self.text = tkinter.Text(info_frame, font=("Helvetica",10))

        # Positioning and layout
        info_frame.place(height=600, width=300, x = 600, y = 0)
        button_frame.place(height=200, width=300, x = 0, y = 400)
        _pause.place(height=50, width=300, x = 0, y = 0)
        _next.place(height=50, width=300, x = 0, y = 50)
        _prev.place(height=50, width=300, x = 0, y = 100)
        _reset.place(height=50, width=300, x = 0, y = 150)
        self.canvas.place(height=600, width=600, x = 0, y = 0)
        self.text.place(height=400, width=300, x = 0, y = 0)

    def loadFile(self, filename):
        json_file = open(filename, "r")
        for json_str in json_file: self.json_data.append(json_str)
        data = loads(self.json_data[0])
        module = __import__("PyAIDE.Enviros.CustomEnviros")
        class_ = getattr(module, data["Enviro"])
        self.enviro = class_()

    def run(self, filename):
        self.loadFile(filename)
        self.animate()
        self.root.mainloop()

    def animate(self):
        if not self.pause: self.incrIter()
        self.drawText()
        self.drawCanvas()
        delay = 25
        self.canvas.after(delay, self.animate)

    def drawCanvas(self):
        self.canvas.delete(tkinter.ALL)
        data = loads(self.json_data[1+self.iter])
        self.enviro.render(self.canvas, data)

    def drawText(self):
        self.text.delete(1.0, tkinter.END)
        enviro_data = loads(self.json_data[0])
        self.text.insert(tkinter.INSERT, "Enviro : " + enviro_data["Enviro"])
        self.text.insert(tkinter.INSERT, "\nLegal Actions : " + str(enviro_data["Legal_Acts"]))
        self.text.insert(tkinter.INSERT, "\n\nIteration : " + str(self.iter))
        self.text.insert(tkinter.INSERT, "\n\n" + self.json_data[1+self.iter][2:-2].replace(", \"", "\n"))

    def pauseIter(self):
        self.pause =  not self.pause

    def incrIter(self):
        if self.iter < len(self.json_data)-2: self.iter += 1
        else: self.pauseIter()

    def decrIter(self):
        if self.iter > 0: self.iter -= 1

    def resetIter(self):
        self.iter = 0
