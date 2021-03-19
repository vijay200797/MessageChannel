from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime
import time
import openpyxl as excel

chrome_options = Options()
chrome_options.add_argumanet('--user-data-dir=./User_Data')
driver = webdriver.Chrome('./chromedriver', options=chrome_options)

def readContacts(fileName):
    lst = []
    file = excel.load_workbook(fileName)
    sheet = file.active
    firstCol = sheet['A']
    for cell in range(len(firstCol)):
        contact = (firstCol[cell].value).encode('utf-8')
        lst.append(contact)
    return lst


targets = readContacts("tt.xlsx")

driver.get("https://web.whatsapp.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 600)
wait5 = WebDriverWait(driver, 5)
msg = input('Enter the message : ')
#targets =['Deepika','Vijay1']
for target in targets:

    x_argSearchText= "//*[@id='side']/div[1]/div/label/div/div[2]"
    search = driver.find_element_by_xpath(x_argSearchText)
    print(target.decode('utf-8'))
    search.send_keys(target.decode('utf-8'))

    
    x_arg = '//span[contains(@title,' +'"' +target.decode('utf-8') + '"' +')]' #.decode('utf-8')
    if EC.presence_of_element_located((
        By.XPATH, x_arg)):
    
        group_title = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg)))
        group_title.click()

        x_argMessageText= "//*[@id='main']/footer/div[1]/div[2]/div/div[2]"
        message = driver.find_element_by_xpath(x_argMessageText)
        message.send_keys(msg)

        x_argSendButton="//*[@id='main']/footer/div[1]/div[3]/button/span"
        sendbutton = driver.find_element_by_xpath(x_argSendButton)    
        sendbutton.click()
        time.sleep(5)
    else:
        print('Contact Not Found'+target.decode('utf-8'))
driver.close()
