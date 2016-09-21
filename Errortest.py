# -*- coding: utf-8 -*-
try:
  
    sum = 1+'1'
    f = open('123.txt')
    print(f.read())
    f.close
except OSError as reason: #检测输出系统错误 和 类型错误
    print('文件出错啦'+ str(reason))
except TypeError as reason:
    print'类型出错' + str(reason)
finally: #无论如何都会执行
    print('finally！')