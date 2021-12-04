import pygame


class Event():
    def __init__(self, Window):
        self.window = Window

    def clickLeft(self, x, y):
        # lấy tạo độ của mảng 2 chiều
        # nếu ô chưa mở và ô chưa cắm cờ
        if x < 0 or y < 0:
            self.window.reset()
            self.window.draw()
        elif (not self.window.Tboard.array[x][y].open) and (not self.window.Tboard.array[x][y].flagged):
            self.window.Tboard.openUmbrella(x, y)
            self.window.Tboard.checkWin()
            self.window.Tboard.checkLose()

    def clickRight(self, x, y):
        # nếu ô dang mơ thì thoát
        if self.window.Tboard.array[x][y].open: return
        # nếu ô đang cắm cờ thì tắt cờ đi
        if x < 0 or y < 0: return
        if self.window.Tboard.array[x][y].flagged:
            self.window.Tboard.array[x][y].flagged = False
            self.window.drawPictures("empty-block", x, y)
        else:  # nếu ô chưa cắm cờ thì cắm cờ vô
            self.window.Tboard.array[x][y].flagged = True
            self.window.drawPictures("flag", x, y)

    def control(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()  # lấy tọa đọ chuật
        x = mouse_x // self.window.sizeBlock
        y = (mouse_y - self.window.windowsetting) // self.window.sizeBlock
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #
                self.window.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pressed()  # nhận được trạng thái của các nút chuột
                if mouse[0] == 1:  # kích chuật trái
                    self.clickLeft(x, y)
                elif mouse[2] == 1:  # kích chuật phải
                    self.clickRight(x, y)
