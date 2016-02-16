import pygame, sys
from pygame.locals import *

class Startscreen:
    def __init__(self, font):
        self.StartGame = pygame.Rect(250, 150, 50, 50)
        self.Text = font.render("MathGame", True, (0,0,0))
        self.TextStart = font.render("Start Spel", True, (255,255,0))
     def Render(self, SURF):
        pygame.draw.rect(SURF, RED, self.StartGame, 0)
        SURF.blit(self.TextStart, (self.StartGame.x, self.StartGame.y))
        SURF.blit(self.Text, (50, 150))
  
class MultiplicationScreen:
    def __init__(self, font):
        self.StartGame = pygame.Rect(50, 150, 50, 50)
        self.Text = font.render("Start Spel", True, (0,0,0))
     def Render(self, SURF):
        pygame.draw.rect(SURF, RED, self.rplayer, 0)
        SURF.blit(self.Text, (self.StartGame.x, self.StartGame.y))
    
class EndScreen:
    def __init__(self, font):
        self.RestartGame = pygame.Rect(50, 250, 50, 50)
        self.TextRestart = font.render("Game Over", True, (0,0,0))
        self.Text = font.render("Herstart Spel", True, (255,255,0))
     def Render(self, SURF):
        pygame.draw.rect(SURF, RED, self.RestartGame, 0)
        SURF.blit(self.TextRestart, (self.StartGame.x, self.StartGame.y))
        SURF.blit(self.Text, (50, 150))