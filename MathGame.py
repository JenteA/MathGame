import pygame, sys, enemies
from enemies import *
from pygame.locals import *
from random import randint, randrange
sys.path.append("./libraries/")
import eztext


FPS = 50
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
clock = pygame.time.Clock()
ENEMY = []

def main():
    pygame.init()
    font = pygame.font.Font("./fonts/arial.ttf", 20)
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Math Game')
    txtbx = eztext.Input(maxlength=5, color=(255,0,0), prompt='schrijf hier je uitkomst: ')
    for x in range(3):
        enemy = Enemy(randint(1,590), -randint(50,100), font)
        ENEMY.append(enemy)
    while True:
        clock.tick(FPS)
        DISPLAYSURF.fill( (0,0,0) )
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    for x in range(len(ENEMY)):
                        if txtbx.value == str(ENEMY[x].multip.sol):
                            ENEMY.pop(x)
                    txtbx.value = ""
        for x in range(len(ENEMY)):
            ENEMY[x].update(font)
            ENEMY[x].Render(DISPLAYSURF)
        txtbx.update(events)
        txtbx.set_pos(0,460)
        txtbx.draw(DISPLAYSURF)
        pygame.display.update()
        
if __name__ == '__main__':
    main()