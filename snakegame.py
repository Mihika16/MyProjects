import pygame
import random
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode([600,600])
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
yellow=(255,255,0)
screen.fill(yellow)
foodx=random.randint(0,600)//10*10 
foody=random.randint(0,600)//10*10
#snakexandsnakey together are head of snake
snakex=random.randint(0,600)//10*10 
snakey=random.randint(0,600)//10*10
upkey=0
donkey=0
rightkey=0
leftkey=0
clock=pygame.time.Clock()
snakelist=[]
snakelist.append([snakex,snakey])
score=0
def show_text(msg,x,y,colour):
   fontobj=pygame.font.SysFont("Papyrus",35)
   msgobj=fontobj.render(msg,True,colour)
   screen.blit(msgobj,(x,y))
   
while True:
   show_text(str(score), 50,50, white)
   snakelist.insert(0,[snakex,snakey])
   snakelist.pop()
   clock.tick(20)
   for segment in snakelist:
       pygame.draw.rect(screen,red,segment+[10,10])
   pygame.draw.rect(screen, black, (foodx, foody, 10,10))
   pygame.display.update()
   for event in pygame.event.get():
       
       if event.type==KEYDOWN:
           if event.key==K_UP and donkey==0: 
               upkey=1
               donkey=0
               rightkey=0
               leftkey=0
           if event.key==K_DOWN and upkey==0:
               donkey=1
               upkey=0
               rightkey=0
               leftkey=0
           if event.key==K_RIGHT and leftkey==0:
               rightkey=1
               leftkey=0
               upkey=0
               donkey=0
           if event.key==K_LEFT and rightkey==0:
               leftkey=1
               rightkey=0
               upkey=0
               donkey=0
       if event.type==QUIT:
           pygame.quit()
           exit()
   screen.fill(yellow)
   if upkey==1:
       snakey=snakey-10
   if donkey==1:
       snakey=snakey+10
   if rightkey==1:
       snakex=snakex+10
   if leftkey==1:
       snakex=snakex-10
       
   if[snakex,snakey] in snakelist[1:]:
       print("GAME OVER")
       pygame.display.update()
       break 

   if snakex==foodx and snakey==foody:
       print("Da snake ate da food!!!!!!!!!!!!!")
       foodx=random.randint(0,600)//10*10
       foody=random.randint(0,600)//10*10
       snakelist.append([snakex,snakey])
       print(snakelist)
       score=score+1
       print(score)

   if snakex==600:
       snakex=10
   if snakey==600:
       snakey=10
   if snakex==0:
       snakex=590
   if snakey==0:
       snakey=590
    
