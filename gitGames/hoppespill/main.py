import pygame, sys, time, random
import pygame as pg
from pygame.locals import *
from random import randint as ran
from spriteSheet import SpriteSheet
from enemy import *
from settings import *

pg.init()

screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
size = screen.get_size() #[x,y]
scrollLine = size[1]/2


#backgroundImg
backgroundImg = pg.image.load('bilder/sky1.png').convert_alpha()
backgroundImg = pg.transform.scale(backgroundImg, size)
player1Img = pg.image.load('bilder/jumpy3.png').convert_alpha()
player2Img = pg.image.load('bilder/jumpy2.png').convert_alpha()
platformImg = pg.image.load('bilder/wood.png').convert_alpha()
birdpics = pg.image.load('bilder/bird.png').convert_alpha()
birdsheet = SpriteSheet(birdpics)


#sounds
pg.mixer.music.load('music/loop3.mp3')
pg.mixer.music.set_volume(0.2)
pg.mixer.music.play(loops = -1)
jumpSound = pg.mixer.Sound('music/slime_jump.mp3')
jumpSound.set_volume(0.2)
#deathsound = pg.mixer.Sound('music/Death.mp3')
#deathsound.set_volume(0.2)




class Box:
    def __init__(self, x, y, b, h, color):
        self.x = x
        self.y = y
        self.b = b
        self.h = h
        self.color = color
    
    def draw(self):
        rect = pygame.Rect(self.x, self.y, self.b, self.h)
        pygame.draw.rect(screen, self.color, rect)
        
linje1 = Box(size[0]/2 - lineWidth/4, 0, lineWidth/2, 40, LIGHTBLUE)
linje2 = Box(size[0]/2 - lineWidth/4, 110, lineWidth/2, size[1], LIGHTBLUE)


class Player:
    def __init__(self, x, y, img):
        self.img = pg.transform.scale(img, (playerSize, playerSize * 1.3))
        self.width = playerSize - 25
        self.height = playerSize*2 - 55
        self.rect = pg.Rect(0, 0, self.width, self.height)
        self.rect.center = (x,y)
        self.rect.x = x
        self.rect.y = y
        self.flip = False
        self.jumpcount = 0
        self.gameOver = False
        
        #fart
        self.vx = 10
        self.vy = 0
        self.ay = 1.1
        
    
    def draw(self):
        screen.blit(pygame.transform.flip(self.img, self.flip, False), (self.rect.x - 15, self.rect.y - 14))
        #pg.draw.rect(wscreen, RED, self.rect, 2)
        
    def update(self):
        scroll = 0
        
        if abs(self.vy) > 30:
            self.vy = 30
        
        # Bevegelseslikninger
        self.vy += self.ay 
        self.rect.y += self.vy + 0.5 * self.ay
        
        #scroll
        if self.rect.y <= scrollLine:
            self.rect.y = scrollLine
            if self.vy < 0:
                scroll = -self.vy
        
        
        for i in range(2):
            #platform colisjon (bare bunn)
            for platform in platformGroups[i]:
                #y retning
                if platform.rect.colliderect(self.rect.x, self.rect.y, self.width, self.height):
                    if self.vy > 0:
                        self.rect.y = platform.rect.y - self.rect.height
                        self.vy = 0
                        self.jumpcount = 0
        
        #mask - pixel perfect collision
        self.mask = pg.mask.from_surface(self.img)
 
 
        return scroll
    
    
    def jump(self):
        if self.jumpcount <= 1:
            jumpSound.play()
            self.vy = -20


#players
leftPlayer = Player(size[0]//4, size[1] - start, player1Img)
rightPlayer = Player(size[0]*(3/4), size[1] - start, player2Img)
players = [leftPlayer, rightPlayer]


            
            

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, width, moving):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(platformImg, (width, 20))
        self.moving = moving
        self.moveCount = ran(0,50)
        self.direction = random.choice([-1, 1])
        self.spid = ran(1,2)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self, scroll):
        #bevegende platformer
        if self.moving == True:
            self.moveCount += 1
            self.rect.x += self.direction * self.spid
        
        #changing direction
        if self.moveCount >= 300:
            self.direction *= -1
            self.moveCount = 0
        
        self.rect.top += scroll
        
        if self.rect.top >= size[1]:
            self.kill()
            
            
