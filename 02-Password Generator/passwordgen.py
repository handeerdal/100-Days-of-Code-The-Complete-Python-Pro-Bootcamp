import string
import random

print('Welcome to Password Generator')
num_letter=int(input('How many letters do you want'))
num_num=int(input('How many numbers do you want'))
num_sym=int(input('How many symbols do you want'))


letters=['']*num_letter
numbers=[0]*num_num
symbols=['']*num_sym



alphabet=string.ascii_letters
number=string.digits
symbol=string.punctuation



for i in range(0,num_letter):
    letters[i]=random.choice(alphabet)
for i in range(0,num_sym):
    symbols[i]=random.choice(symbol)
for i in range(0,num_num):
    numbers[i]=random.choice(number)

    
password=letters+numbers+symbols

finallpass=''
for i in range(0,len(password)):
    finallpass+= password[i]

print(f'your password is {finallpass}')
print(len(finallpass))