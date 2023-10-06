import pygame
from assets.board import board
from assets.msgtext import BlinkText

class game:
    def __init__(self):
        self.run = False
        self.board = board(self)
        self.gameOver = False
        self.start_text = BlinkText("Enter to start")
        self.gameOver_text = BlinkText("Game over, R to reset!!!")
        self.clock = pygame.time.Clock()

    def reset(self):
        self.board = board(self)
        self.gameOver = False
