import random
import pygame
from umbrella import Umbrella
class Board():
    def __init__(self,Window,NumberOfBoom):
        self.window=Window
        self.line=self.window.Line #so dong
        self.columns=self.window.Line#so cot
        self.numberOfBoom=NumberOfBoom#so boom
        self.flag=0#số cờ đã đánh dấu
        self.array=[[Umbrella(-99,-99)]]
    # def loadPictures(self):
    #     self.images = {}
    #     imagesDirectory = "images"
    #     for fileName in os.listdir(imagesDirectory):
    #         if not fileName.endswith(".png"):
    #             continue
    #         path = imagesDirectory + r"/" + fileName
    #         img = pygame.image.load(path)
    #         img = img.convert()
    #         img = pygame.transform.scale(img, (int(self.pieceSize[0]), int(self.pieceSize[1])))
    #         self.images[fileName.split(".")[0]] = img
    def prinfnum(self,x,y):
        # self.images
        #chưa tối ưu code
        arr = []
        zero = pygame.image.load('images/' + '0.png')
        zero = pygame.transform.scale(zero, (50, 50))
        arr.append(zero)
        One = pygame.image.load('images/' + '1.png')
        One = pygame.transform.scale(One, (50, 50))
        arr.append(One)
        Two = pygame.image.load('images/' + '2.png')
        Two = pygame.transform.scale(Two, (50, 50))
        arr.append(Two)
        three = pygame.image.load('images/' + '3.png')
        three = pygame.transform.scale(three, (50, 50))
        arr.append(three)
        four = pygame.image.load('images/' + '4.png')
        four = pygame.transform.scale(four, (50, 50))
        arr.append(four)
        five = pygame.image.load('images/' + '5.png')
        five = pygame.transform.scale(five, (50, 50))
        arr.append(five)
        six = pygame.image.load('images/' + '6.png')
        six = pygame.transform.scale(six, (50, 50))
        arr.append(six)
        seven = pygame.image.load('images/' + '7.png')
        seven = pygame.transform.scale(seven, (50, 50))
        arr.append(seven)
        eight = pygame.image.load('images/' + '8.png')
        eight = pygame.transform.scale(eight, (50, 50))
        arr.append(eight)
        #22
        x=x-x%50
        y=y-y%50
        for a in self.array:
            for i in a:
                if i.x==x and i.y==y:
                    print(i.number)
                    self.window.screen.blit(arr[i.number], (x, y))
                    i.open=True
    def prinfbomb(self,x,y):
        bomb = pygame.image.load('images/' + 'wrong-flag.png')
        bomb = pygame.transform.scale(bomb, (50, 50))
        x = x - x % 50
        y = y - y % 50
        for a in self.array:
            for i in a:
                if i.x==x and i.y==y:
                    self.window.screen.blit(bomb, (x, y))
                    i.open=True
    def createBomb(self):
        n=0
        while n<self.numberOfBoom:
            temp1=random.randint(0,self.line-1)
            temp2=random.randint(0,self.line-1)
            if self.array[temp1][temp2].bombExist:
                continue
            self.array[temp1][temp2].bombExist=True
            n+=1
    def bombCount(self,x,y):
        count=0
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                #xét những vị trí không hợp=> tiếp tục lặp
                if i<0 or i>=self.line or j<0 or j>=self.columns or (i==x and j==y): continue
                else:
                    #xét xem ô có bomb hay ko
                    if self.array[i][j].bombExist:count+=1
        return count
    def createNumber(self):
        for i in range(self.line):
            for j in range(self.columns):
                self.array[i][j].number=self.bombCount(i,j)