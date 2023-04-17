import pygame
import random
import math
from pygame.locals import * 

# Initialiserer Pygame
pygame.init()

# Setter vinduets størrelse
window_size = (700, 400)
centerWidth = window_size[0] // 2
centerHeight = window_size[1] // 2

# Oppretter vinduet
screen = pygame.display.set_mode(window_size)

# Setter tittelen på vinduet
pygame.display.set_caption("Bouncing Ball")

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pygame.font.SysFont("Arial", 50)

WHITE = (255, 255, 255)
BLACK = (0,0,0)

space = True

class Padle:
    def __init__(self, x, y, b, h, color):
        self.x = x
        self.y = y
        self.b = b
        self.h = h
        self.color = color
        
        #hastighet på padlemovement
        self.speed = 0
        self.vy = self.speed
    
    #tegne rectangelent
    def draw(self):
        rect = pygame.Rect(self.x, self.y, self.b, self.h)
        pygame.draw.rect(screen, self.color, rect)
    
    #metode for å bevege figuren
    def move(self):
        self.y += self.vy
        if self.y + self.h >= window_size[1]:
            self.vy = 0
        if self.y <= 0:
            self.vy = 0
        
    

#klasse for ball
class Ball:
    def __init__(self, screen, color, center, r):
        self.screen = screen
        self.color = color
        self.center = center #tuple
        self.r = r
        
        #fart
        self.vx = 0
        self.vy = 4
    
    def draw(self):
        pygame.draw.circle(screen, self.color, self.center, self.r)
    
    def move(self):
        #oppdaterer posisjonen 
        self.center[0] += self.vx
        self.center[1] += self.vy
        
        #høyre
        if self.center[0] + self.r >= window_size[0]:
            self.vx = 0
            #self.vy = 0
            self.center[0] = window_size[0] - self.r
        #venstre
        if self.center[0] - self.r <= 0:
            self.vx = 0
            #self.vy = 0
            self.center[0] = self.r
            
        #bunn    
        if self.center[1] + self.r >= window_size[1]:
            self.vy *= -1
            self.center[1] = window_size[1] - self.r 
        #top 
        if self.center[1] - self.r <= 0:
            self.vy *= -1
            self.center[1] = self.r 



def keysPressed():
    randomXfart = [-4,4]
    
    # Henter en liste med status for alle tastatur-taster
    trykkede_taster = pygame.key.get_pressed()
    
    if trykkede_taster[K_UP] and padles[1].y >= 0:
        padles[1].y -= 5
    if trykkede_taster[K_DOWN] and padles[1].y + padles[1].h <= window_size[1]:
        padles[1].y += 5
    if trykkede_taster[K_w]:
        padles[0].y -= 5
    if trykkede_taster[K_s]:
        padles[0].y += 5
        
    if trykkede_taster[pygame.K_SPACE] and baller[0].vx == 0:
        baller[0].vx = random.choice(randomXfart)
        



#skriver tekst til vinduet
def tegnTekst(tekst, x, y, farge, fontSize):
    
    font = pygame.font.SysFont("Arial", fontSize)
    
    textImg = font.render(tekst, True, farge)
    
    surface.blit(textImg, (x - textImg.get_width()//2, y - textImg.get_height()//2))
    
    

def scoreBoard(ball):
    left = []
    right = []
    leftWinner = "Bokstaver vant!"
    rightWinner = "Piltaster vant!"
    gameOver = False
    
    if ball.center[0] + ball.r >= window_size[0]:
        left.append(1)
        ball.center = [window_size[0]/2, window_size[1]/2]
        ball.vx = 0
        
    if ball.center[0] - ball.r <= 0:
        right.append(1)
        ball.center = [window_size[0]/2, window_size[1]/2]
        ball.vx = 0
        
    if len(left) == 5:
        gameOver = True
        tegnTekst(leftWinner, centerWidth, centerHeight, WHITE, 60)
    if len(right) == 5:
        gameOver = True
        tegnTekst(rightWinner, centerWidth, centerHeight, WHITE, 60)
    
    score = font.render(str(len(left)), True, WHITE, BLACK)
    screen.blit(score, (100, 30))
    
    score = font.render(str(len(right)), True, WHITE, BLACK)
    screen.blit(score, (window_size[0]-100-score.get_width(), 30))
    
    
        
def tilfeldigFarge():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    nyFarge = (r,g,b)
    return nyFarge    


def collideLeft(ball, padle):
    if ball.center[0] - ball.r < padle.x + padle.b and ball.center[1] + ball.r > padle.y and ball.center[1] - ball.r < padle.y + padle.h:
        ball.vx *= -1.1
        ball.color = tilfeldigFarge()
    
     
    
def collideRight(ball, padle):
    if ball.center[0] + ball.r >= window_size[0] - padle.b and ball.center[1] + ball.r >= padle.y and ball.center[1] - ball.r <= padle.y + padle.h:
        ball.vx *= -1.1
        ball.color = tilfeldigFarge()
        

def kollisjon(ball, ball2):
    #pyt
    dist2 = (ball.center[0] - ball2.center[0])**2 + (ball.center[1] - ball2.center[1])**2
    dist = math.sqrt(dist2)


def drawBoard():
    b = 4
    h = 23
    for i in range(0,window_size[1], 30):
        line = pygame.Rect((window_size[0]/2)-(b/2), i, b, h)
        pygame.draw.rect(screen, WHITE, line)


   
        
#konstater
bg_color = (0, 0, 0) 
fps = 60

#ball
color = (100, 100, 255)
center = [window_size[0]/2, window_size[1]/2]
ball = Ball(screen, color, center, 13)


baller = [ball]

#padles
padleColor = (255, 255, 255)
padleLeft = Padle(5, 200, 30, 200, padleColor)
padleRight = Padle(window_size[0] - 30 - 5, 200, 30, 200, padleColor)

padles = [padleLeft, padleRight]



# Kjører spillets løkke
running = True
while running:
    # Setter fps
    pygame.time.Clock().tick(fps)

    #keysPressed()

    # Håndterer hendelser
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            color = tilfeldigFarge()
               

    # Tømmer skjermen
    screen.fill(bg_color)
    drawBoard()
    keysPressed()
    
    for i in range(len(padles)):
        padles[i].draw()
        padles[i].move()
        
    for i in range(len(baller)):
        baller[i].draw()
        baller[i].move()
        scoreBoard(baller[i])
    
    
    collideLeft(ball, padles[0])
    collideRight(ball, padles[1])  
        

    # Oppdaterer skjermbildet
    pygame.display.flip()

# Avslutter Pygame
pygame.quit()