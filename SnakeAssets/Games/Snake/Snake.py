import os #Imports os, must be imported before pygame
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" #Hides the pygame start message
import pygame       #imports the pygame library
import random
import sys

pygame.init() #starts pygame
pygame.display.set_caption("Snake") #names the window
pygame.event.set_allowed(pygame.QUIT)
clock=pygame.time.Clock()

width= 500 #Sets the screen width
height=600 #Sets the screen height
screen = pygame.display.set_mode((width,height)) #sets screen size

font=pygame.font.SysFont("arial",30) #sets the font

def fps():
    text = font.render(str(int(clock.get_fps())),True,(255,255,255)); screen.blit(text,(472,500)) #sets the text to render

def score():
    global high
    font=pygame.font.SysFont("arial",50)
    if len(snake)-1>=high: high=len(snake)-1 #increases highscore
    text = font.render("Score: "+str(len(snake)-1),True,(255,255,255)); screen.blit(text,(10,520)) #score
    text = font.render("High: "+str(high),True,(255,255,255)); screen.blit(text,(230,520)) #highscore
    
def inputs():
    global keys
    global d
    keys = pygame.key.get_pressed()

    for event in pygame.event.get(): #ensures player can always close pygame
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if keys[pygame.K_w] or keys[pygame.K_UP]:
        d=1

    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        d=-1

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        d=2

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        d=-2

def foodpos(): #generates random food posiotion
    global fx,fy,px,py
    fx=random.randint(0,24); fy=random.randint(0,24)
    while (fx,fy) in snake: fx=random.randint(0,24); fy=random.randint(0,24) #ensures food will never spawn on player

def food():
    global fx, fy, px, py
    if (fx,fy)==(px,py): foodpos(); snake.append((px,py)) #new food pos and increase player length
    pygame.draw.rect(surface=screen,color=(255,0,0),rect=(20*fx,20*fy,20,20),width=0)

def player(): #handles player render
    global px,py
    global fx,fy
    global d, od, timer
    global snake
    timer+=1

    if timer==10: #only update square pos every set amount of runs
        timer=0 #reset timer for next update
        if abs(od)==abs(d): d=od #prevent player from moving backwards
        od=d
        if d==1: py-=1 #check if player is moving up
        elif d==-1: py+=1 #down
        elif d==2: px+=1 #right
        elif d==-2: px-=1 #left
        snake.pop(len(snake)-1) #removes the last item from the list
        snake.insert(0,(px,py)) #adds the current player pos to the list
        if px<0 or py<0 or px>24 or py>24 or snake.count((px,py))>1: px=12; py=12; d=0; snake=[(px,py)]; foodpos()#resets game if player is outside of the grid
    sc=0
    for z in range(0,len(snake)):
        sc+=0.408
        x=snake[z][0]; y=snake[z][1]
        pygame.draw.rect(surface=screen,color=(sc,sc,255),rect=(20*x,20*y,20,20),width=0) #renders the player

def gridLines(): #renders the grid
    l=0
    while l<500:
        l+=20
        pygame.draw.line(surface=screen,color=(55,55,55),width=1,start_pos=(0,l),end_pos=(500,l)) #horizontal lines
        pygame.draw.line(surface=screen,color=(55,55,55),width=1,start_pos=(l,0),end_pos=(l,500)) #vertical lines

px=12; py=12 #init player position
snake=[(px,py)] #init snake list
high=0 #init highscore
foodpos() #init food position
d=0; od=0; timer=0 #init player movement and direction
while True:
    screen.fill((0,125,0)) #clears screen
    pygame.draw.rect(surface=screen,color=(0,0,0),rect=(0,500,width,height-500),width=0) #renders the player
    inputs() #tracks player inputs
    food() #renders food
    player() #renders the player
    gridLines() #renders the grid
    score()
    clock.tick(60) #limits the fps to 60fps
    fps() #adds an fps counter to the corner of the screen
    pygame.display.update() #Updates the screen