#platform grupper med startplatform
platformGroup = pg.sprite.Group()
platformGroup2 = pg.sprite.Group()
platform = Platform(size[0]/4-150, size[1] - start, 300, False)
platform2 = Platform(size[0]*3/4-150, size[1] - start, 300, False)
platformGroup.add(platform)
platformGroup2.add(platform2)
platformGroups = [platformGroup, platformGroup2]



#enemies enemy.py
enemyGroup = pg.sprite.Group()
enemyGroup2 = pg.sprite.Group()
enemyGroups = [enemyGroup, enemyGroup2]





def font(size):
    return pg.font.SysFont("Lucida Sans", size)

def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def changePlatDir(group):
    if group == platformGroup:
        group = platformGroup
        left = 0
        right = size[0]/2 - lineWidth
    else:
        group = platformGroup2
        left = size[0]/2
        right = size[0]
    for platform in group:
        if platform.rect.left < left or platform.rect.right > right:
            platform.direction *= -1


def drawScore(score, x):
    draw_text("Score: " + str(score), font(40), BLUE, x, 50)
    
    
def gameOverScreen():
    screen.blit(backgroundImg, (0, 0))
    margin = 150
    rect = Rect(0 + margin, 0 + margin, size[0] - margin*2, size[1] - margin*2)
    pg.draw.rect(screen, BLUE, rect, 0, 20)
    draw_text("GAME OVER", font(130), LIGHTBLUE, size[0]/2 - 300, size[1]/2 - 200)
    draw_text(str(winner), font(140), WHITE, size[0]/2 - 470, size[1]/2 - 20)

        
def checkWinner(leftScore, rightScore):
    if leftScore > rightScore:
        winner = "LEFT PLAYER WON"
    elif rightScore > leftScore:
        winner = "RIGHT PLAYER WON"
    else:
        winner = "NO WINNER. DRAW"
    return winner


def moveX():
    pressed = pg.key.get_pressed()
    #left
    if pressed[K_a] and leftPlayer.rect.x > 0:
        leftPlayer.rect.x -= leftPlayer.vx
        leftPlayer.flip = True
    if pressed[K_d] and leftPlayer.rect.x < size[0]/2 - leftPlayer.width - (lineWidth - 9):
        leftPlayer.rect.x += leftPlayer.vx
        leftPlayer.flip = False
    #right
    if pressed[K_LEFT] and rightPlayer.rect.x > size[0]/2 + lineWidth/2:
        rightPlayer.rect.x -= rightPlayer.vx
        rightPlayer.flip = True
    if pressed[K_RIGHT] and rightPlayer.rect.x < size[0] - (rightPlayer.width + 7):
        rightPlayer.rect.x += rightPlayer.vx
        rightPlayer.flip = False
        

t1 = pg.time.get_ticks()
def timer(sek, font, color, x, y):
    t2 = pg.time.get_ticks()
    dt = (t2-t1)/1000
    total_seconds = int(round(sek - dt,0))
    seconds = total_seconds % 60
    sekund = "{0:00}".format(seconds)
    draw_text(str(sekund), font, color, x, y)
    
    return total_seconds
    

def checkGameOver(player, enemygroup, score):
    
    if player.rect.top >= size[1]:
        player.rect.top = size[1] + 400
        score = 0
        player.gameOver = True
    
    if pg.sprite.spritecollide(player, enemygroup, False):
        if pg.sprite.spritecollide(player, enemygroup, False, pg.sprite.collide_mask):
            player.rect.top = size[1] + 400
            score = 0
            player.gameOver = True
            
    return score


def background():
    screen.blit(backgroundImg, (0, 0))
    linje1.draw()
    linje2.draw()


