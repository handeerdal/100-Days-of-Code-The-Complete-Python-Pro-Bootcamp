# Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill. Use the `input()` function to get a user's preferences and then add up the total for their order and tell them how much they have to pay.

# Small pizza (S): $15

# Medium pizza (M): $20

# Large pizza (L): $25

# Add pepperoni for small pizza (Y or N): +$2

# Add pepperoni for medium or large pizza (Y or N): +$3

# Add extra cheese for any size pizza (Y or N): +$1

print('Welcome to Python Pizza')
pizza_type=input('Which size do you want S M L ')
peperoni=input('Pepperoni? Y or N ')

bill=0

if(pizza_type=='S'):
    bill+=15
    if(peperoni=='Y'):
        bill+=2
elif(pizza_type=='M'):
    if(peperoni=='Y'):
        bill+=3
elif(pizza_type=='L'):
    if(peperoni=='Y'):
        bill+=3
if(input(' do you want cheese? Y or N')=='Y'):
    bill+=1
else:
    print("you didn't choose correctly")

print(f'your bill is {bill}')

    
