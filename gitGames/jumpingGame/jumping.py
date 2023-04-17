import pygame as pg

# Initialiserer Pygame
pygame.init()

# Oppretter vinduet
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Setter tittelen på vinduet
pygame.display.set_caption("Bouncing Ball")

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pygame.font.SysFont("Arial", 50)

WHITE = (255, 255, 255)
BLACK = (0,0,0)