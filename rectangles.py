import pygame, sys
from pygame.locals import *

class Rectangle:
    global RED
    RECTSIZE = 50
    RECTX = 10
    RECTY = 100
    RED = (255,0,0)
    
    def __init__(self, x, y):
        self.rplayer = pygame.Rect(x, y, 50, 50)

    def render(self, SURF):
        pygame.draw.rect(SURF, RED, self.rplayer, 0)
        
    def getPos(self):
        return self.rplayer.x, self.rplayer.y
    
    def update(self):
        if self.rplayer.y == 480:
            self.rplayer.y = -50
        else:
            self.rplayer.y +=1