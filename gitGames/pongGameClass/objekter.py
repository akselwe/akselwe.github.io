import pygame as pg
import pygame
import random
from setting import *
from random import randint as ran


class Rect:
    def __init__(self, x, y, b, h, color):
        self.x = x
        self.y = y
        self.b = b
        self.h = h
        self.color = color
        
        #hastighet på padlemovement
        self.vx = 5
        self.vy = 10
    
    def draw(self, screen):
        rect = pygame.Rect(self.x, self.y, self.b, self.h)
        pygame.draw.rect(screen, self.color, rect)
    
    def move(self):
        
        trykk = pg.key.get_pressed()
        if trykk[pg.K_LEFT] and self.x >= 0:
            self.x -= self.vx
        if trykk[pg.K_RIGHT] and self.x + self.b <= WIDTH:
            self.x += self.vx
  
class Ball:
    def __init__(self):
        self.r = ran(30,50)
        self.x = ran(0, WIDTH)
        self.y = 0
        self.center = [self.x, self.y]
        self.color = BLACK
        
        self.vx = 4
        self.vy = 8
        
    def draw(self, screen):
        pg.draw.circle(screen, self.color, self.center, self.r)
    
    def move(self):
        #oppdaterer posisjonen 
        self.center[0] += self.vx
        self.center[1] += self.vy
        
        #høyre
        if self.center[0] + self.r >= WIDTH:
            self.vx *= -1
            self.center[0] = WIDTH - self.r
            self.color = tilfeldigFarge()
        #venstre
        if self.center[0] - self.r <= 0:
            self.vx *= -1
            self.center[0] = self.r
            self.color = tilfeldigFarge()
        #bunn    
        if self.center[1] + self.r >= HEIGHT:
            self.vy *= -1
            self.center[1] = HEIGHT - self.r 
        #top 
        if self.center[1] - self.r <= 0:
            self.vy *= -1
            self.center[1] = self.r 