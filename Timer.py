# -*- coding: cp936 -*-
import time as t
class MyTimer:
    def __init__(self):
        self. name = ['year','month','day','hour','minute','second']
        self.last = []
        self.begin = []
        self.end = []
        self.prompt = 'You have to start first!'
    #改写内置函数__str__ （就是当print该实例时调用的一个函数）
    def __str__(self):
        return self.prompt
    #改写内置函数__repr__ （就是单单当输入该实例时显示调用的一个函数）
    __repr__ = __str__

    
    def __add__(self,other):
        prompt = 'Add result: '
        result = []
        for index in range(6):
            result.append(self.last[index]+other.last[index])
            if result[index]:
                prompt +=(str(result[index]) + self.name[index])
        return prompt

    
#开始计时
    def start(self):
       self.begin = t.localtime()
       self.prompt = 'You should STOP first.'
       print('Begin now....')
#结束计时
    def stop(self):
        if  len(self.begin) == 0:
             self.prompt = 'You should START first.'
             print self.prompt
        else:
            self.end = t.localtime()
            self._cal()
            print ('Time up!')
		
    def _cal(self):
        self.prompt = 'In sum the time is '
        for index in range(6):
            self.last.append(self.end[index] - self.begin[index])
            if  self.last[index]:
                self.prompt +=str(self.last[index])+str(self.name[index])+' '
        self.begin = []
        self.end = []

            
		
      
