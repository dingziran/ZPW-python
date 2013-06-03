#system
import math
from random import randint
from time import clock
import sys
try:
    import cPickle as pickle
except:
    import pickle
#3rd party lib
import pygame
from pygame.locals import *
from gameobjects.vector2 import Vector2
#project
from Monster import *
from Character import *
    

SCREEN_SIZE=(800,600)
LOCATION=(0,0)
TXT_HEIGHT=20


class CombatSys(object):
    def __init__(self,char,monster):
        self.round=1
        self.battle=[]
        self.char=char
        self.mons=monster
        self.total=0
        self.win=0
        self.chooseEqTxt=''
        self.monsType=1
        self.tmp=0
    
    def combat(self):
        charDamage,charShield=self.char.getRoll()
        monsDamage,monsShield=self.mons.getRoll()
        self.total+=1
        string="Round "+str(self.round)+" : " + str(charDamage)+"("+ str(charShield)+")" + " vs " + str(monsDamage)+"("+ str(monsShield)+")"
        if charDamage-monsShield>monsDamage-charShield:
            self.win+=1
            string+=" win!"
            self.char.addExp(self.mons.getExp())
        self.battle.append(string)
        self.battle=self.battle[-20:]
        self.round+=1
        
    def render(self,surface):
        #self.renderBattle(surface)    
        self.renderChar(surface)
        self.renderRate(surface)
        self.renderMonster(surface)
        self.renderEquip(surface)
            
    def renderBattle(self,surface):
        new_location=(200,0) 
        height=20
        font=pygame.font.SysFont("courier new",16,True)
        for string in self.battle:
            txt=font.render(string,True,(0,0,0))
            surface.blit(txt,new_location)
            new_location=(200,new_location[1]+height)  
        
    def renderChar(self,surface):        
        font=pygame.font.SysFont("courier new",16,True)
        nameTxt=font.render(self.char.name,True,(0,0,0))
        levelTxt=font.render("level is "+str(self.char.level),True,(0,0,0))
        expTxt=font.render("exp is " +str(self.char.exp),True,(0,0,0))
        expNextTxt=font.render("next level's exp is " +str(self.char.nextExp),True,(0,0,0))
        surface.blit(nameTxt,LOCATION)
        surface.blit(levelTxt,(LOCATION[0],LOCATION[1]+TXT_HEIGHT))
        surface.blit(expTxt,(LOCATION[0],LOCATION[1]+TXT_HEIGHT*2))
        surface.blit(expNextTxt,(LOCATION[0],LOCATION[1]+TXT_HEIGHT*3))
              
    def renderEquip(self,surface):
        def format(n):
            #poor
            #common
            #uncommon
            #rare
            #epic
            #legendary
            if n == 0:
                return 'None'
            elif n == 1:
                return 'common'
            elif n == 2:
                return 'uncommon'
            elif n == 3:
                return 'rare'
            elif n == 4:
                return 'epic'
            elif n == 5:
                return 'legendary'
            else:
                return 'None' 
        font=pygame.font.SysFont("courier new",16,True)
        equip=self.char.equip
        goldtxt=font.render("gold coin "+str(equip.gold),True,(0,0,0))
        txt4=font.render("helmet "+format(equip.helmet),True,(0,0,0))
        txt7=font.render("plastron "+format(equip.plastron),True,(0,0,0))
        txt2=font.render("cape "+format(equip.cape),True,(0,0,0))
        txt3=font.render("gloves "+format(equip.gloves),True,(0,0,0))
        txt6=font.render("pants "+format(equip.pants),True,(0,0,0))
        txt8=font.render("weapon "+format(equip.weapon),True,(0,0,0))
        txt1=font.render("amulet "+format(equip.amulet),True,(0,0,0))
        txt5=font.render("medal "+format(equip.medal),True,(0,0,0))
        surface.blit(goldtxt,(LOCATION[0],LOCATION[1]+TXT_HEIGHT*16))
        surface.blit(txt1,(LOCATION[0],LOCATION[1]+TXT_HEIGHT*17))
        surface.blit(txt2,(LOCATION[0],LOCATION[1]+TXT_HEIGHT*18))
        surface.blit(txt3,(LOCATION[0],LOCATION[1]+TXT_HEIGHT*19))
        surface.blit(txt4,(LOCATION[0],LOCATION[1]+TXT_HEIGHT*20))
        surface.blit(txt5,(LOCATION[0],LOCATION[1]+TXT_HEIGHT*21))
        surface.blit(txt6,(LOCATION[0],LOCATION[1]+TXT_HEIGHT*22))
        surface.blit(txt7,(LOCATION[0],LOCATION[1]+TXT_HEIGHT*23))
        surface.blit(txt8,(LOCATION[0],LOCATION[1]+TXT_HEIGHT*24))
        
    
    def renderRate(self,surface):
        font=pygame.font.SysFont("courier new",16,True)
        try:
            rate=(self.win+0.0)/self.total
        except ZeroDivisionError, e:
            rate=0
        txt=font.render("The winner rate is %.2f, TotalTime is %d, WinTime is %d" % (rate , self.total , self.win),True,(0,0,0))
        surface.blit(txt,(LOCATION[0],SCREEN_SIZE[1]-TXT_HEIGHT))   
        
    def renderMonster(self,surface):
        font=pygame.font.SysFont("courier new",16,True)
        nameTxt=font.render("The monster name is %s."%self.mons.name,True,(0,0,0))
        numTxt1=font.render("strength %d"% self.mons.strength,True,(0,0,0))
        numTxt2=font.render("defence %d%%"%self.mons.defence,True,(0,0,0))
        numTxt3=font.render("agile %d"%self.mons.agile,True,(0,0,0))
        numTxt4=font.render("lucky %d"%self.mons.lucky,True,(0,0,0))
        numTxt5=font.render("life %d"%self.mons.life,True,(0,0,0))
        numTxt6=font.render("morale %d"%self.mons.morale,True,(0,0,0))
        expTxt=font.render("You can earn %d exp."%(self.mons.exp*self.mons.number),True,(0,0,0))
        surface.blit(nameTxt,(LOCATION[0],LOCATION[1]+TXT_HEIGHT*5))
        surface.blit(numTxt1,(LOCATION[0],LOCATION[1]+TXT_HEIGHT*6))
        surface.blit(numTxt2,(LOCATION[0],LOCATION[1]+TXT_HEIGHT*7))
        surface.blit(numTxt3,(LOCATION[0],LOCATION[1]+TXT_HEIGHT*8))
        surface.blit(numTxt4,(LOCATION[0],LOCATION[1]+TXT_HEIGHT*9))
        surface.blit(numTxt5,(LOCATION[0],LOCATION[1]+TXT_HEIGHT*10))
        surface.blit(numTxt6,(LOCATION[0],LOCATION[1]+TXT_HEIGHT*11))
        surface.blit(expTxt,(LOCATION[0],LOCATION[1]+TXT_HEIGHT*12))
        if self.mons.name!="Guard":
            introTxt1=font.render("Press left key to beat a easier monster",True,(0,0,0))
            surface.blit(introTxt1,(LOCATION[0],LOCATION[1]+TXT_HEIGHT*13))
        if self.mons.name!="Crossbowman":
            introTxt2=font.render("Press right key to beat a harder monster",True,(0,0,0))
            surface.blit(introTxt2,(LOCATION[0],LOCATION[1]+TXT_HEIGHT*14))
            
