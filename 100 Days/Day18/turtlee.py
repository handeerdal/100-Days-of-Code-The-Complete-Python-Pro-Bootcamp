import turtle
import random


turtle.colormode(255)


def randomcolor():
    r=random.randint(0,255)  
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)



tim = turtle.Turtle()
tim.pensize(15)
tim.speed('fastest')


#Random WALK
for i in range(0,100):
    tim.color(randomcolor())
    x=random.randint(1,3)
    if x==1:
        tim.right(90)
        tim.forward(50)
    if x==2:
        tim.left(90)
        tim.forward(50)
    if x==3:
        tim.forward(50)




screen=turtle.Screen()
screen.exitonclick()