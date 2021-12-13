import pygame
from umbrella import Umbrella
from board import Board
from event import Event

import os

pygame.display.set_caption('Minesweeper')
GRAY = (112, 112, 112)


class Window():
    def __init__(self, line, game, NumberofBoom):
        self.event = Event(self)
        self.game = game
        self.sizeBlock = 35  # kich thước 1 ô
        self.Line = line  # so ô trên 1 dòng
        self.windowsetting = self.sizeBlock
        self.WIDTH = self.Line * self.sizeBlock  # chiều ngang cửa sổ bằng số dòng nhân kích thước
        self.HEIGHT = self.Line * self.sizeBlock + self.windowsetting  # chiều cao cửa sổ bằng số cột nhân kích thước
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))  # cửa sổ hiển thị
        self.numberofBoom = NumberofBoom
        self.Tboard = Board(self, self.numberofBoom)  # tạo đối tượng bảng
        # self.running = True

    def drawPictures(self, fileName, x, y):
        self.screen.blit(self.Tboard.Pictures[fileName],
                         (x * self.sizeBlock, self.windowsetting + y * self.sizeBlock))

    # def draw(self):  # vẽ bảng
    #     self.Tboard.array.pop(0)  # lấy ra ô khởi tạo sẵn ban đầu và xóa nó khỏi mảng
    #     self.screen.blit(self.Tboard.Pictures['restart'], (100, 0))
    #     for col in range(self.Line):  # tạo phàn tử có mảng hai chiều
    #         temp = []
    #         for row in range(self.Line):
    #             temp.append(Umbrella())
    #             self.drawPictures("empty-block", col, row)
    #         self.Tboard.array.append(temp)
    def draw(self):  # vẽ bảng
        self.screen.fill(GRAY)
        self.screen.blit(self.Tboard.Pictures['0'], (0, 0))
        self.Tboard.SumBoom(self.Tboard.ChangeBoom)
        self.screen.blit(self.Tboard.Pictures['restart'], ((self.Line // 2 * self.sizeBlock), 0))
        self.screen.blit(self.Tboard.Pictures['setting'], ((self.Line * self.sizeBlock - self.sizeBlock), 0))
        for col in range(self.Line):  # ve bang
            for row in range(self.Line):
                self.drawPictures("empty-block", col, row)

    def reset(self):
        self.Tboard = Board(self, self.numberofBoom)  # tạo đối tượng bảng
        self.Tboard.createBomb()  # khởi tạo bom
        self.Tboard.createNumber()  # khởi tạo số cho các ô

    def Running(self):
        self.Tboard.createBomb()  # khởi tạo bom
        self.Tboard.createNumber()  # khởi tạo số cho các ô
        while self.game.running:
            self.event.control()  # thao tác chuật
            pygame.display.flip()  # cập nhật nội dung của toàn bộ màn hình
