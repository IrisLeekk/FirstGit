# -*- coding: cp936 -*-
"""
�������ӣ����޵ݹ飩
�����е���__init__������ʼ��ʱ��������self.width��self.height�ĸ�ֵ������
�������__setattr__�����ֵ��������width��height������square ���Ծͻ�
ʵ��self.name = value����������Ҳ��һ����ֵ�������������__setattr__���
��ֵ����������������ѭ����
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
            #2.7�滻�ɣ�super(Rectangle,self).__setattr__(name,value)

    def getArea(self):
        return (self.width*self.height)
        
            
