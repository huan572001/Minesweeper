import pygame
from window import Window
from pygame.locals import *

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Game():
    def __init__(self):
        # self.screen = pygame.display.set_mode((600, 600))
        self.running = True

    def run(self):
        while self.running:
            mouse_x, mouse_y = pygame.mouse.get_pos()  # lấy tọa đọ chuật
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  #
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pressed()  # nhận được trạng thái của các nút chuột
                    if mouse[0] == 1:  # kích chuật trái
                        if 200 < mouse_x < 400 and 200 < mouse_y < 250:
                            app = Window(9, self, 10)
                            app.draw()
                            app.Running()
                        elif 200 < mouse_x < 400 and 300 < mouse_y < 350:
                            app = Window(16, self, 40)
                            app.draw()
                            app.Running()
                        elif 200 < mouse_x < 400 and 400 < mouse_y < 450:
                            app = Window(20, self, 60)
                            app.draw()
                            app.Running()
            pygame.display.flip()  # cập nhật nội dung của toàn bộ màn hình

    def textSet(self, t, x, y):
        pygame.init()
        font = pygame.font.SysFont('console', 50)
        text = font.render(t, True, WHITE)
        self.screen.blit(text, (x, y))

    def drawmenu(self):
        self.screen = pygame.display.set_mode((600, 600))
        self.textSet('MINESWEEPER', 150, 100)
        pygame.draw.rect(self.screen, GREEN, (200, 200, 200, 50))  # Hình chữ nhật
        self.textSet('9x9', 250, 200)
        pygame.draw.rect(self.screen, RED, (200, 300, 200, 50))  # Hình chữ nhật
        self.textSet('16x16', 220, 300)
        pygame.draw.rect(self.screen, BLUE, (200, 400, 200, 50))  # Hình chữ nhật
        self.textSet('20x20', 220, 400)

