import pygame
class Event():
    def __init__(self,Window):
        self.window=Window
    def clickLeft(self,mouse_x,mouse_y):
        x=mouse_x // self.window.sizeBlock
        y=mouse_y // self.window.sizeBlock
        if self.window.Tboard.array[x][y].flagged:return
        if self.window.Tboard.array[x][y].bombExist:
            self.window.Tboard.prinfbomb(x, y)
        else: self.window.Tboard.prinfnum(mouse_x, mouse_y)
    def clickRight(self,mouse_x,mouse_y):
        x = mouse_x // self.window.sizeBlock
        y = mouse_y // self.window.sizeBlock
        flag=pygame.image.load('images/' + 'flag.png')
        flag=pygame.transform.scale(flag, (50, 50))
        emptyBlock = pygame.image.load('images/' + 'empty-block.png')
        emptyBlock = pygame.transform.scale(emptyBlock, (self.window.sizeBlock, self.window.sizeBlock))
        if self.window.Tboard.array[x][y].open:return
        if self.window.Tboard.array[x][y].flagged:
            self.window.Tboard.array[x][y].flagged=False
            self.window.screen.blit(emptyBlock,(x*self.window.sizeBlock,y*self.window.sizeBlock))
        else:
            self.window.Tboard.array[x][y].flagged=True
            self.window.screen.blit(flag, (x*self.window.sizeBlock, y*self.window.sizeBlock))
    def control(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.window.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pressed()
                if mouse[0] == 1:#kích chuật trái
                    self.clickLeft(mouse_x,mouse_y)
                elif mouse[2]==1:#kích chuật phải
                    self.clickRight(mouse_x,mouse_y)