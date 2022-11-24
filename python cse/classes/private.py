

#CLASS DEFINATION
#declear private

from calendar import c


class employee:
    def __init__(self,a,b,c):
        self.name=a
        self.salary=b
        self.__age=c
    def disp(self):
        print("Name=",self.name)
        print("salary",self.salary)
        print("Age=",self.__age)

emp1=employee("SUN",2000,35)
emp1.disp()
print(emp1.name)
print(emp1.salary)
print(emp1._employee__age)
print(emp1.__age)