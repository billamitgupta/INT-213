import math
i = int(input())
if (i > 1 or i < 1000):
    
    for i in range(0, i):
        a = int(input())
        b = int(input())
        d = math.trunc((abs((a-b)/10))+1)
        if(a!=b):
            print(d)
