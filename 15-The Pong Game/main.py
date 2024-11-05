import turtle
import random
import time
from players import Player
from dottedline import Line
from ball import Ball
from score import Score

turtle.colormode(255)
increase=5

screen=turtle.Screen()
screen.bgcolor((191,243,224))
screen.setup(width=1000,height=800)
screen.tracer(0)


line=Line()
score1=Score()
score1.goto(-400,330)
score1.createscore()

score2=Score()
score2.goto(400,330)
score2.createscore()

# score2=Score()
# score1.goto(200,600)

firstplayer=Player()
secondplayer=Player()
firstplayer.goto(-280,0)
secondplayer.goto(280,0)



screen.listen()

screen.onkeypress(firstplayer.up, 'Up')
screen.onkeyrelease(firstplayer.stop_up, 'Up')
screen.onkeypress(firstplayer.down, 'Down')
screen.onkeyrelease(firstplayer.stop_down, 'Down')
screen.onkeypress(firstplayer.down, 'Down')

# Bind keys for second player
screen.onkeypress(secondplayer.up, 'w')
screen.onkeyrelease(secondplayer.stop_up, 'w')
screen.onkeypress(secondplayer.down, 's')
screen.onkeyrelease(secondplayer.stop_down, 's')
bouncingball=Ball()

def game_loop():

    screen.update()
    firstplayer.move()
    secondplayer.move()
    screen.ontimer(game_loop, 10 )  # Adjust delay as needed for smoothness
    bouncingball.move()
    #detectcollusion with wall
    if bouncingball.ycor()>=380 or bouncingball.ycor()<=-380:
        bouncingball.bounce()


    #detectcollusion with paddle
    if bouncingball.xcor()>=280 and bouncingball.distance(secondplayer)<50: 

        bouncingball.paddlebounce()
    elif bouncingball.xcor()>320:
        score1.score+=1
        score1.clear()
        score1.createscore()
        bouncingball.reset_pos()   


         
    if bouncingball.xcor()<=-280 and bouncingball.distance(firstplayer)<50: 

        bouncingball.paddlebounce()
    elif bouncingball.xcor()<-320:
        score2.score+=1
        score2.clear()
        score2.createscore() 
        bouncingball.reset_pos()   
        

        


# Start the game loop
game_loop()
screen.mainloop()




screen.exitonclick()
