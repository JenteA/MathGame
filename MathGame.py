import pygame, sys, enemies
from enemies import *
from pygame.locals import *


FPS = 50
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
clock = pygame.time.Clock()

def main():
    pygame.init()
    font = pygame.font.Font("./fonts/arial.ttf", 20)
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Math Game')
    ENEMY = Enemy(10, font)
    while True:
        clock.tick(FPS)
        DISPLAYSURF.fill( (0,0,0) )
        ENEMY.update(font)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        ENEMY.Render(DISPLAYSURF)
        pygame.display.update()
        
if __name__ == '__main__':
    main()