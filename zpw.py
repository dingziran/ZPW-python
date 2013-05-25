import pygame
from pygame.locals import *
import math

try:
    import cPickle as pickle
except:
    import pickle
    
import sys

from random import randint
from gameobjects.vector2 import Vector2
SCREEN_SIZE=(640,480)
LOCATION=(0,0)
TXT_HEIGHT=20

class Localize(object):
    def __init__(self,character,monster,combatSys):
        self.char=character
        self.mons=monster
        self.comb=combatSys
        
    def setChar(self,character):
        f=open("character.dat","")

class CombatSys(object):
    def __init__(self,char,monster):
        self.round=1
        self.battle=[]
        self.char=char
        self.mons=monster
        self.total=1
        self.win=1
    
    def combat(self):
        charRoll=self.char.getRoll()
        monsRoll=self.mons.getRoll()
        self.total+=1
        string="Round "+str(self.round)+" : " + str(charRoll)+ " vs "+str(monsRoll)
        if charRoll>monsRoll:
            self.win+=1
            string+=" win!"
            self.char.addExp(self.mons.getExp())
        self.battle.append(string)
        self.battle=self.battle[-20:]
        self.round+=1
        
    def render(self,surface):
        new_location=(200,0) 
        height=20
        font=pygame.font.SysFont("courier new",16,True)
        for string in self.battle:
            txt=font.render(string,True,(0,0,0))
            surface.blit(txt,new_location)
            new_location=(200,new_location[1]+height)  
              
    def renderRate(self,surface):
        font=pygame.font.SysFont("courier new",16,True)
        rate=(self.win+0.0)/self.total
        txt=font.render("The winner rate is %.2f, TotalTime is %d, WinTime is %d" % (rate , self.total , self.win),True,(0,0,0))
        surface.blit(txt,(LOCATION[0],SCREEN_SIZE[1]-TXT_HEIGHT))   
           
    

class Character(object):
    
    def __init__(self,name):
        self.name=name
        self.level=0
        self.exp=0
        self.nextExp=2
        self.attack=2
        self.defence=2
        
    def render(self,surface):
        font=pygame.font.SysFont("courier new",16,True)
        nameTxt=font.render(self.name,True,(0,0,0))
        levelTxt=font.render("level is "+str(self.level),True,(0,0,0))
        expTxt=font.render("exp is " +str(self.exp),True,(0,0,0))
        surface.blit(nameTxt,LOCATION)
        surface.blit(levelTxt,(LOCATION[0],LOCATION[1]+TXT_HEIGHT))
        surface.blit(expTxt,(LOCATION[0],LOCATION[1]+TXT_HEIGHT*2))
        
    def getRoll(self):
        total=randint(1,self.attack)+randint(1,self.defence)
        return total
    
    def addExp(self,num):
        self.exp+=num
        if self.exp>self.nextExp:
            self.levelup()
            self.exp=0
    
    def levelup(self):
        self.level+=1
        self.nextExp*=2
        self.attack+=1
        self.defence+=1

class Monster(object):
    def __init__(self,name,exp,level,number,attack,defence):
        self.name=name
        self.exp=exp
        self.level=level
        self.number=number
        self.attack=attack
        self.defence=defence
        self.combatNum=1
        self.loseNum=0        
        
    def getRoll(self):
        total=self.number*(randint(1,self.attack)+randint(1,self.defence))
        self.combatNum+=1
        return total
    
    def spawn(self):
        self.exp=randint(1,10)
        self.number=randint(1,3)
        self.attack=randint(1,10)
        self.defence=randint(1,5)
        
    def getExp(self):
        return self.exp*self.number
    
                
def run():
    pygame.init()    
    screen = pygame.display.set_mode(SCREEN_SIZE, 0,32)
    clock=pygame.time.Clock()
    round=0
    if len(sys.argv)!=1:
        filename= sys.argv[1]
        with open(filename, 'rb') as in_s:
            try:
                #char = pickle.load(in_s)
                #mon = pickle.load(in_s)
                print "Read data from file"
                combat=pickle.load(in_s)
                char=combat.char
                mon=combat.mons
            except EOFError:
                pass
            else:
                pass#print 'READ: %s (%s)' % (o.name, o.name_backwards)
    else:
        char=Character("Dingziran")
        mon=Monster("Goblin",10,1,1,1,1)
        combat=CombatSys(char,mon)
    while True:
        for event in pygame.event.get():
            if event.type ==QUIT:
                with open(filename,'wb') as out_s:
                    #pickle.dump(char,out_s)
                    #pickle.dump(mon,out_s)
                    pickle.dump(combat,out_s)
                return
        time_passed=clock.tick(30)
        screen.fill((255, 255, 255))
        if round==3:
            round=0    
            combat.combat()
        char.render(screen)
        #combat.render(screen)
        combat.renderRate(screen)
        pygame.display.update()
        mon.spawn()
        round+=1
        
if __name__ == "__main__":

    run()
        
            