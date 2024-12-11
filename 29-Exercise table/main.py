import requests
from datetime import datetime
import string
import os
from dotenv import load_dotenv

load_dotenv()

URL= os.getenv('URL')
APP_ID=os.getenv('APP_ID')
API_KEY=os.getenv('API_KEY')
SPREADSHEET_URL=os.getenv('SPREADSHEET_URL')


getquery=str(input('What you have done?'))

nlp={
    'query':getquery,
    'weight_kg':55,
    'height_cm':160,
    'age':22
}

headers={
    'x-app-id':APP_ID,
    'x-app-key':API_KEY
}


response=requests.post(URL,json=nlp,headers=headers)
newdata=response.json()['exercises']



today=datetime.today().strftime('%d/%m/%Y')

time=datetime.today().strftime('%H:%M:%S')


for key in newdata:
    data={
            "workout":  {
       
            "date": str(today),
            "time": time,
            "exercise": key['name'].capitalize(),
            "duration": int(key['duration_min']//60),
            "calories": key['nf_calories']
            
        
    }
    
    }
    sheet_response = requests.post(SPREADSHEET_URL, json=data)
    print(sheet_response.text)

  
    

    # request=requests.post(url=SPREADSHEET_URL,json=data)
    # 




    








