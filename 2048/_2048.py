import pygame
from pygame.locals import *
from assets.constants import WIDTH, HEIGHT, SIZE_SQUARE, SIZE_BLOCK, GRAY, FPS
from assets.game import game


pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

def main():
    Game = game()

    while not Game.run:
        Game.clock.tick(FPS)
        Game.start_text.update()
        Game.start_text.draw(WIN)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN and event.key in [13, 271]:
                Game.run = True
        

    while Game.run:
        for event in pygame.event.get():    
            if event.type == QUIT:
                Game.run = False 

            if event.type == KEYDOWN:
                if not Game.gameOver:
                    if event.key == K_LEFT:
                        Game.board.update("K_LEFT")
                    if event.key == K_RIGHT:
                        Game.board.update("K_RIGHT")
                    if event.key == K_UP:
                        Game.board.update("K_UP")
                    if event.key == K_DOWN:
                        Game.board.update("K_DOWN")
                else:
                    if event.key == K_r:
                        Game.board.reset()
                        Game.gameOver = False
        
        Game.clock.tick(FPS)
        WIN.fill(GRAY)
        Game.board.draw(WIN)
        if Game.gameOver:
            Game.gameOver_text.update()
            Game.gameOver_text.draw(WIN)
        pygame.display.update()

    pygame.quit()

main()
    