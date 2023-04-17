import random, sys
import pygame as pg

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


#farger RGB
GREEN = (0, 200, 0)
RED = (200, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


pg.init()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption('TicTacToe')

#font
font = pg.font.SysFont("Arial", 80)
font2 = pg.font.SysFont("Arial", 40)

line_width = 12
def grid():
    BG = (255, 255, 255)
    GRID = (30, 30, 30)
    screen.fill(BG)
    
    for x in range(1,3):
        pg.draw.line(screen, GRID, (0, x * 200), (SCREEN_WIDTH, x * 200), line_width)
        pg.draw.line(screen, GRID, (x * 200, 0), (x * 200, SCREEN_HEIGHT), line_width)


markers = []
klikket = False
pos = []
spiller = 1
vinner = 0
game_over = False
antallTrykk = 0

#slik skal vi bytte ut verdier i en liste av lister (grid):
#    [
#    [0,0,0]
#    [0,0,0]
#    [0,0,0]
#    ]
def behind_grid():
    for x in range(3):
        rad = [0] * 3
        markers.append(rad)
behind_grid()

def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pg.draw.line(screen, GREEN, (x_pos * 200 + 30, y_pos * 200 + 30), (x_pos * 200 + 170, y_pos * 200 + 170), line_width)
                pg.draw.line(screen, GREEN, (x_pos * 200 + 30, y_pos * 200 + 170), (x_pos * 200 + 170, y_pos * 200 + 30), line_width)
            if y == -1:
                pg.draw.circle(screen, RED, (x_pos * 200 + 100, y_pos * 200 + 100), 68, line_width)
            
            y_pos += 1
        x_pos += 1
        
        
def sjekk_vinner():
    
    global vinner
    global game_over
    y_pos = 0
    
    #sjekker uavgjort
    if antallTrykk == 9:
        vinner = 3
        game_over = True
    
    for x in markers:
        
        #sjekke loddrett radene 
        if sum(x) == 3:
            vinner = 1
            game_over = True
        
        if sum(x) == -3:
            vinner = 2
            game_over = True
        
        #sjekker vanrette radene
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == 3:
            vinner = 1
            game_over = True
        
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == -3:
            vinner = 2
            game_over = True
        
        y_pos += 1
        
    
    #sjekk kryss 
    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[2][0] + markers[1][1] + markers[0][2]== 3:
        vinner = 1
        game_over = True
        
    if markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[2][0] + markers[1][1] + markers[0][2]== -3:
        vinner = 2
        game_over = True
    
    
def draw_vinner(vinner):
    global vinner_rect
    global omstart_rect
    
    vinner_str = ""
    if vinner == 3:
        vinner_farge = BLACK
        vinner_str = "Uavgjort" 
    elif vinner == 2:
        vinner_farge = RED
        vinner_str =  "Sirkel vant!"
    elif vinner == 1:
        vinner_farge = GREEN
        vinner_str = "Kryss vant!"
    
    omstart = "Start på nytt"
    omstart_img = font2.render(omstart, True, BLACK)
    winimg = font.render(vinner_str, True, vinner_farge)
    
    #rektangler til vinner og spill igjen
    vinner_rect = pg.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
    omstart_rect = pg.Rect((screen.get_width() - omstart_img.get_width())/2, (screen.get_height() - omstart_img.get_height())/2 + 50, omstart_img.get_width(), omstart_img.get_height())

    pg.draw.rect(screen, WHITE, vinner_rect)
    pg.draw.rect(screen, WHITE, omstart_rect)
    
    #sentrere tekst
    #screen.blit(winimg, winimg.get_rect(center = screen.get_rect().center))
    screen.blit(winimg, ((screen.get_width() - winimg.get_width())/2, (screen.get_height() - winimg.get_height())/2 - 50))
    screen.blit(omstart_img, ((screen.get_width() - omstart_img.get_width())/2, (screen.get_height() - omstart_img.get_height())/2 + 50))
    
            
running = True
while running:
    
    grid()
    draw_markers()
    
    #eventhandlers
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        #rute-trykker-lytter, så lenge game_over ikke er et faktum (1)
    
        if game_over == False:
            
            if event.type == pg.MOUSEBUTTONDOWN and klikket == False:
                klikket = True
            if event.type == pg.MOUSEBUTTONUP and klikket == True:
                klikket = False
                #posisjonen til klikket
                pos = pg.mouse.get_pos()
                rute_x = pos[0]
                rute_y = pos[1]
                #posisjonen til markøren som tegnes med draw_markers()
                #floor divisjon (rund ned for å få hele tall)
                if markers[rute_x // 200][rute_y // 200] == 0:
                    markers[rute_x // 200][rute_y // 200] = spiller
                    spiller *= -1
                    antallTrykk += 1
                    
                    sjekk_vinner()
            
    if game_over == True:
        draw_vinner(vinner)
        
        if event.type == pg.MOUSEBUTTONDOWN and klikket == False:
            klikket = True
        if event.type == pg.MOUSEBUTTONUP and klikket == True:
            klikket = False
            pos = pg.mouse.get_pos()
                    
            if omstart_rect.collidepoint(pos):
                markers = []
                pos = []
                spiller = 1
                vinner = 0
                game_over = False
                antallTrykk = 0
                behind_grid()
                
    pg.display.update()
            

pg.quit()
