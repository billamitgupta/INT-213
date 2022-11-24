#WAP to read the content of the filae and count how many times a comes in file

#myfile=open(r"C:\Users\ASUS\Documents\python.txt","r")
#strl=myfile.read()
#print(strl.count('a'))

myfile=open(r"C:\Users\ASUS\Documents\python.txt","r")
count=0
strl=myfile.read()
for i in strl:
    if(i=="a"):
        count=count+1
print("the frequency of letter a is ",count)



   