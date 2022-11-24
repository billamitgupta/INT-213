class info:
    def __init__(self,a,b,c):
        self.name= a
        self.rollNo= b
        self.__marks=c

        
    def disp(self):
            print("Name=",self.name)
            print("rollNo",self.rollNo)
            print("marks=",self.__marks)

    ##def __del__(self):
     #   info.name
           
            
       

stu1=info('amit',1,99)
stu1.disp()
stu2=info('aman',2,98)
stu2.disp()
stu3=info('rohan',3,88)
stu3.disp()


