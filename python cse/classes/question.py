#class circle use a class variable to define lhe value of constant PI. 
# calculate area of circumfernce of the circle with specigird radius

from xml.etree.ElementTree import PI
PI=3.14

class circle:
    def area(self,r):
        
        areaa=PI*r*r
        print(areaa)

    def circum(self,r):
        circ=2*PI*r
        print(circ)

cir1=circle()
cir1.area(5)
cir1.circum(5)