# data=[]

# with open('Python\\100 Days\\Day25\\weather_data.csv',mode='r') as file:
#     for line in file:
#         a=line
#         a=a.replace(',',' ')
#         data.append(a.strip())
        
# print(data)

import csv 
import pandas as pd

# with open('Python\\100 Days\\Day25\\weather_data.csv') as file:
#     data=csv.reader(file)
#     temperatures=[]
#     next(data)
#     for row in data:
#          temperatures.append(int(row[1]))


# print(temperatures)


df=pd.read_csv(r'C:\Users\snrpc\Desktop\Python\100 Days\Day25\weather_data.csv')
#print(df)

# temperatures_series= df['temp'] ##get column

# #print(temperatures_series)

# templist=temperatures_series.tolist()

# print(templist)
# avg=sum(templist)

# avg=round(avg/len(templist),2)

# print(avg)

# #######OR

# avg=temperatures_series.mean()
# print(avg)

# print(temperatures_series.max())

# ##get row

# maxrow=(df['temp']== df['temp'].max())
# print(maxrow)

# maxrow=df[df.temp== df.temp.max()]
# print(maxrow)
print(df)

#mondays temperature to fahrenheit


temperature=(df[df.day=='Monday'].temp)


#°F = (°C × 9/5) + 32

f=temperature*(9/5)+32
print(f)
