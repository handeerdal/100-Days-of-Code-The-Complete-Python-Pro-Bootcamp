
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from fake_useragent import UserAgent
import time
from selenium.webdriver.common.keys import Keys
import time


    

# Use a random User-Agent to mimic a real browser
user_agent = UserAgent().random

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option('detach', True)
edge_options.add_argument(f"user-agent={user_agent}")
edge_options.add_argument('--disable-blink-features=AutomationControlled')


driver = webdriver.Edge(options=edge_options)

driver.get('https://orteil.dashnet.org/experiments/cookie/')
# buttonconstent= driver.find_element(By.CLASS_NAME,value='fc-button')
# buttonconstent.click()
# enbutton= driver.find_element(By.ID,value='langSelect-EN')
# enbutton.click()
cookie=driver.find_element(By.ID,value='cookie')

buyShipment=driver.find_element(By.ID,value='buyShipment')
buyAlchemylab=driver.find_element(By.ID,value='buyAlchemy lab')
buyPortal=driver.find_element(By.ID,value='buyPortal')
buyTimemachine=driver.find_element(By.ID,value='buyTime machine')
last_time = time.time()  

def checkmoney(money):
    # 'buyCursor' ID'sine sahip elementi bul
 
# <b> etiketini bul ve metnini al
    cursor_number = driver.find_element(By.XPATH, "//*[@id='buyCursor']/b").text.split()[-1] 
    grandma_number= driver.find_element(By.XPATH, '//*[@id="buyGrandma"]/b').text.split()[-1]
    factory_number= driver.find_element(By.XPATH, '//*[@id="buyFactory"]/b').text.split()[-1]
   
    ###################################################################################
    buyCursor=driver.find_element(By.ID,value='buyCursor')
    buyGrandma=driver.find_element(By.ID,value='buyGrandma')
    buyFactory=driver.find_element(By.ID,value='buyFactory')
    # grandma=driver.find_element(By.XPATH,value='//*[@id="buyGrandma"]/b/text()[2]').text


    if int(money)>=int(cursor_number):
        buyCursor.click()  # Tıklama işlemi
    elif int(money)>=int(grandma_number):
        buyGrandma.click()  # Tıklama işlemi
    elif int(money)>=int(factory_number):
        buyFactory.click()  # Tıklama işlemi
    
        


while 1:
    cookie.click()
    cookiemoney=driver.find_element(By.XPATH,value='//*[@id="money"]').text
    if time.time() - last_time >= 1:  # 5 saniye geçmiş mi?
        checkmoney(cookiemoney)  # Fonksiyonu çağır
        last_time = time.time()  # Zamanı güncelle





