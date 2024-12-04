import main


def coins(drinktype):
     avaliablemoney=0
     print(f'Please insert coins.It costs {main.MENU[drinktype]["cost"]}$')
     quanters=int(input('How money 25 cents you inserted?'))
     dimes=int(input('How money 10 cents you inserted?'))
     nickles=int(input('How money 5 cents you inserted?'))
     pennies=int(input('How money 1 cents you inserted?'))
     avaliablemoney=(0.01*pennies)+(0.10*dimes)+(0.25*quanters)+(0.05*nickles)
     if avaliablemoney<main.MENU[drinktype]['cost']:
          print('Money is refunded. Not enough money insterted')

     elif avaliablemoney==main.MENU[drinktype]['cost']:
          print(f'Here is your coffee. Enjoy!')
          main.resources['water']-=main.MENU[drinktype]["ingredients"]['water']
          main.resources['coffee']-=main.MENU[drinktype]["ingredients"]['coffee']
          main.resources['money']+=avaliablemoney
          if drinktype == 'latte' or drinktype=='cappuccino':
             main.resources['milk']-=main.MENU[drinktype]["ingredients"]['milk']
     elif avaliablemoney>main.MENU[drinktype]['cost']: 
          change=(avaliablemoney)-(main.MENU[drinktype]['cost'])
          change=round(change, 3)
          avaliablemoney-=change
          main.resources['money']+=avaliablemoney
  
          print(f'Here is your coffee and change {change}$ . Enjoy!')
          main.resources['water']-=main.MENU[drinktype]["ingredients"]['water']
          main.resources['coffee']-=main.MENU[drinktype]["ingredients"]['coffee']
          if drinktype == 'latte' or drinktype=='cappuccino':
             main.resources['milk']-=main.MENU[drinktype]["ingredients"]['milk']
     


def report():
        print(f"""
              Water={main.resources['water']}\n
              Milk={main.resources['milk']}\n
              Coffee={main.resources['coffee']}\n
              Money={main.resources['money']}
              """)
        
def turnoff():
    print('Thanks for using DeLonghi. Good Day')


def makeespresso():
     espresso_water=main.MENU['espresso']["ingredients"]["water"]
     espresso_coffee=main.MENU['espresso']["ingredients"]["coffee"]
     machine_water=main.resources['water']
     machine_coffee=main.resources['coffee']
     if(machine_coffee<espresso_coffee):
          print("Sorry there is not enough coffee")
     elif(machine_water<espresso_water):
          print("Sorry there is not enough water")

     else:
          coins('espresso')
        #   print('Here is your espresso. Enjoy!')
        #   main.resources['water']-=espresso_water  
        #   main.resources['coffee']-=espresso_coffee  


def makelatte():
     latte_water=main.MENU['latte']["ingredients"]["water"]
     latte_coffee=main.MENU['latte']["ingredients"]["coffee"]
     machine_water=main.resources['water']
     machine_coffee=main.resources['coffee']
     machine_milk=main.resources['milk']
     latte_milk=main.MENU['latte']["ingredients"]["milk"]
     if(machine_coffee<latte_coffee):
          print("Sorry there is not enough coffee")
     elif(machine_water<latte_water):
          print("Sorry there is not enough water")
     elif(machine_milk<latte_milk):
          print("Sorry there is not enough milk")
     else:
          coins('latte')
        #   print('Here is your latte. Enjoy!')
        #   main.resources['water']-=latte_water  
        #   main.resources['coffee']-=latte_coffee  
        #   main.resources['milk']-=latte_milk  


def makecappuccino():
     cappuccino_water=main.MENU['cappuccino']["ingredients"]["water"]
     cappuccino_coffee=main.MENU['cappuccino']["ingredients"]["coffee"]
     machine_water=main.resources['water']
     machine_coffee=main.resources['coffee']
     machine_milk=main.resources['milk']
     cappuccino_milk=main.MENU['cappuccino']["ingredients"]["milk"]
     if(machine_coffee<cappuccino_coffee):
          print("Sorry there is not enough coffee")
     elif(machine_water<cappuccino_water):
          print("Sorry there is not enough water")
     elif(machine_milk<cappuccino_milk):
          print("Sorry there is not enough milk")
     else:
          coins('cappuccino')




while(1):
    user=str(input('What would you like? (espresso/latte/cappuccino): '))
    if user=='report':
         report()
    elif user=='turn off':
         turnoff()
         exit()
    elif user=='espresso':
         makeespresso()
         continue
    elif user=='latte':
         makelatte()
         continue

             