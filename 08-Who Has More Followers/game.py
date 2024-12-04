import game_data
import random

totalscore=0
score=0
def startgame():
    while True:
        print('Welcome to the who has more follower game, try to find who is more popular!')
        global totalscore
        if totalscore>0:
            print(f'TOTAL SCORE:{totalscore}')
        while True:
            x=popular()
            if x==1:
                if int(input('One more try? 1/0'))==1:
                    print("\n")
                    break
                else:
                    exit()


  
def popular():
    global totalscore
    global score
    famous1=random.choice(game_data.data)
    print(f"Name is {famous1['name']}, {famous1['description']},from {famous1['country']}")
    # print(f"follower:{famous1['follower_count']}")
    famous2=random.choice(game_data.data)
    while famous1 == famous2:
        famous2 = random.choice(game_data.data)

    print(f"Name is {famous2['name']}, {famous2['description']},from {famous2['country']}")
    # print(f"follower:{famous2['follower_count']}")

    user=int(input('Who is more popular 1 or 2?'))
    if user==1 and famous1['follower_count']>famous2['follower_count']:
        print('That is true!')
        score+=1

        return 0
    elif user==2 and famous2['follower_count']>famous1['follower_count']:
        print('That is true!')
        score+=1
        return 0 
    else:
        print(f'You lost the game your score is {score}')
        if score>totalscore:
            totalscore=score
            score=0

        return 1


startgame()






      

