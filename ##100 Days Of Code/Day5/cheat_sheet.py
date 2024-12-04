# import random
# integer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# random.shuffle(integer_list)

# max=0

# for i in integer_list:
#     if i>max:
#         max=i
# print(max)

# for i in range(1,10):
#     print(i)

for i in range(1,101):
    if (i%3==0) and (i%5==0):
        print("FizzBuzz")
    elif (i%3==0):
        print("Fizz")
    elif (i%5==0):
        print("Buzz")
    else:
        print(i)

