import pygame, sys, enemies, showText
from enemies import *
from showText import *
from pygame.locals import *
from random import randint, randrange
sys.path.append("./libraries/")
import eztext

FPS = 20
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
clock = pygame.time.Clock()
ENEMY = []

def main():
    pygame.init()
    SCORE = 0
    LIFE = 100
    HIT = False
    font = pygame.font.Font(None, 32)
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Math Game')
    txtbx = eztext.Input(maxlength=5, color=(255,0,0), prompt='schrijf hier je uitkomst: ')
    text = ShowText()
    for x in range(1):
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
                            SCORE+=5
                            for x in range(2):
                                enemy = Enemy(randint(1,590), -randint(50,100), font)
                                ENEMY.append(enemy)
                    txtbx.value = ""
        for x in range(len(ENEMY)):
            HIT = ENEMY[x].update(font, SCORE, LIFE)
            ENEMY[x].Render(DISPLAYSURF)
            if HIT == True:
                SCORE -= 3
                LIFE -= 1
                HIT = False
        txtbx.update(events)
        txtbx.set_pos(0,460)
        txtbx.draw(DISPLAYSURF)
        text.renderScreenText(DISPLAYSURF, SCORE, font)
        text.renderLifeBar(0, LIFE, DISPLAYSURF)
        pygame.display.update()
        
if __name__ == '__main__': main()