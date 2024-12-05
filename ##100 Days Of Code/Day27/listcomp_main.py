numbers=[1,2,3]

newnum=[i for i in numbers]

print(newnum)

name='Angela'

newname=[i for i in name]
print(newname)

newlist=[i*2 for i in range(1,5)]

print(newlist)


names=['Angela','John','Courtney']

chosennames=[a.upper() for a in names if len(a)>5]

print(chosennames)