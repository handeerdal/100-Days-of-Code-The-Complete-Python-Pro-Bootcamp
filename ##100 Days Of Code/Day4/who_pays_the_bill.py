import random
friends=['John','Jason','Sally','July']

random_person=random.randint(0,len(friends)-1)  #last index is included


print(f'{friends[random_person]} pays the bill!')