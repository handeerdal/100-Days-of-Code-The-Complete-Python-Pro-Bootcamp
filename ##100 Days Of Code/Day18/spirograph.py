import turtle
import random


turtle.colormode(255)


def randomcolor():
    r=random.randint(0,255)  
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)


myturtle=turtle.Turtle()
myturtle.speed('fastest')

# for i in range(0,360):
#     myturtle.color(randomcolor())
#     myturtle.circle(100)
#     myturtle.forward(1)

#     myturtle.right(3)



for i in range(0,360,5):
    myturtle.color(randomcolor())
    myturtle.circle(100)
    myturtle.setheading(i)    

    
screen=turtle.Screen()
screen.exitonclick()