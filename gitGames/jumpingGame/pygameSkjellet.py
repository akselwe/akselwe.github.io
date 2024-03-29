# Pygame template - skeleton for a new pygame project
import pygame
import random

WIDTH = 700
HEIGHT = 800
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen1 = pygame.display.set_mode((WIDTH, HEIGHT))
screen2 = pygame.display.set_mode((WIDTH/2, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw / render
    screen1.fill(BLACK)
    screen2.fill(RED)
    
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()