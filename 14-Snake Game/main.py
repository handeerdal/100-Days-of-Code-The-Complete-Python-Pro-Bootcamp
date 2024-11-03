import time
import turtle
from snake import Snake
from food import Food
from score import Score


screen=turtle.Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('SNAKE GAME')
screen.tracer(0)

newsnake=Snake()
food=Food()
score=Score()

screen.listen()
screen.onkey(newsnake.up,'Up')
screen.onkey(newsnake.down,'Down')
screen.onkey(newsnake.left,'Left')
screen.onkey(newsnake.right,'Right')


game_is_on=True


while game_is_on:
     screen.update()
     time.sleep(0.1)
     newsnake.movesnake()

     if newsnake.head.distance(food)<15:
          food.changepos()
          newsnake.extendsnake()

          score.increasescore()
     game_is_on=newsnake.tailcollision(score)

     if newsnake.head.xcor()>290 or newsnake.head.xcor()<-290 or newsnake.head.ycor()>290 or newsnake.head.ycor()<-290:
        game_is_on=False
        score.gameover()

        


    


    

    
screen.exitonclick()



