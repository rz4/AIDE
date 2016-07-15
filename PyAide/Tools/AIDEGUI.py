#!/usr/bin/python3
"""
Project: AIDE
File: EnviroData.py
Author: Rafael Zamora
Version: 0.01
Date Updated: 6/18/2016

Change Log:
-ADDED Replay from enviro file.
"""
import pygame

class AIDEGUI:

    def __init__(self):
        self.pygame = pygame
        self.screen = pygame.display.set_mode((800, 600))
        self.filename = None
        self.data = []
        self.enviro = None

    def loadFile(self, filename):
        self.filename = filename
        enviro_file = open(filename, "r")
        for enviro_str in enviro_file:
            varss = enviro_str.strip().split(" / ")
            self.data.append(varss)
        module = __import__("PyAide.Enviros.CustomEnviros")
        class_ = getattr(module, self.data[0][1])
        self.enviro = class_()

    def run(self):
        self.pygame = pygame
        self.pygame.init()
        self.pygame.display.set_caption("AIDEGUI v0.5")
        done = False
        play = False
        i = 0
        while not done:
            #Rendering
            self.screen.fill((0, 0, 0))
            pygame.draw.rect(self.screen,(100,100,100),pygame.Rect(600,0,800,600))
            basicfont = pygame.font.SysFont(None, 16)
            self.drawString("Welcome to AIDEGUI version 0.5!", 602,2)
            self.drawString("Controls: Left - Previous Frame", 602,36)
            self.drawString("Right - Next Frame", 602,54)
            self.drawString("R - Reset", 602,70)
            self.drawString("Space - Play/Pause", 602,86)
            self.drawString("Frame: "+ str(i), 602,122)
            self.drawString("Enviro Info", 662,150)
            self.drawString("Enviro Name: " + self.enviro.__class__.__name__, 602,176)
            if self.enviro != None:
                self.enviro.render(self, self.enviro.readState(self.data[i+6][1]))

            #Events and Controls
            for event in self.pygame.event.get():
                    if event.type == self.pygame.QUIT:
                            done = True
                    if event.type == self.pygame.KEYDOWN:
                        if event.key == self.pygame.K_RIGHT:
                            play = False
                            if i+1 < len(self.data)-6: i +=1
                        if event.key == self.pygame.K_LEFT:
                            play = False
                            if i > 0: i -=1
                        if event.key == self.pygame.K_SPACE:
                            play = not play
                        if event.key == self.pygame.K_r:
                            play = False
                            i = 0
            if play:
                if i+1 < len(self.data)-6: i +=1

            self.pygame.display.flip()

    def drawString(self, str_, x, y, centered = False, font_size = 16, color = (255, 255, 255)):
        font = self.pygame.font.SysFont(None, font_size)
        text = font.render(str_, True, color)
        textrect = text.get_rect()
        if centered:
            textrect.centerx = x
            textrect.centery = y
        else:
            textrect.x = x
            textrect.y = y
        self.screen.blit(text, textrect)
