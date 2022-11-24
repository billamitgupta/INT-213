#CLASS DEFINATION

class hero:
    def __init__(self):
        self.name="abc"
        self.salary=10
    def disp(self):
        print("Name=",self.name)
        print("salary",self.salary)

emp1=hero()
emp1.disp()
print(emp1.name)