import pygame
from pygame.locals import *
import math

from random import randint
from gameobjects.vector2 import Vector2
SCREEN_SIZE=(640,480)
LOCATION=(0,0)
TXT_HEIGHT=20

class Character(object):
    
    def __init__(self,name):
        self.name=name
        self.level=0
        self.exp=0
        
    def render(self,surface):
        font=pygame.font.SysFont("courier new",16,True)
        nameTxt=font.render(self.name,True,(0,0,0))
        levelTxt=font.render("level is "+str(self.level),True,(0,0,0))
        expTxt=font.render("exp is " +str(self.exp-2**self.level),True,(0,0,0))
        surface.blit(nameTxt,LOCATION)
        surface.blit(levelTxt,(LOCATION[0],LOCATION[1]+TXT_HEIGHT))
        surface.blit(expTxt,(LOCATION[0],LOCATION[1]+TXT_HEIGHT*2))
        
    def addExp(self,num):
        self.exp+=num
        for i in xrange(100):
            if self.exp < 2**i:
                self.level=i-1
                break
        
                
def run():
    pygame.init()    
    screen = pygame.display.set_mode(SCREEN_SIZE, 0,32)
    clock=pygame.time.Clock()
    char=Character("Dingziran")
    while True:
        for event in pygame.event.get():
            if event.type ==QUIT:
                return
            
        time_passed=clock.tick(30)
        screen.fill((255, 255, 255))
        char.addExp(1)
        char.render(screen)
        pygame.display.update()
        
if __name__ == "__main__":

    run()
        
            