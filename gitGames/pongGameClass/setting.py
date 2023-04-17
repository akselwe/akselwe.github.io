# game options/settings
import random

def tilfeldigFarge():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    nyFarge = (r,g,b)
    return nyFarge

def font(size):
    return pg.font.SysFont("Lucida Sans", size)

def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


TITLE = "MultiPong"
WIDTH = 1100
HEIGHT = 800
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHTBLUE = (0,0,150)
YELLOW = (255, 255, 0)

