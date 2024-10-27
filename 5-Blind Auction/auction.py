import photo
import os 

print(photo.photo)

bidders={}
max=''
ans=0


while True:
    print('welcome to blind auction')
    name= str(input('what is your name'))
    money= int(input('how much you are offering$'))

    bidders[name]=money

    isitfinished=str(input('are there any more bidders? yes/no'))

    if (isitfinished)=='yes':
        os.system('cls' if os.name == 'nt' else 'clear')
        continue

    elif isitfinished=='no':  
        break

for key in bidders:
    if bidders[key]>ans:
        ans=bidders[key]
        max=key


print(f'auction is finished.{max} won with {ans}$. other bidders:')

