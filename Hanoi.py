def Hanoi( n , x , y, z ):
    if n == 1 :
        print(x + '-->' + z) #如果只有一层，就直接 x--> z
    else:  
	    Hanoi(n-1 , x , z, y) #前n-1层借助 z 从 x 放到 y 上
	    print(x + '-->' + z)  #把第n层直接从 x 放到 z
	    Hanoi(n-1 , y , x , z) #再把前n-1层借助 x 从 y 放到 z 上
		
n = input("The layers number is ")
Hanoi(n,'x','y','z')
 