def createMons(n):
    if n==1:
        return M1(1)
    elif n==2:
        return M2(2)
    elif n==3:
        return M3(3)
    elif n==4:
        return M4(4)
    elif n==5:
        return M5(5)
    elif n==6:
        return M6(6)
    elif n==7:
        return M7(7)       
           
def chooseMons(combat,surface):
    pressed = pygame.key.get_pressed()
    combat.tmp+=1
    if combat.tmp>10:
        combat.tmp=0
        if pressed[K_LEFT]:
            if combat.monsType>1:
                combat.monsType-=1
                combat.mons=createMons(combat.monsType)
                combat.total=0
                combat.win=0
        if pressed[K_RIGHT]:
            if combat.monsType<7:
                combat.monsType+=1
                combat.mons=createMons(combat.monsType)
                combat.total=0
                combat.win=0
    txt=combat.chooseEqTxt
    if pressed[K_1]:
        txt=combat.char.useGold(1)
    if pressed[K_2]:
        txt=combat.char.useGold(2)
    if pressed[K_3]:
        txt=combat.char.useGold(3)
    if pressed[K_4]:
        txt=combat.char.useGold(4)
    if pressed[K_5]:
        txt=combat.char.useGold(5)
    if pressed[K_6]:
        txt=combat.char.useGold(6)
    if pressed[K_7]:
        txt=combat.char.useGold(7)
    if pressed[K_8]:
        txt=combat.char.useGold(8)

    font=pygame.font.SysFont("courier new",16,True)
    nameTxt=font.render(txt,True,(0,0,0))
    introTxt=font.render("use key 1 to 8 to use gold to update the equip",True,(0,0,0))
    surface.blit(introTxt,(LOCATION[0],LOCATION[1]+TXT_HEIGHT*26))
    surface.blit(nameTxt,(LOCATION[0],LOCATION[1]+TXT_HEIGHT*27))

    
                
def run():
    pygame.init()    
    screen = pygame.display.set_mode(SCREEN_SIZE, 0,32)
    clock=pygame.time.Clock()
    round=0
    if len(sys.argv)!=1:
        filename= sys.argv[1]
        try:
            with open(filename, 'rb') as in_s:
                try:
                    #char = pickle.load(in_s)
                    #mon = pickle.load(in_s)
                    print "Read data from file"
                    combat=pickle.load(in_s)
                    combat.total=0
                    combat.win=0
                except EOFError:
                    pass
                else:
                    pass#print 'READ: %s (%s)' % (o.name, o.name_backwards)
        except IOError:
            char=Character("Dingziran")
            mon=M1(1)
            combat=CombatSys(char,mon)
    else:
        char=Character("Dingziran")
        mon=M1(1)
        combat=CombatSys(char,mon)
    while True:
        for event in pygame.event.get():
            if event.type ==QUIT:
                with open(filename,'wb') as out_s:
                    pickle.dump(combat,out_s)
                return
        time_passed=clock.tick(30)
        screen.fill((255, 255, 255))
        if round==3:
            round=0
            combat.combat()
        
        combat.render(screen)
        chooseMons(combat,screen)
        pygame.display.update()
        #combat.mons.spawn()
        round+=1

def timeit():
    filename='test.dat'
    try:
        with open(filename, 'rb') as in_s:
            try:
                print "Read data from file"
                combat=pickle.load(in_s)
                char=combat.char
                mon=combat.mons
            except EOFError:
                pass
            else:
                pass#print 'READ: %s (%s)' % (o.name, o.name_backwards)
    except IOError:
        char=Character("Dingziran")
        mon=Monster("Goblin",10,1,1,1,1)
        combat=CombatSys(char,mon)
    finally:
        if in_s:
            in_s.close()
    n=10000
    t=clock()
    for _ in xrange(n):
        combat.combat()
        mon.spawn()
    t=clock()-t
    print '%ds combat using %f second'%(n,t)
if __name__ == "__main__":

    run()
    #timeit()
        
        
            