from random import randint
class Character(object):
    
    def __init__(self,name):
        self.name=name
        self.level=0
        self.exp=0
        self.nextExp=4
        self.strength=2
        self.defence=1
        self.agile=1
        self.lucky=1
        self.life=10
        self.morale=1
        self.number=1
        self.equip=Equip()
        
        
    def getRoll(self):
        equip=self.equip
        damage=self.number*(randint((self.strength+2**equip.weapon+2**equip.gloves)/2,
                                    (self.strength+2**equip.weapon+2**equip.gloves)*2)
                           *randint((self.agile/2+2**equip.pants)/2+100,
                                    (self.agile/2+2**equip.pants)*2+100)
                           *randint((self.lucky+2**equip.amulet)/2+100,
                                    (self.lucky+2**equip.amulet)*2+100)
                           *randint((self.morale+2**equip.medal)/2+100,
                                    (self.morale+2**equip.medal)*2+100)
                            /100.0/100.0/100.0)
        shield=self.number*(randint((self.defence+2**equip.plastron+2**equip.cape)/2+100,
                                    (self.defence+2**equip.plastron+2**equip.cape)*2+100)
                           *randint((self.life+2**equip.helmet)/2,
                                    (self.life+2**equip.helmet)*2)
                           *randint((self.lucky+2**equip.amulet)/2+100,
                                    (self.lucky+2**equip.amulet)*2+100)
                           *randint((self.morale+2**equip.medal)/2+100,
                                    (self.morale+2**equip.medal)*2+100)/100.0/100.0/100.0)
                            
        return (damage,shield)
    
    def addExp(self,num):
        self.exp+=num
        if self.exp>self.nextExp:
            self.levelup()
            self.exp=0
        eq=self.getEquip(num)
        self.equip.gold+=num
        if eq==0:
            return
        i=randint(1,8)
        if i==1 and self.equip.amulet<eq:
            self.equip.amulet=eq
        elif i==2 and self.equip.cape<eq:
            self.equip.cape=eq
        elif i==3 and self.equip.gloves<eq:
            self.equip.gloves=eq
        elif i==4 and self.equip.helmet<eq:
            self.equip.helmet=eq
        elif i==5 and self.equip.medal<eq:
            self.equip.medal=eq
        elif i==6 and self.equip.pants<eq:
            self.equip.pants=eq
        elif i==7 and self.equip.plastron<eq:
            self.equip.plastron=eq
        elif i==8 and self.equip.weapon<eq:
            self.equip.weapon=eq
            
    def useGold(self,i):
        k=10
        if i==1 and 2**(self.equip.amulet+k)<self.equip.gold:
            self.equip.amulet+=1
            self.equip.gold-=2**(self.equip.amulet+k)/2
            return 'update equip success'
        elif i==2 and 2**(self.equip.cape+k)<self.equip.gold:
            self.equip.cape+=1
            self.equip.gold-=2**(self.equip.cape+k)/2
            return 'update equip success'
        elif i==3 and 2**(self.equip.gloves+k)<self.equip.gold:
            self.equip.gloves+=1
            self.equip.gold-=2**(self.equip.gloves+k)/2
            return 'update equip success'
        elif i==4 and 2**(self.equip.helmet+k)<self.equip.gold:
            self.equip.helmet+=1
            self.equip.gold-=2**(self.equip.helmet+k)/2
            return 'update equip success'
        elif i==5 and 2**(self.equip.medal+k)<self.equip.gold:
            self.equip.medal+=1
            self.equip.gold-=2**(self.equip.medal+k)/2
            return 'update equip success'
        elif i==6 and 2**(self.equip.pants+k)<self.equip.gold:
            self.equip.pants+=1
            self.equip.gold-=2**(self.equip.pants+k)/2
            return 'update equip success'
        elif i==7 and 2**(self.equip.plastron+k)<self.equip.gold:
            self.equip.plastron+=1
            self.equip.gold-=2**(self.equip.plastron+k)/2
            return 'update equip success'
        elif i==8 and 2**(self.equip.weapon+k)<self.equip.gold:
            self.equip.weapon+=1
            self.equip.gold-=2**(self.equip.weapon+k)/2
            return 'update equip success'
        return 'you need more gold to update the equip'
        
    def levelup(self):
        self.level+=1
        self.nextExp*=2
        self.strength+=1
        self.defence+=1
        self.agile+=1
        self.morale+=1
        self.life+=2
        
        
    def getEquip(self,num):
        rate=num
        if randint(1,100)<=rate:
            rate/=10
            if randint(1,100)<=rate:
                rate/=10
                if randint(1,100)<=rate:
                    rate/=10
                    if randint(1,100)<=rate:
                        rate/=10
                        if randint(1,100)<=rate:
                            rate/=10
                            return 5
                        return 4
                    return 3
                return 2
            return 1
        return 0
        
        
        
class Equip(object):
    def __init__(self):
        self.gold=0
        #helmet life
        self.helmet=0
        #plastron defence
        self.plastron=0
        #cape defence
        self.cape=0
        #gloves strength
        self.gloves=0 
        #pants agile
        self.pants=0
        #weapon strength
        self.weapon=0
        #amulet lucky
        self.amulet=0
        #medal morale
        self.medal=0
        