
def factorial(x):
    fac=1
    for i in range(1,x+1):
        fac=fac*i
    print("factorial of number is",fac)

z=int(input("Enter the number for which you want factorail"))
factorial(z)
