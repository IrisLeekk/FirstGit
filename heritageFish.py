# coding=utf-8
import random as r
class Fish(object):
    def __init__(self):
        self.x = r.randint(0 , 10)
        self.y = r.randint(0,10)

    def move(self):
        self.x -= 1
        print("my place is ",self.x , self.y)
	kkk
class Goldfish(Fish):
    pass
class Carp(Fish):
    pass
	
class Shark(Fish):
    def __init__(self):
        super(Shark,self).__inkkkit__()
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('I am eating!!!')
            self.hungry = False
        else:
            print("Enough~")
		
