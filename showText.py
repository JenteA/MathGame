import pygame, sys
from pygame.locals import *

class ShowText:
    def renderScreenText(self, SURF, score, font):
        self.scoreText = font.render("Score: "+str(score), True, (255,0,0))
        SURF.blit(self.scoreText, (520, 0))
        
    def renderLifeBar(self, x, life, SURF):
        lbar = []
        for i in range(life):
            LBAR = lifeBar(x)
            lbar.append(LBAR)
            lbar[i].Render(SURF)
            x = x+4
        
class lifeBar:
    def __init__(self, x):
        self.lifeBar = pygame.Rect(x, 0, 3, 10)
    
    def Render(self, SURF):
        pygame.draw.rect(SURF, (0,255,0), self.lifeBar, 0)
         