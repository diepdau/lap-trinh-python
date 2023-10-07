import pygame, random, math
from assets.constants import SIZE_BLOCK, SIZE_SQUARE, BORDER, FONT, BLACK

pygame.init()

class board:
    def __init__(self, game):
        self.game = game
        self.init()

    def init(self):
        self.board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        lst = random.choices(range(16), k=2)
        for pos in lst:
            x = pos % SIZE_BLOCK
            y = pos // SIZE_BLOCK
            self.board[y][x] = 2

    def reset(self):
        self.init()

    def __noname__(self):
        lst = []
        for i in range(SIZE_BLOCK):
            for j in range(SIZE_BLOCK):
                if self.board[j][i] == 0:
                    lst.append((i, j))
        x, y = random.choice(lst)
        self.board[y][x] = 2

    def checkendgame(self):
        gameOver = True
        for i in range(SIZE_BLOCK):
            for j in range(SIZE_BLOCK):
                if self.board[j][i] == 0:
                    gameOver = False
                    return None
        self.game.gameOver = gameOver


    def update(self, event):
        mark = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        isMoved = False
        if event == "K_LEFT":
            for x in range(1, SIZE_BLOCK):
                for y in range(SIZE_BLOCK):
                    if self.board[y][x] != 0:
                        i, j = x, y
                        while i - 1 >= 0 and self.board[j][i-1] == 0:
                            i -= 1
                        
                        if i - 1 >= 0:
                            if self.board[j][i-1] == self.board[y][x] and not mark[j][i-1]:
                                self.board[j][i-1] *= 2
                                self.board[y][x] = 0
                                mark[j][i-1] = 1
                                isMoved = True
                            elif i != x:
                                self.board[j][i] = self.board[y][x]
                                self.board[y][x] = 0
                                isMoved = True
                        else:
                            self.board[j][i] = self.board[y][x]
                            self.board[y][x] = 0
                            isMoved = True

            

        if event == "K_RIGHT":
            for x in range(SIZE_BLOCK - 2, -1, -1):
                for y in range(SIZE_BLOCK):
                    if self.board[y][x] != 0:
                        i, j = x, y
                        while i + 1 <= SIZE_BLOCK - 1 and self.board[j][i+1] == 0:
                            i += 1
                        
                        if i + 1 <= SIZE_BLOCK - 1:
                            if self.board[j][i+1] == self.board[y][x] and not mark[j][i+1]:
                                self.board[j][i+1] *= 2
                                self.board[y][x] = 0
                                mark[j][i+1] = 1
                                isMoved = True
                            elif i != x:
                                self.board[j][i] = self.board[y][x]
                                self.board[y][x] = 0
                                isMoved = True
                        else:
                            self.board[j][i] = self.board[y][x]
                            self.board[y][x] = 0
                            isMoved = True

            

        if event == "K_UP":
            for y in range(1, SIZE_BLOCK):
                for x in range(SIZE_BLOCK):
                    if self.board[y][x] != 0:
                        i, j = x, y
                        while j - 1 >= 0 and self.board[j-1][i] == 0:
                            j -= 1
                        
                        if j - 1 >= 0:
                            if self.board[j-1][i] == self.board[y][x] and not mark[j-1][i]:
                                self.board[j-1][i] *= 2
                                self.board[y][x] = 0
                                mark[j-1][i] = 1
                                isMoved = True
                            elif j != y:
                                self.board[j][i] = self.board[y][x]
                                self.board[y][x] = 0
                                isMoved = True
                        else:
                            self.board[j][i] = self.board[y][x]
                            self.board[y][x] = 0
                            isMoved = True

        

        if event == "K_DOWN":
            for y in range(SIZE_BLOCK - 2, -1, -1):
                for x in range(SIZE_BLOCK):
                    if self.board[y][x] != 0:
                        i, j = x, y
                        while j + 1 <= SIZE_BLOCK - 1 and self.board[j+1][i] == 0:
                            j += 1
                        
                        if j + 1 <= SIZE_BLOCK - 1:
                            if self.board[j+1][i] == self.board[y][x] and not mark[j+1][i]:
                                self.board[j+1][i] *= 2
                                self.board[y][x] = 0
                                mark[j+1][i] = 1
                                isMoved = True
                            elif j != y:
                                self.board[j][i] = self.board[y][x]
                                self.board[y][x] = 0
                                isMoved = True
                        else:
                            self.board[j][i] = self.board[y][x]
                            self.board[y][x] = 0
                            isMoved = True

        if isMoved: self.__noname__()
        else:
            self.checkendgame()


    def draw(self, WIN):
        for y in range(SIZE_BLOCK):
            for x in range(SIZE_BLOCK):
                r = math.log2(max(self.board[y][x], 1)) * 20
                g = 255 - math.log2(max(self.board[y][x], 1)) * 20
                b = 255 - math.log2(max(self.board[y][x], 1)) * 20
                SURF = pygame.Surface((SIZE_SQUARE - BORDER * 2, SIZE_SQUARE - BORDER * 2))
                SURF.fill((r, g, b))
                if self.board[y][x] > 0:
                    TEXT_SUR = FONT.render(str(self.board[y][x]), True, BLACK)
                    x_cen = SURF.get_width() // 2 - TEXT_SUR.get_width() // 2
                    y_cen = SURF.get_height() // 2 - TEXT_SUR.get_height() // 2
                    SURF.blit(TEXT_SUR, (x_cen, y_cen), (0, 0, TEXT_SUR.get_width(), TEXT_SUR.get_height()))
                WIN.blit(SURF, (x * SIZE_SQUARE + BORDER, y * SIZE_SQUARE + BORDER), (0, 0, SURF.get_width(), SURF.get_height()))
        
