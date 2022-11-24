#class person attrebutes name,dob calculatr the age and inform wheather the person is eligible to vote or not

import datetime
today=2022
class persom():

    def __init__(self,name,dob):
        self.name=name
        self.dob=dob

    def check(self):
        today=datetime.date.today()
        age=today.year-self.dob.year
        if today<datetime.date(today.year,self.dob.month,self.dob.day):
            age =-1
        if age>=18:
            print(self.name,", congratulation>>> you are eligible to vate." )
        else:
            print(self.name,",Sorry... tou should be atleest 18 years of a age")

p=persom("abc",datetime.date(1992,12,11))
p.check()





