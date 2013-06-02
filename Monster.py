from random import randint
class Monster(object):
    def __init__(self,name,exp,strength,defence,agile,lucky,life,morale,number):
        self.name=name
        #attribute
        self.strength=strength
        self.defence=defence
        self.agile=agile
        self.lucky=lucky
        self.life=life
        self.morale=morale
        #quantity and level
        self.number=number
        self.exp=exp
        
    def getRoll(self):
        damage=self.number*(randint(self.strength/2,self.strength*2)
                           *randint(self.agile/2+100,self.agile*2+100)
                           *randint(self.lucky/2+100,self.lucky*2+100)
                           *randint(self.morale/2+100,self.morale*2+100)/100.0/100.0/100.0)
        shield=self.number*(randint(self.defence/2+100,self.defence*2+100)
                           *randint(self.life/2,self.life*2)
                           *randint(self.lucky/2+100,self.lucky*2+100)
                           *randint(self.morale/2+100,self.morale*2+100)/100.0/100.0/100.0)
                            
        return (damage,shield)
    
    def spawn(self):
        self.number=randint(1,1)
        
    def getExp(self):
        return self.exp*self.number
   
class M1(Monster):
    def __init__(self,n):
        Monster.__init__(self,name="Goblin",exp=1,strength=4,defence=9,agile=30,lucky=3,life=25,morale=7,number=n)
    
class M2(Monster):
    def __init__(self,n):
        Monster.__init__(self,name="Skeleton",exp=2,strength=5,defence=14,agile=45,lucky=5,life=22,morale=7,number=n)
    
class M3(Monster):
    def __init__(self,n):
        Monster.__init__(self,name="wolf",exp=4,strength=5,defence=14,agile=55,lucky=8,life=25,morale=6,number=n)
    
class M4(Monster):
    def __init__(self,n):
        Monster.__init__(self,name="Rogue",exp=8,strength=11,defence=34,agile=45,lucky=8,life=70,morale=7,number=n)
    
class M5(Monster):
    def __init__(self,n):
        Monster.__init__(self,name="Skilled killer",exp=16,strength=15,defence=34,agile=45,lucky=6,life=72,morale=7,number=n)
    
class M6(Monster):
    def __init__(self,n):
        Monster.__init__(self,name="Demon",exp=32,strength=21,defence=34,agile=50,lucky=8,life=90,morale=11,number=n)
    
class M7(Monster):
    def __init__(self,n):
        Monster.__init__(self,name="Dragon",exp=64,strength=56,defence=49,agile=55,lucky=10,life=260,morale=7,number=n)
 