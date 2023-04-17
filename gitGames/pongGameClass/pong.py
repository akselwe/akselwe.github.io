# Jumpy! (a platform game) - Part 1
# Video link: https://www.youtube.com/watch?v=uWvb3QzA48c

import pygame as pg
import pygame
import random
from setting import *
from objekter import *
from random import randint as ran


class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font = 'arial'
        
        self.lives = 0 
        self.go = False
        
        self.baller = []
        

    def new(self):
        # start a new game
        
        #for i in range(6):
            #self.ball = Ball()
            #self.baller.append(self.ball)
        
        self.ball = Ball()
        self.padle = Rect(WIDTH - 400, HEIGHT - 40, 300, 20, RED)
        self.run()


    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            

    def update(self):
        
        self.padle.move()
        
        #for ball in self.baller:
         #   self.ball.move()
          #  self.kollisjon(ball, self.padle)
          
        self.ball.move()
        self.kollisjon(self.ball, self.padle)

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # Game Loop - draw
        self.screen.fill(WHITE)
        
        #for ball in self.baller:
          #  self.ball.draw(self.screen)
        
        self.ball.draw(self.screen)
        self.padle.draw(self.screen)
        
        # *after* drawing everything, flip the display
        pg.display.flip()
    
    def kollisjon(self, ball, rect):
        
        if ball.center[1] + ball.r >= HEIGHT:
            self.lives += 1
        
        #sjekker game over
        if self.lives >= 3:
            self.playing = False
        
        #for ball in self.baller:
        if ball.center[1] + ball.r >= rect.y and ball.center[0] + ball.r >= rect.x and ball.center[0] - ball.r <= rect.x + rect.b:
            ball.vy *= -1
            ball.color = tilfeldigFarge()
        

    
    def show_start_screen(self):
        # game start screen
        self.screen.fill(LIGHTBLUE)
        self.drawtext(TITLE, 80, WHITE, WIDTH//2, HEIGHT//4)
        self.drawtext("Arrows to move", 40, WHITE, WIDTH//2, HEIGHT//2)
        self.drawtext("You die if 10 balls go of the screen", 40, WHITE, WIDTH//2, HEIGHT*3/4)
        
        pg.display.flip()
        self.wait()
        
        

    def show_go_screen(self):
        
        if not self.running:
            return
        
        # game over/continue
        self.screen.fill(LIGHTBLUE)
        self.drawtext("GAME OVER", 80, WHITE, WIDTH//2, HEIGHT//4)
        self.drawtext("Score: ", 40, WHITE, WIDTH//2, HEIGHT//2)
        self.drawtext("10 balls went off the screen", 40, WHITE, WIDTH//2, HEIGHT*3/4)
        
        pg.display.flip()
        self.wait()
    
    def drawtext(self, text, size, color, x, y):
        font = pg.font.SysFont(self.font, size)
        textSurface = font.render(text, True, color)
        textRect = textSurface.get_rect()
        textRect.midtop = (x,y)
        self.screen.blit(textSurface, textRect)
    

    def wait(self):
        wait = True
        while wait:
            self.clock.tick(FPS)
            for event in pg.event.get():
            # check for closing window
                if event.type == pg.QUIT:
                    wait = False
                    self.running = False
                if event.type == pg.KEYUP:
                    wait = False
            


g = Game()
g.show_start_screen()

while g.running:
    g.new()
    g.show_go_screen()

pg.quit()


