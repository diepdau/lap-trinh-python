import pygame
from assets.constants import FONTMESSAGE, WIDTH, HEIGHT

class BlinkText():
    def __init__(self, text):
        self.text = text
        self.size = 18
        self.surface = FONTMESSAGE.render(self.text, False, (207,0,0))

    def update(self):
        pass

    def draw(self, WIN):#căn giữa
        WIN.blit(self.surface, (WIDTH // 2 - self.surface.get_width() // 2, HEIGHT // 2 - self.surface.get_height() // 2))
