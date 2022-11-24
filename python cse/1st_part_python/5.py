quantity=int(input("number quantity customer wants"))
totalCOst=quantity*100
if(totalCOst>1000):
    discount=totalCOst- (totalCOst*.1)
    print("total cost",discount)
else:
    print("total cost is",totalCOst)