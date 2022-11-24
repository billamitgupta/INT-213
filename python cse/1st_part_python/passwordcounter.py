counter=0
password= "abc123"
x=input("Enter your password: ")
for counter in range(3):
 if(x==password):
    print("you have been logged in")
    break
else:
    print("your password is wrong please renter your password")
    counter=counter+1
