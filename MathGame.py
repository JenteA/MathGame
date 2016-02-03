import pygame, sys, rectangles
from rectangles import *
from pygame.locals import *

FPS = 50
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
clock = pygame.time.Clock()

def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Math Game')
    RECTANGULAR = Rectangle(10, 100)
    while True:
        clock.tick(FPS)
        DISPLAYSURF.fill( (0,0,0) )
        RECTANGULAR.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        RECTANGULAR.render(DISPLAYSURF)
        pygame.display.update()
        
if __name__ == '__main__':
    main()