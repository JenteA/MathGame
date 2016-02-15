import pygame, sys
from pygame.locals import *
from random import randint

class Enemy:
    global RED
    RED = (255,0,0)
    
    def __init__(self, x, y, font):
        self.rplayer = pygame.Rect(x, y, 50, 50)
        self.multip = Multiplication()
        self.multiplText = self.multip.getExer(font)

    def Render(self, SURF):
        pygame.draw.rect(SURF, RED, self.rplayer, 0)
        SURF.blit(self.multiplText, (self.rplayer.x, self.rplayer.y))
        
    def getPos(self):
        return self.rplayer.x, self.rplayer.y
    
    def update(self, font, score, life):
        if self.rplayer.y == 480:
            self.rplayer.y = -50
            self.multiplText = self.multip.getExer(font)
            score-=3
            life -=1
            hit = True
            return hit
        else:
            self.rplayer.y +=1
            
class Multiplication:
    def __init__(self):
        self.val1 = None
        self.val2 = None
        
    def getExer(self, font):
        self.val1 = randint(0,10)
        self.val2 = randint(0,10)
        self.sol = self.val1*self.val2
        return font.render(str(self.val1)+"X"+str(self.val2), True, (0,0,0))