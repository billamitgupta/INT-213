#Write a python program function to check wheather a number is in a given range....

def check(x):
    if ( x>0 and x<1000) :
        print("Number is in range")
    else:
        print("NUmber is not in range")

y=int(input("enter the number you want to chexk "))        
check(y)