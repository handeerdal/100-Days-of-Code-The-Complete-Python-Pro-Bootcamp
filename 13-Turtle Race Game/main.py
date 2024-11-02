import turtle
import random

turtles=[]

screen=turtle.Screen()
screen.setup(width=500,height=400)
screen.title("Turtle Race")

# List of valid rainbow colors
rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Function to get a valid user bet
def get_user_bet():
    while True:
        user_bet = screen.textinput(title="Bet", prompt="Which turtle will win the race? (Choose a rainbow color)")
        
        # Check if the bet is in the list of rainbow colors
        if user_bet.lower() in rainbow_colors:
            return user_bet.lower()
        else:
            # Show an error message if input is invalid
            screen.textinput(title="Invalid Input", prompt="Please try again. Choose a rainbow color.")

# Call the function to get a valid bet
user_bet = get_user_bet()
print(f"User's bet: {user_bet}")
toplevel=180

for i in rainbow_colors:
    x=turtle.Turtle()
    x.penup()
    x.color(i)
    x.shape('turtle')
    turtles.append(x)
    x.goto(-240,toplevel)
    toplevel-=57


while 1:
    a=random.choice(turtles)
    if a.xcor() >=230:
        print(f'{a.pencolor()} wins')
        if (user_bet==a.pencolor()):
            print('YOU WIN')
        else:
            print('YOU LOST')

        break
    b=random.randint(0,10)
    a.forward(b)

   





screen=screen.exitonclick()
