import re
txt= open(r"C:\\Users\\ASUS\Documents\\python.txt","r")
txt1=txt.read()

x=re.match(r"\bthe",txt1)

if x:
    print("yes! We have the match!")
else:
    print("no match")