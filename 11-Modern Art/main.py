import colorgram
import turtle
import random 

turtle.colormode(255)
rgbcolors=[(233, 233, 232), (236, 231, 233), (231, 233, 237), (222, 232, 225), (207, 160, 83), (54, 89, 131), (145, 91, 40), (139, 27, 48), (222, 206, 108), (132, 177, 203)]

# colors=colorgram.extract('c:/Users/snrpc/Desktop/Python/11-Modern Art/bb.jpg', 10)


# for color in colors:

#      r=color.rgb.r

#      g=color.rgb.g

#      b=color.rgb.b

#      rgbcolors.append((r,g,b))


# print(rgbcolors)

myturtle=turtle.Turtle()
myturtle.penup()
myturtle.speed('fastest')
myturtle.setheading(225)
myturtle.forward(250)
print(myturtle.pos())
myturtle.setheading(0)
myturtle.pendown()


for i in range(1,11):
    for _ in range(0,10):
        myturtle.color(random.choice(rgbcolors))
        myturtle.dot(20)
        myturtle.penup()
        myturtle.forward(50)
  
    myturtle.goto(-176.78,-176.78+i*50)
    myturtle.left(90)
    myturtle.right(90)
    myturtle.pendown()




