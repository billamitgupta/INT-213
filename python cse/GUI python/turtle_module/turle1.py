import turtle
turtle.showturtle()
   
for y in range(60,40,-5):
    turtle.begin_fill()

    if(y==55):
        turtle.circle(y) 
        turtle.fillcolor("black")
        turtle.end_fill()
    elif(y==50):
        turtle.circle(y) 
        turtle.fillcolor("pink")
        turtle.end_fill()
    
    elif(y==45):
        turtle.circle(y) 
        turtle.fillcolor("red")
        turtle.end_fill()

    
    elif(y==40):
        turtle.circle(y) 
        turtle.fillcolor("cyan")
        turtle.end_fill()







'''
turtle.begin_fill()
turtle.circle(60) #radius=45
turtle.fillcolor("cyan")
turtle.end_fill()
turtle.begin_fill()
turtle.circle(55) #radius=45
turtle.fillcolor("red")
turtle.end_fill()
turtle.begin_fill()
turtle.circle(50) #radius=45
turtle.fillcolor("green")
turtle.end_fill()
turtle.begin_fill()
turtle.circle(45) #radius=45
turtle.fillcolor("yellow")
turtle.end_fill()
'''

