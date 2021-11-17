import pygame
from umbrella import Umbrella
from board import Board
from event import Event
import os

class Window(object):
    def __init__(self):
        self.sizeBlock = 25#kich thước 1 ô
        self.Line=18#so ô trên 1 dòng
        self.event = Event(self)
        self.WIDTH = self.Line*self.sizeBlock#chiều ngang cửa sổ bằng số dòng nhân kích thước
        self.HEIGHT = self.Line*self.sizeBlock#chiều cao cửa sổ bằng số cột nhân kích thước
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))#cửa sổ hiển thị
        self.Tboard = Board(self, 36)#tạo đối tượng bảng
        self.running = True
    def draw(self):#vẽ bảng
        self.Tboard.array.pop(0)#lấy ra ô khởi tạo sẵn ban đầu và xóa nó khỏi mảng
        for col in range(self.Line):#tạo phàn tử có mảng hai chiều
            temp=[]
            for row in range(self.Line):
                temp.append(Umbrella())
                self.screen.blit(self.Tboard.Pictures["empty-block"], (col*self.sizeBlock,row*self.sizeBlock))
            self.Tboard.array.append(temp)

    def Running(self):
        self.Tboard.createBomb()#khởi tạo bom
        self.Tboard.createNumber()#khởi tạo số cho các ô
        while self.running:
            self.event.control()#thao tác chuật
            pygame.display.flip()#cập nhật nội dung của toàn bộ màn hình