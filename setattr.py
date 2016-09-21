# -*- coding: cp936 -*-
"""
错误例子（无限递归）
在类中调用__init__函数初始化时，进行了self.width和self.height的赋值操作，
即会调用__setattr__这个赋值函数，而width和height不等于square 所以就会
实现self.name = value操作，而这也是一个赋值操作，即会调用__setattr__这个
赋值函数，所以陷入死循环。
"""


class Rectangle(object):
    def __init__(self,width=0,height=0):
        self.width = width
        self.height = height
    def __setattr__(self,name,value):
        if name == 'square':
            self.width = value
            self.height = value
        else:
            self.name = value
            #2.7替换成：super(Rectangle,self).__setattr__(name,value)

    def getArea(self):
        return (self.width*self.height)
        
            
