#WAP to check wheather the no is prime or not

def checkprime(n):
    if(n==1):
        return "not prime"
    elif(n==2):
        return "prime"
    else:
        for x in range(2,n):
            if(n%x==0):
                return "not prime"
            return"prime"

a=eval(input("Enter the number"))
print(checkprime(a))            