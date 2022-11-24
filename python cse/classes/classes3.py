from tokenize import Name


class student:
    def __init__ (self):
        self.Name= input("Enter the name")
        self.RollNo= int(input("Enter the roll no"))

        self.__marks1= int(input("Enter the marks1"))
        self.__marks2= int(input("Enter the marks2"))
        self.__marks3= int(input("Enter the marks3"))

    def percent(self):
        self.percent1=((self.__marks1 + self.__marks2 + self.__marks3)/300)*100
    
    def disp(self):
        print("name: " ,self.Name)
        print("RollNo: ",self.RollNo)
        print("Marks: ",self.__marks1,"Marks2: ",self.__marks2, "marks3: ",self.__marks3)
        print("Percent: " ,self.percent1)

stu1=student()
stu1.percent()
stu1.disp()
        