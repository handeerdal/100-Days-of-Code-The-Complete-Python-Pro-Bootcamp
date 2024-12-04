import picture
import random
print(picture.photo)



print('Welcome to BLACK JACK')

    


def choosecard(user,sum):
    selected=random.choice(deck)
    user.append(selected)
    deck.remove(selected)
    if selected=='K' or selected=='Q' or selected=='J':
        return 10
    elif selected=='A':
        return 11 if sum + 11 <= 21 else 1    
    else:
        return selected    




def whoisthewinner(usersum,compsum):
    if usersum==21:
        print('YOU WIN')
        return 1
    elif compsum==21:
        print('COMPUTER WIN')
        return 1
    elif usersum>21:
        print('COMPUTER WIN')
        return 1

    else:
        return 0

while(True):
    usersum=0
    user=[]
    computer=[]
    compsum=0
    whois=0
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,"K", "A","Q","J", 2, 3, 4, 5, 6, 7, 8, 9, 10,2, 3, 4, 5, 6, 7, 8, 9, 10,2, 3, 4, 5, 6, 7, 8, 9, 10,"K", "A","Q","J", 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,"K", "A","Q","J", 2, 3, 4, 5, 6, 7, 8, 9, 10,2, 3, 4, 5, 6, 7, 8, 9, 10,2, 3, 4, 5, 6, 7, 8, 9, 10,"K", "A","Q","J"]
    get=str(input('Do you want to play? y/n'))
    if(get=='n'):
        break
    usersum+=choosecard(user,usersum)
    compsum+=choosecard(computer,compsum)
    while (whois==0):
        usersum+=choosecard(user,usersum)
        compsum+=choosecard(computer,compsum)
        print(f'You choose {user}')
        print(f'Computer choose {computer[0]}')
        whois=whoisthewinner(usersum,compsum)
        if whois==1:
            break
        # print(usersum,compsum)
        doyouwanttocontinue=str(input('do yo want to continue y/n'))
        if doyouwanttocontinue=='y':
            continue
        if doyouwanttocontinue=='n': 
           print(f'You choose {user}')
           print(f'Computer choose {computer}') 
           if compsum>21 and usersum<21:
                print('YOU WIN')
       
           elif compsum<21 and usersum>21:
                 print('COMPUTER WIN')

       
           elif compsum>usersum:
                print('YOU LOST')

           elif usersum>compsum:
                print('YOU WIN')
           
           break

        

    

    

    

