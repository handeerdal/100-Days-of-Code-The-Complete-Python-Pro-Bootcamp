import turtle
import pandas as pd
screen=turtle.Screen()
screen.setup(width=1500,height=900)
screen.bgpic(r'C:\Users\snrpc\Desktop\Python\17-European Countries Guess Game\countries.gif')
screen.title('1914 EUROPEAN COUNTRIES GUESS GAME')

#for create database
# def screenclickfunc(x,y):
#     print(x,y)

# turtle.onscreenclick(screenclickfunc)

# turtle.mainloop()

countriesdict={

'Countries':['Italy','Spain','France','Portugal','Switzerland','Austria-Hungary','German Empire','Belgium','Luxembourg','United Kingdom','Netherlands','Denmark','Norway','Sweden','Romania','Serbia','Montenegro','Turkey','Bulgaria','albania','Greece'],
'X':[-12.0,-497.0,-239.0,-595.0,-131.0,112.0,-48.0,-172.0,-154.0,-298.0,-143.0,-47.0,74.0,-33.0,326.0,205.0,165.0,479.0,308.0,179.0,221.0],
'Y':[-196.0,-200.0,-50.0,-145.0,-28.0,-35.0,151.0,141.0,95.0, 246.0,191.0,311.0,364.0,428.0,-111.0,-170.0,-193.0,-298.0,-199.0,-257.0,-301.0]


}
countriesdict['Countries'] = [country.lower() for country in countriesdict['Countries']]

inputanswer='Answer'
gameison=True

df = pd.DataFrame(countriesdict)
counter=0
guessed=[]
notguessed = []

print(df)
while gameison:
    answer=screen.textinput(title=inputanswer,prompt='What is your guess?')

    if answer is None:
        newturtle=turtle.Turtle()
        newturtle.hideturtle()
        newturtle.penup()         
        newturtle.write(f'GAME OVER\nTotal Score={counter}', font=('Comic Sans MS', 15, 'bold'), align='center', move=True) 
        gameison=False


    elif answer.lower() in countriesdict['Countries']:
         newturtle=turtle.Turtle()
         newturtle.hideturtle()
         newturtle.penup()
         xlocation=int(df[df['Countries']==answer]['X'])
         ylocation=int(df[df['Countries']==answer]['Y'])
         newturtle.goto(xlocation,ylocation)
         newturtle.write(answer.capitalize(), font=('Arial', 10, 'bold'), align='center', move=True)
         counter+=1
         inputanswer = f"{counter}/{len(countriesdict['Countries'])} Correct"
         guessed.append(answer)


    if counter==len(countriesdict['Countries']):
        newturtle=turtle.Turtle()
        newturtle.hideturtle()
        newturtle.penup()         
        newturtle.write('WELL DONE', font=('Comic Sans MS', 15, 'bold'), align='center', move=True) 
        gameison=False
   

         

#notguessedcsv - for learn missed countries

countrylist=df['Countries'].to_list()

for country in countrylist:
    if country not in guessed:
        notguessed.append(country)
         
newdata=pd.DataFrame(notguessed)
newdata.to_csv('statestolearn.csv')





screen.exitonclick()
