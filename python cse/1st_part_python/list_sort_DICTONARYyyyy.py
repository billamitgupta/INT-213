'''''
from unicodedata import name


l1=[3,4,2,6,7]
l1.sort()
print(l1)
'''''
'''''
#crete dictonary

D1={'one':'Name'}
D3={}
D3 ['one'] = 'roll number'
print(D1)
print(D3)

#del D3['one']
#print(D3)

print(len (D3))
print(D3.keys())
'''''

#alisasing and copying

from ast import alias
from copy import copy


opposites={'up':'down','right':'left','true':'false'}
alias=opposites
copy= opposites.copy()
alias['right'] ='hello'
print(opposites['right'])
copy['right'] = 'privilage'
print(opposites['right'])
