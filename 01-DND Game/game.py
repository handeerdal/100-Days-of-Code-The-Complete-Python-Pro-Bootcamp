import random

heart = 10
x = 0

print("""
                                                           ___
                                             ___..--'  .`.
                                    ___...--'     -  .` `.`.
                           ___...--' _      -  _   .` -   `.`.
                  ___...--'  -       _   -       .`  `. - _ `.`.
           __..--'_______________ -         _  .`  _   `.   - `.`.
        .`    _ /\    -        .`      _     .`__________`. _  -`.`.
      .` -   _ /  \_     -   .`  _         .` |Train Depot|`.   - `.`.
    .`-    _  /   /\   -   .`        _   .`   |___________|  `. _   `.`.
  .`________ /__ /_ \____.`____________.`     ___       ___  - `._____`|
    |   -  __  -|    | - |  ____  |   | | _  |   |  _  |   |  _ |
    | _   |  |  | -  |   | |.--.| |___| |    |___|     |___|    |
    |     |--|  |    | _ | |'--'| |---| |   _|---|     |---|_   |
    |   - |__| _|  - |   | |.--.| |   | |    |   |_  _ |   |    |
 ---``--._      |    |   |=|'--'|=|___|=|====|___|=====|___|====|
 -- . ''  ``--._| _  |  -|_|.--.|_______|_______________________|
`--._           '--- |_  |:|'--'|:::::::|:::::::::::::::::::::::|
_____`--._ ''      . '---'``--._|:::::::|:::::::::::::::::::::::|
----------`--._          ''      ``--.._|:::::::::::::::::::::::|
`--._ _________`--._'        --     .   ''-----..............LGB'
     `--._----------`--._.  _           -- . :''           -    ''
          `--._ _________`--._ :'              -- . :''      -- . ''
 -- . ''       `--._ ---------`--._   -- . :'' 
          :'        `--._ _________`--._:'  -- . ''      -- . ''
  -- . ''     -- . ''    `--._----------`--._      -- . ''     -- . ''
                              `--._ _________`--._
 -- . ''           :'              `--._ ---------`--._-- . ''    -- . ''
          -- . ''       -- . ''         `--._ _________`--._   -- . ''
:'                 -- . ''          -- . ''  `--._----------`--._""")

print('You wake up in a small, dimly lit storage room, bound with rope.')

if input('Do you attempt to break the bindings with strength? (Y/N)') == 'Y':
    x = random.randint(1, 10)
    print(f'You rolled a dice and you got {x}')
    if x < 7:
        heart -= 4
        print(f'You strain yourself, damage and staying bound. Your hearts: {heart}')
        if heart <= 0:
            print("You have no hearts left. GAME OVER.")
            exit()  # End the game if hearts reach 0
    else:
        print('You break free.')

print('The door is slightly open, revealing a patrolling guard.')
if input('Do you try to sneak past the guard? (Y/N)') == 'Y':
    x = random.randint(1, 10)
    print(f'You rolled a dice and you got {x}')
    if x < 7:
        heart -= 4
        print(f'The guard hears you, and you must either fight or flee. Your hearts: {heart}')
        if heart <= 0:
            print("You have no hearts left. GAME OVER.")
            exit()  # End the game if hearts reach 0
        if input('Do you lure the guard closer to ambush him? (Y/N)') == 'Y':
            print('You idiot, he is a guard and you don\'t have anything. YOU ARE DEAD.')
            heart = 0
            print("You have no hearts left. GAME OVER.")
            exit()  # End the game
    else:
        print('You slip past unnoticed.')

if input('A massive iron door demands an offering for passage. Do you offer something valuable from your inventory? (Y/N)') == 'Y':
    heart -= 2
    print(f'Just tell me. They caught you and tied you already. WHAT DO YOU HAVE HUH? The door didn\'t like your gift and hit you. Your hearts: {heart}')
    if heart <= 0:
        print("You have no hearts left. GAME OVER.")
        exit()  # End the game if hearts reach 0

if(input('You heard the train and you are so close. If you run maybe you can catch and leave. Are you gonna try? (Y/N)') == 'Y'):
     print("You ran with all your might, heart racing as you sprint towards the train. Just as the doors are about to close, you leap aboard, securing your escape!")
else:
    print('you are totally idiot.are you a hero or something?No train ever came again and you had to hide for so long that you died of thirst.')