def makeEnemy(group, score, xlim, ylim):
    global maks 
    if score >= lvls[3]:
        maks = 2
    if len(group) <= maks and score >= lvls[2]:
        enemy = Enemy(xlim, ylim, random.choice([-400, -200, 0, 200]), birdsheet, 2.5)
        group.add(enemy)

def updateHighscore():
    for score in scores:
        if score > highscore:
            highscore = score
            with open('highscore.txt', 'w') as file:
                file.write(str(highscore))


def platformMaker():
    global platform, platform2
    if len(platformGroup) < MaxPlatforms:
        p_b = ran(100,200)
        p_x = ran(0, size[0]/2 - p_b)
        p_y = platform.rect.y - ran(250,300)
        p_type = ran(1,2)
        if p_type == 1 and scores[0] >= 1:
            p_moving = True
        else:
            p_moving = False
        platform = Platform(p_x, p_y, p_b, p_moving)
        platformGroup.add(platform)

    if len(platformGroup2) < MaxPlatforms:
        p_b = ran(100,200)
        p_x = ran(size[0]/2, size[0] - p_b)
        p_y = platform2.rect.y - ran(250,300)
        p_type2 = ran(1,2)
        if p_type2 == 1 and scores[1] >= 1:
            p_moving2 = True
        else:
            p_moving2 = False
        platform2 = Platform(p_x, p_y, p_b, p_moving2)
        platformGroup2.add(platform2)




while running:
    
    pg.time.Clock().tick(fps)
    if leftPlayer.gameOver == False or rightPlayer.gameOver == False:
        
        background()

        #timer
        sek = timer(40, font(80), BLUE, size[0]/2 - 35, 50)
        if sek <= 0:
            leftPlayer.gameOver = True
            rightPlayer.gameOver = True
        
        platformMaker()
        
        #lagre update som scroll for å ha variabelen til å sjekke scrolling på skjermen (player.update() returnerer scroll)
        leftScroll = leftPlayer.update()
        rightScroll = rightPlayer.update()
        scrolls = [leftScroll, rightScroll]
        
        moveX()
        
        for i in range(2):
            players[i].draw()
            platformGroups[i].update(scrolls[i])
            platformGroups[i].draw(screen)
            changePlatDir(platformGroups[i])
            enemyGroups[i].draw(screen)
            
            if scrolls[i] > 0:
                scores[i] += int(scrolls[i]//10)
        

        drawScore(scores[0], 50)
        drawScore(scores[1], size[0] - 200)
        
        makeEnemy(enemyGroup, scores[0], 0, size[0]/2)
        makeEnemy(enemyGroup2, scores[1], size[0]/2, size[0])
        enemyGroup.update(scrolls[0], 0, size[0]/2)
        enemyGroup2.update(scrolls[1], size[0]/2, size[0])
       
        
        scores[0] = checkGameOver(leftPlayer, enemyGroup, scores[0])
        scores[1] = checkGameOver(rightPlayer, enemyGroup2, scores[1])
        

        # Håndterer hendelser
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
                    pg.quit()
                    sys.exit()
                if event.key == pg.K_UP:
                    rightPlayer.jump()
                    rightPlayer.jumpcount += 1
                if event.key == pg.K_w:
                    leftPlayer.jump()
                    leftPlayer.jumpcount += 1
         
        
        #highscoreline
        '''
        if scores[0] > scores[1]:
            s = scores[0]
        else:
            s = scores[1]
        
        pg.draw.line(screen, WHITE, (0, s - highscore + scrollLine), (size[0], s - highscore + scrollLine), 3)
        '''
        '''
        
        for score in scores:
            if score > highscore:
                highscore = score
        with open('highscore.txt', 'w') as file:
            file.write(str(highscore))
        '''    
        
        
    else:
        #sjekk vinner
        winner = checkWinner(scores[0], scores[1])
        gameOverScreen()

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
                    pg.quit()
                    sys.exit()
                    

    pg.display.flip()    
    
pg.quit()
