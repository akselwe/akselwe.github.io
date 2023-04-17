#homescreen
import pygame
import pygame as pg
import sys 
import settings

pg.init()

# Oppretter vinduet
screen = pg.display.set_mode((WIDTH, HEIGHT))
size = screen.get_size()

# Setter tittelen på vinduet
pg.display.set_caption("WEDSET AND RIDDER")

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.SysFont("Arial", 50)

running = True
while running:
    pg.time.Clock().tick(FPS)
    
    # Håndterer hendelser
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
                pg.quit()
                sys.exit()
    
    pg.display.update()
    
pg.quit()