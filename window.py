import pygame
from umbrella import Umbrella
from board import Board
import os

class Window(object):
    def __init__(self):
        self.GREY = (150, 150, 150)
        self.WHILE = (255, 255, 255)
        self.RED = (250, 0, 0)
        self.sizeBlock = 50
        self.Line=9
        # self.game = game
        self.WIDTH = self.Line*self.sizeBlock+self.Line
        self.HEIGHT = self.Line*self.sizeBlock+self.Line
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.Tboard = Board(self, 16)
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
        # self.Tboard.loadPictures()
        running = True
        while running:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.Tboard.array[mouse_x//self.sizeBlock][mouse_y//self.sizeBlock].bombExist:
                            self.Tboard.prinfbomb(mouse_x,mouse_y)
                        else:
                            self.Tboard.prinfnum(mouse_x,mouse_y)
            pygame.display.flip()