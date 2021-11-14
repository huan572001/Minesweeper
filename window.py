import pygame
from umbrella import Umbrella
from board import Board
from event import Event
import os

class Window(object):
    def __init__(self):
        self.GREY = (150, 150, 150)
        self.sizeBlock = 50
        self.Line=9
        self.event = Event(self)
        self.WIDTH = self.Line*self.sizeBlock+self.Line
        self.HEIGHT = self.Line*self.sizeBlock+self.Line
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.Tboard = Board(self, 16)
        self.running = True
    def draw(self):
        self.screen.fill(self.GREY)
        emptyBlock = pygame.image.load('images/' + 'empty-block.png')
        emptyBlock = pygame.transform.scale(emptyBlock, (50, 50))
        self.Tboard.array.pop(0)
        for col in range(self.Line):
            temp=[]
            for row in range(self.Line):
                temp.append(Umbrella(col*self.sizeBlock, row*self.sizeBlock))
                self.screen.blit(emptyBlock, (col*self.sizeBlock, row*self.sizeBlock))
            self.Tboard.array.append(temp)

    def Running(self):
        self.Tboard.createBomb()
        self.Tboard.createNumber()
        while self.running:
            self.event.control()
            pygame.display.flip()