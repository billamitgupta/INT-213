class person:
    def __init__(self, fname, lname):
        self.firstname=fname
        self.lastname=lname
        self.__marks1= int(input("Enter the marks1"))
        self.__marks2= int(input("Enter the marks2"))
        self.__marks3= int(input("Enter the marks3"))
    def printname(self):
        print(self.firstname,self.lastname)

    def percent(self):
        self.percent1=((self.__marks1 + self.__marks2 + self.__marks3)/300)*100

class student(person):  
        def __init__(self, fname, lname,year):
            super().__init__(self,fname,lname)
            self.year=year
         
    
 
x=student("Amit","Gupta",2019)
x.printname()
x.percent()