import random
import pygame
from pygame.locals import *
from sys import exit

print("Welcome to your new house!")
print("To open the door press the 0 key")
print("To have the sun, press the 1 key")
print("To close the door and make it night time, press the 2 key")
print("To open the windows, press the 3 key")
print("To grow a tree, press the 4 key")

def drawHouse(background):
    pygame.draw.rect(background, (232, 193, 116), (250,250,500,525))
    pygame.draw.polygon(background, (235, 145, 110), ((250,250), (450,0), (640, 250)))
    pygame.draw.circle(background, (174, 241, 245), (450,150), 55)
    pygame.draw.rect(background, (138, 91, 37),(100, 380, 30, 170))
    pygame.draw.line(background, (0, 0, 0),(450, 100),(450,205),(3))
    pygame.draw.line(background, (0,0,0),(400,150),(500,150),(3))
    pygame.draw.polygon(background, (80, 199, 78), ((70,380), (150,380), (140, 150)))
    pygame.draw.rect(background, (224, 160, 49),(400, 380, 60, 170))
    pygame.draw.circle(background, (135, 99, 27), (413,417), 5)
    pygame.draw.circle(background, (255, 255, 255), (140, 100), 25)
    pygame.draw.circle(background, (255, 255, 255), (160, 120), 25)
    pygame.draw.circle(background, (255, 255, 255), (180, 100), 25)
    pygame.draw.circle(background, (255, 255, 255), (190, 120), 25)
    pygame.draw.circle(background, (255, 255, 255), (210, 100), 25)
    pygame.draw.rect(background, (255, 255, 255),(280, 310, 70, 70))
    pygame.draw.rect(background, (235, 145, 110),(280, 310, 70, 58))
    pygame.draw.rect(background, (255, 255, 255),(520, 310, 70, 70))
    pygame.draw.rect(background, (235, 145, 110),(520, 310, 70, 58))
    


def rain(background):
    for i in range(50):
        x = random.randint(1,639)
        y = random.randint(1,479)
        pygame.draw.line(background, (132, 161, 224),(x, y),(x+30,y+30),(3))
    

def openDoor(background):
    pygame.draw.rect(background, (255, 255, 255),(400, 380, 60, 170))
    pygame.draw.rect(background, (224, 160, 49),(460, 380, 60, 170))
    pygame.draw.circle(background, (135, 99, 27), (505,420), 5)
    


def make_sun(background):
    background.fill(SKY_COLOR)
    pygame.draw.circle(background, (240, 207, 24), (50,30), 35)

def moon(background):
    background.fill(NIGHT_COLOR)
    pygame.draw.circle(background, (255, 255, 255), (50,30), 35)

def window(background):
    pygame.draw.rect(background, (255, 255, 255),(280, 310, 70, 70))
    pygame.draw.rect(background, (235, 145, 110),(280, 310, 70, 20))
    pygame.draw.rect(background, (255, 255, 255),(520, 310, 70, 70))
    pygame.draw.rect(background, (235, 145, 110),(520, 310, 70, 20))

def growtree(background):
    pygame.draw.polygon(background, (110, 199, 78), ((140,380), (220,380), (210, 150)))
    pygame.draw.rect(background, (138, 91, 37),(170, 380, 30, 170))
    




#add functions here

#color VARS
SKY_COLOR = (170, 226, 240)
NIGHT_COLOR = (45, 87, 179)


pygame.init()
background=pygame.display.set_mode((640, 480))
background.fill(SKY_COLOR)
drawHouse(background)
pygame.display.update()

while True:
    f_openDoor = False
    f_make_sun = False
    f_moon = False
    f_window = False
    f_growtree = False
    f_rain = False
    # add flags here
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit
        elif event.type == pygame.KEYDOWN:
            # User presses ESCAPE-Key
            if event.key == pygame.K_ESCAPE:
                mainloop = False
            if event.key == pygame.K_0:
                f_openDoor = True
            if event.key == pygame.K_1:
                f_make_sun = True
            if event.key == pygame.K_2:
                f_moon = True
            if event.key == pygame.K_3:
                f_window = True
            if event.key == pygame.K_4:
                f_growtree = True
            if event.key == pygame.K_5:
                f_rain = True
            
            # add if statements
               
    if f_openDoor:
        openDoor(background)
        pygame.display.update()

    if f_make_sun:
        make_sun(background)
        drawHouse(background)
        pygame.display.update()

    if f_moon:
        moon(background)
        drawHouse(background)
        pygame.display.update()

    if f_window:
        window(background)
        pygame.display.update()

    if f_growtree:
        growtree(background)
        pygame.display.update()

    if f_rain:
        rain(background)
        pygame.display.update()
        
        
    # add checks

