a=""
for row in range (0,7):
    for col in range(0,7):
        if ((col==1 or col==6) and row != 0) or ((row==0 or row==3 )and (1<col<5)): 
          a=a +"*"
        else:
            a=a +" "
    a=a+"\n"
print(a)