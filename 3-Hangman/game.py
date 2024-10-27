import random
import string 

hangman=[
"""
 ____
|/   |
|   (_)
|    
|    
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|    |
|    |    
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \|
|    |
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \|/
|    |
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \|/
|    |
|   / 
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \|/
|    |
|   / \
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   /|\
|    |
|   | |
|
|_____
"""]

words = ["Witcher",
    "RedDead",
    "Cyberpunk",
    "Zelda",
    "DarkSouls",
    "Assassins",
    "Cod",
    "Horizon",
    "Doom",
    "Ghost",
    "MonsterHunter",
    "FarCry",
    "Battlefield",
    "Sekiro",
    "WatchDogs",
    "SpiderMan",
    "FinalFantasy",
    "DragonAge",
    "Skyrim"]

words = [word.lower() for word in words]



print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/         


      AAA GAMES              
      ''')

print('your word:')

word=random.choice(words)

guessedword=['_']*len(word)

print(''.join(guessedword))

heart=6
counter=0
alreadychosen=[]

while True:
    if heart==0:
        print(f'YOU LOST your word is {word}')
        break

        
    get=input('give a letter').lower()
    if get not in string.ascii_lowercase or get=='':
        print('please choose a letter')
        continue
    if get in alreadychosen:
        print(f'you already choose {get}')
        continue
    alreadychosen.append(get) 

    for i in range(0,len(word)):
        if word[i]==get:
            guessedword[i]=get
            
    if get not in guessedword:
        heart-=1
        print(hangman[counter])
        
        counter+=1
    print(''.join(guessedword))
    if '_' not in guessedword:
        print('Congrats!You won!')
        break



        


