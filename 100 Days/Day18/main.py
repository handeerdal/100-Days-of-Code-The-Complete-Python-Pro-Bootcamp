from  turtle import Turtle, Screen
import random 

my_little_turtle=Turtle()

my_little_turtle.shape('turtle')
my_little_turtle.color('purple')
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


##SQUARE
# my_little_turtle.forward(100)
# my_little_turtle.right(90)
# my_little_turtle.forward(100)
# my_little_turtle.right(90)
# my_little_turtle.forward(100)
# my_little_turtle.right(90)
# my_little_turtle.forward(100)

##DASHED LINE

# for _ in range(15):
#     my_little_turtle.forward(5)
#     my_little_turtle.penup()
#     my_little_turtle.forward(5)
#     my_little_turtle.pendown()


#TRIANGLE
# for i in range (0,3):
#     my_little_turtle.left(240)
#     my_little_turtle.forward(100)

# x=4

# #LOOP 
# while 1:
#     for i in range (0,x):
#         my_little_turtle.right(360/x)
#         my_little_turtle.forward(100)
#     x+=1
    




my_little_turtle.pensize(10) 
#Random WALK
for i in range(0,100):
    my_little_turtle.color(random.choice(colours))
    x=random.randint(1,3)
    if x==1:
        my_little_turtle.right(90)
        my_little_turtle.forward(50)
    if x==2:
        my_little_turtle.left(90)
        my_little_turtle.forward(50)
    if x==3:
        my_little_turtle.forward(50)







screen=Screen()

screen.exitonclick()
