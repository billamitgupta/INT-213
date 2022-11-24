'''''
#Q1 add a key to dictonary

d3={0:10,1:20}
d3 ['2'] ='30'
print(d3)

#concatenate dictonary

t1={1:10,2:20}
t2={3:30,4:40}
t3={5:50,6:60}
t4={}
for d in (t1,t2,t3):t4.update(d)
print(t4)
'''''

#check given ley already exits in dictonary



#WAP to print a dictonary where the key is from 1 to 15 and value is square of the keys

for x in range(1,16):
    d1={x:(x*x)}
    print(d1)

#WAP to sum all the iteam indictonary 

t5={1:10,2:30,4:40}
for x in range(1,3):
    z=t5.values(x)
    f=0
    f=f+z

