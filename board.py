import random
import pygame
import os
from umbrella import Umbrella


class Board():
    def __init__(self, Window, NumberOfBoom):
        self.window = Window
        self.line = self.window.Line  # so dong
        self.columns = self.window.Line  # so cot
        self.numberOfBoom = NumberOfBoom  # so boom
        self.flag = 0  # số cờ đã đánh dấu
        self.Pictures = self.loadPictures()  # Dictionary chứa ảnh
        self.Lose = False
        self.array = [[Umbrella()]]  # khởi tạo mảng hai chiều chứa các ô
        self.createarray()
    def createarray(self):
        del self.array[0]
        for col in range(self.line):#tạo phàn tử có mảng hai chiều
            temp=[]
            for row in range(self.line):
                temp.append(Umbrella())
            self.array.append(temp)
    def loadPictures(self):  # tải ảnh lên
        images = {}

        # Phương thức này trả về một danh sách chứa tên của các mục trong thư mục images
        for fileName in os.listdir("images"):
            # những file ko có đuôi .png thì bỏ qua
            if not fileName.endswith(".png"):
                continue
            # tải hình ảnh từ tệp images
            img = pygame.image.load('images/' + fileName)
            # tạo kích thước cho hinh ảnh
            img = pygame.transform.scale(img, (self.window.sizeBlock, self.window.sizeBlock))
            # cho hinh ảnh vào Dictionary key là ký tự trước dấu "." valua là img
            images[fileName.split(".")[0]] = img
        return images

    def prinfbomb(self, x, y):
        self.window.drawPictures("bomb-at-clicked-block", x, y)
        self.array[x][y].open = True
        # duyetj taonf bộ mảng hai chiều
        for col in range(self.line):
            for row in range(self.line):
                # nếu ô không mở
                if not self.array[col][row].open:
                    # nếu ô đã cắm cờ
                    if self.array[col][row].flagged:
                        # nếu ô ko có bom
                        if not self.array[col][row].bombExist:
                            self.window.drawPictures("wrong-flag", col, row)
                    else:
                        # nếu ô có bom
                        if self.array[col][row].bombExist:
                            self.window.drawPictures("unclicked-bomb", col, row)
                            self.Lose = True

    def openUmbrella(self, x, y):  # hàm mở ô
        # nếu ô chưa mở và ô chưa cắm cờ
        if (not self.array[x][y].open) and (not self.array[x][y].flagged):
            self.array[x][y].open = True
            # nếu ô có bom thì tin ra taonf bộ bom và kết thúc game
            if self.array[x][y].bombExist:
                self.prinfbomb(x, y)
            else:
                if self.array[x][y].number > 0:
                    self.window.drawPictures(str(self.array[x][y].number), x, y)
                else:  # ô không có số
                    self.window.drawPictures(str(self.array[x][y].number), x, y)
                    for i in range(x - 1, x + 2):
                        for j in range(y - 1, y + 2):
                            # xét những vị trí không hợp=> tiếp tục lặp
                            if i < 0 or i >= self.line or j < 0 or j >= self.columns or (i == x and j == y): continue
                            # dệ quy
                            self.openUmbrella(i, j)

    def createBomb(self):
        n = 0  # đếm số bom đc tạo ra
        while n < self.numberOfBoom:
            temp1 = random.randint(0, self.line - 1)  # random từ số 0 tới số dòng -1
            temp2 = random.randint(0, self.line - 1)
            # nếu có bom rồi thì random lại
            if self.array[temp1][temp2].bombExist:
                continue
            # bật cho ô này có bom và tăng n
            self.array[temp1][temp2].bombExist = True
            n += 1

    def bombCount(self, x, y):  # đếm số lượng bom xung quanh ô
        count = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                # xét những vị trí không hợp=> tiếp tục lặp
                if i < 0 or i >= self.line or j < 0 or j >= self.columns or (i == x and j == y):
                    continue
                else:
                    # xét xem ô có bomb hay ko
                    if self.array[i][j].bombExist: count += 1
        return count

    def createNumber(self):  # đánh số bom cho từng ô
        for i in range(self.line):
            for j in range(self.columns):
                self.array[i][j].number = self.bombCount(i, j)

    def countOpen(self):
        NumberOfOpened = 0
        for i in range(self.line):
            for j in range(self.columns):
                if not self.array[i][j].open:
                    NumberOfOpened += 1
        return NumberOfOpened

    def text(self, text):
        pygame.init()
        font = pygame.font.SysFont('console', 50)
        text = font.render(text, True, (0, 0, 0))
        self.window.screen.blit(text, (50, 50))

    def checkWin(self):
        if self.countOpen() == self.numberOfBoom:
            print(1)
            self.text('You Win')

    def checkLose(self):
        if self.Lose == True:
            print('lose')
            self.text('You Lose')
