#CLASS DEFINATION
# __init__ is constructor

class employee:
    def __init__(self,a,b):
        self.name=a
        self.salary=b
    def disp(self):
        print("Name=",self.name)
        print("salary",self.salary)

emp1=employee("SUN",2000)
print(hasattr(emp1,"name"))
print(hasattr(emp1,"age"))
print(getattr(emp1,"name"))
#print(getattr(emp1,"age"))
setattr(emp1,"name","Moon")

emp1.disp()
delattr(emp1,"salary")
print(emp1.name)
print(emp1.salary)