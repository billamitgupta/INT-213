myfile=open(r"C:\Users\ASUS\Documents\python.txt","a")
for i in range (3):
    name=input("Enter the name:")
    myfile.write(name)
    myfile.write('\n')

myfile.close()
myfile=open(r"C:\Users\ASUS\Documents\python.txt","r")
print(myfile.read())
