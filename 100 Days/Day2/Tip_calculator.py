print("Welcome to tip calculator")

total_bill = float(input('How much total bill? $'))
tip=float(input('How many percents you want to leave as tip? $'))
people=input('How many people splitting this tip?')
value= round(((total_bill * tip)/100)/float(people)+total_bill/float(people),2)
print(value)

