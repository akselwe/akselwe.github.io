import pygame
import pygame as pg
import sys
from pygame.locals import *
from os import listdir
from os.path import isfile, join
from random import randint as ran
from settings import *

# Initialiserer Pygame
pg.init()

# Oppretter vinduet
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
size = screen.get_size()

# Setter tittelen på vinduet
pg.display.set_caption("Bouncing Ball")

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.SysFont("Arial", 50)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 0, 255)

#player variables 
start = 150
PLAYER_xVEL = 10

#Game variabels
playerSize = 70 
MaxPlatforms = 10

def flip(sprites):
    return [pg.transform.flip(sprite, True, False) for sprite in sprites]

def loadSpriteSheets(dir1, dir2, width, height, direction = False):
    path = join("bilder", dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]
    
    allSprites = {}
    
    for image in images:
        #convert_alpha() gjør d mulig å transparent bilder
        spriteSheet = pg.image.load(join(path, image)).convert_alpha()
        
        #få alle spritene alene 
        sprites = []
        for i in range(spriteSheet.get_width() // width):
            surface = pg.Surface((width, height), pg.SRCAPLHA, 32)
            rect = pg.Rect(i * width, 0, width, height)
            surface.blit(spriteSheet, (0,0), rect)
            sprites.append(pg.transform.scale2x(surface))
        
        if direction:
            allSprites[image.replace(".png", "") + "_right"] = sprites
            allSprites[image.replace(".png", "") + "_left"] = flip(sprites)
        else:
            allSprites[image.replace(".png", "")] = sprites
    
    return allSprites

#backgroundImg
backgroundImg = pg.image.load('bilder/sky1.png').convert_alpha()
backgroundImg = pg.transform.scale(backgroundImg, size)
rect = pygame.Rect(size[0]/2 - 10, 0, 20, size[1])


#playerImg 
playerImg = pg.image.load('bilder/jump.png').convert_alpha()

#platformImg
platformImg = pg.image.load('bilder/platform.png').convert_alpha()
platformImg = pg.transform.scale(platformImg, (400, 400))


class Player:
    def __init__(self, x, y, width, height):
        self.rect = pg.Rect(x, y, width, height)
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        
        #fart
        self.x_vel = 0
        self.y_vel = 0
        self.ay = 0.9
    
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
    
    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0
    
    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0
        
    def loop(self, fps):
        self.move(self.x_vel, self.y_vel)
    
    def draw(self):
        pg.draw.rect(screen, BLACK, self.rect)
    
    def update(self):
        # Bevegelseslikninger
        self.y_vel += self.ay
        self.rect.y += self.y_vel + 0.5 * self.ay

        # Sjekker kollisjon med bakken
        if self.rect.y + self.rect.height >= size[1] - start:
            self.rect.y = size[1] - self.rect.height - start
        
    def jump(self):
        self.y_vel = -20

leftPlayer = Player(size[0]//4, size[1] - start, playerSize, playerSize)
rightPlayer = Player(size[0]*3/4, size[1] - start, playerSize, playerSize)


def handle_move():
    key = pg.key.get_pressed()
    
    
    rightPlayer.x_vel = 0
    if key[pg.K_LEFT]:
        rightPlayer.move_left(PLAYER_xVEL)
    if key[pg.K_RIGHT]:
        rightPlayer.move_right(PLAYER_xVEL)
    
    leftPlayer.x_vel = 0
    if key[pg.K_a]:
        leftPlayer.move_left(PLAYER_xVEL)
    if key[pg.K_d]:
        leftPlayer.move_right(PLAYER_xVEL)


running = True
FPS = 60
while running:
    pg.time.Clock().tick(FPS)
    
    #tegne bakgrunn
    screen.blit(backgroundImg, (0, 0))
    pygame.draw.rect(screen, BLACK, rect)
    
    # Håndterer hendelser
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
                pg.quit()
                sys.exit()
            if event.key == pg.K_w:
                leftPlayer.jump()
            if event.key == pg.K_UP:
                rightPlayer.jump()
                
    leftPlayer.loop(FPS)
    rightPlayer.loop(FPS)
    handle_move()
    
    
    #karrakter
    leftPlayer.update()
    leftPlayer.draw()
    rightPlayer.update()
    rightPlayer.draw()
    
    
    
    #Oppdaterer skjermbildet
    pg.display.flip()    
    
pg.quit()