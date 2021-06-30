from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import date
import os

#Hide popup from browser by use Option
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2 
})

email = '*****@gmail.com' #<-- input your mail
pwd = '******' #<-- input your password
people = '****' #<-- input your people name to Send text
botText = '' #<-- input your text
timeSend = '20:00:00' #<-- input your time in HH:MM:SS pattern

def noti_Action(): #all action happend from this !
    driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=option)
    driver.get('https://www.facebook.com/messages')
    pwd_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "pass")))
    email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "email")))
    login_btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "loginbutton")))

    

    #Login Action
    email_input.send_keys(email)
    pwd_input.send_keys(pwd)
    login_btn.click()

    #Search people
    search_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div/label/input")))
    search_input.send_keys(people)

    ptmp = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/ul/li[1]/ul/li[2]/div/a/div/div[2]/div/div/span/span/span")))
    ptmp.click()

    time.sleep(5)
    
    #Send message action
    message_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div/div/div")))
    message_input.send_keys(botText)

    send_btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div")))
    send_btn.click()
    
    time.sleep(5)
    driver.close()

while True:
    print(time.strftime("%H:%M:%S"))
    if(time.strftime("%H:%M:%S") == timeSend): #Check time to send text
        noti_Action()
    time.sleep(1)
    os.system('cls')

