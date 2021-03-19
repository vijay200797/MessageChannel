from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import urllib.parse
driver = None
Link = "https://web.whatsapp.com/"
wait = None

class WhatsApp:
    def __init__(self):
        self.Login()
        
    def Login(self):
        print('Logging to whatsApp')
        global wait, driver, Link
        chrome_options = Options()
        chrome_options.add_argument('--user-data-dir=./User_Data')
        driver = webdriver.Chrome(options=chrome_options)
        wait = WebDriverWait(driver, 20)
        print("SCAN YOUR QR CODE FOR WHATSAPP WEB IF DISPLAYED")
        driver.get(Link)
        driver.maximize_window()
        print("QR CODE SCANNED")
    
    def SendMessage(self):
        print('Sending messsage')
    

    def send_message(self, name, msg, count):
        user_group_xpath = '//span[@title = "{}"]'.format(name)
        for retry in range(3):
            try:
                sleep(3)
                wait.until(EC.presence_of_element_located((By.XPATH, user_group_xpath))).click()
                break
            except Exception:
                print("retry:{} {} not found in your contact list".format(retry,name))
                if retry==2:return
        msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        for index in range(count):
            msg_box.send_keys(msg)
            driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
        print("Message send successfully.")

    def send_attachment(self, name, file_name):
        user_group_xpath = '//span[@title = "{}"]'.format(name)
        print("in send_attachment method")
        for retry in range(3):
            try:
                sleep(3)
                wait.until(EC.presence_of_element_located((By.XPATH, user_group_xpath))).click()
                break
            except Exception:
                print("retry:{} {} not found in your contact list".format(retry,name))
                if retry==2:return
        attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
        attachment_box.click()
        attachment = driver.find_element_by_xpath(
            '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        attachment.send_keys(file_name)
        sleep(5)
        send = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@data-icon="send-light"]')))
        send.click()
        print("File send successfully.")

    def send_message_to_unsavaed_contact(self, number,msg,count):
        # Reference : https://faq.whatsapp.com/en/android/26000030/
        print("In send_message_to_unsavaed_contact method")
        params = {'phone': str(number), 'text': str(msg)}
        end = urllib.parse.urlencode(params)
        final_url = Link + 'send?' + end
        print(final_url)
        driver.get(final_url)
        WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//div[@title = "Menu"]')))
        print("Page loaded successfully.")
        for retry in range(3):
            try:
                sleep(5)
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div[3]/button'))).click()
                break
            except Exception as e:
                print("Fail during click on send button.")
                if retry==2:return
        msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        for index in range(count-1):
            msg_box.send_keys(msg)
            driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
        print("Message sent successfully.")
        driver.close()

    def send_attachment_to_unsavaed_contact(self, number, file_name):
        print("In send_attachment_to_unsavaed_contact method")
        params = {'phone': str(number)}
        end = urllib.parse.urlencode(params)
        final_url = Link + 'send?' + end
        print(final_url)
        driver.get(final_url)
        WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//div[@title = "Menu"]')))
        print("Page loaded successfully.")
        for retry in range(3):
            try:
                sleep(5)
                wait.until(EC.presence_of_element_located((By.XPATH, '//div[@title = "Attach"]'))).click()
                break
            except Exception as e:
                print("Fail during click on Attachment button.")
                if retry==2:return
        attachment = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        attachment.send_keys(file_name)
        sleep(5)
        send = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@data-icon="send-light"]')))
        send.click()
        print("File sent successfully.")
        
