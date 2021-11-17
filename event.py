import pygame
class Event():
    def __init__(self,Window):
        self.window=Window
    def clickLeft(self,mouse_x,mouse_y):
        # lấy tạo độ của mảng 2 chiều
        x=mouse_x // self.window.sizeBlock
        y=mouse_y // self.window.sizeBlock
        #nếu ô chưa mở và ô chưa cắm cờ
        if (not self.window.Tboard.array[x][y].open) and (not self.window.Tboard.array[x][y].flagged):
            self.window.Tboard.openUmbrella(x,y)

    def clickRight(self,mouse_x,mouse_y):
        x = mouse_x // self.window.sizeBlock
        y = mouse_y // self.window.sizeBlock
        #nếu ô dang mơ thì thoát
        if self.window.Tboard.array[x][y].open:return
        #nếu ô đang cắm cờ thì tắt cờ đi
        if self.window.Tboard.array[x][y].flagged:
            self.window.Tboard.array[x][y].flagged=False
            self.window.screen.blit(self.window.Tboard.Pictures["empty-block"],(x*self.window.sizeBlock,y*self.window.sizeBlock))
        else:#nếu ô chưa cắm cờ thì cắm cờ vô
            self.window.Tboard.array[x][y].flagged=True
            self.window.screen.blit(self.window.Tboard.Pictures["flag"], (x*self.window.sizeBlock, y*self.window.sizeBlock))
    def control(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()#lấy tọa đọ chuật
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#
                self.window.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pressed()#nhận được trạng thái của các nút chuột
                if mouse[0] == 1:#kích chuật trái
                    self.clickLeft(mouse_x,mouse_y)
                elif mouse[2]==1:#kích chuật phải
                    self.clickRight(mouse_x,mouse_y)