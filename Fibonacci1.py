 #-*- coding: utf-8 -*-
def f1 (n):   #递归 效率会拉低
    pair = 0
    if n <1 :
		return -1
    if n == 2 or n == 1 :
         pair = 1
    else:
        pair = f1(n-1) + f1(n-2)
    return pair

def f2(n):   #迭代
    pair = [1,1]

    for i in range(n):

        if i == 1 or n == 2 :
            result = 1
        elif i == 0:
			pass
        else:
            #print pair[i-2],  pair[i-3]
            result = pair[i-1] + pair[i-2]
            pair.append(result)
    return result


print '请输入：'
r1 = f1(20)
r2 = f2(20)
print ("First result is %d\nSecond result is %d" %(r1,r2))