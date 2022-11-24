import string
from turtle import position
from xml.dom.minidom import Element
lg1 = "I am learning python"
print (str.split (lg1,'ear'))

l1=[1,2,3,4,5,6]
l1.append(9)
print(l1)
print(l1.index(3))
print(l1.remove(3))
l2=[1,2,3,4,5,6,7]
l2.reverse()
print(l2)
l2.sort()
print(l2)
l2.insert(4,100)
print(l2)
print(len(l2))


#insert two element

l2.append(100)
l2.append(400)
print(l2)
#sum of list
print(sum(l2))

#compare the element

l3=[1,2,2,4,5,6,78,9,10]
print()

#tuple

tuple_1=('a','b')
type(tuple_1)
<class 'tuple'>
tuple_2=('AB',)+tuple_1[1:]
tuple_2
