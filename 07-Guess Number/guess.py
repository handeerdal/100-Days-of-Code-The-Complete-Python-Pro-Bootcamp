import random
typeofgame=str(input('Welcome to Guess the Number Game.Choose easy or hard h/e'))

if typeofgame=='h':
    attempt=5
elif typeofgame=='e':
    attempt=10

tempattempt=attempt

while(True):
    number=random.randint(0,100)

    for i in range(1,attempt):
    
        guess=int(input(f'Guess the number {tempattempt} attempt left'))
        if(guess<number):
            print('Too low ')
        elif(guess>number):
            print('Too high')
        elif number==guess:
            print('YOU WON')
            break
        tempattempt-=1

    print(f'you lost.number was {number}')
    break



