import turtle

myturtle=turtle.Turtle()

def move_forward():
    myturtle.forward(10)


def move_back():
    myturtle.backward(10)

def move_clokwise():
    myturtle.right(10)   
def move_counterclokwise():
    myturtle.left(10)  
def clean():
    myturtle.penup()
    myturtle.clear()
    myturtle.home()
    myturtle.pendown()


screen=turtle.Screen()
screen.listen()
screen.onkey(key='w',fun=move_forward) ##NO PARANTHESIS
screen.onkey(key='s',fun=move_back) ##NO PARANTHESIS
screen.onkey(key='d',fun=move_clokwise) ##NO PARANTHESIS
screen.onkey(key='a',fun=move_counterclokwise) ##NO PARANTHESIS
screen.onkey(key='c',fun=clean) ##NO PARANTHESIS


screen.exitonclick()
