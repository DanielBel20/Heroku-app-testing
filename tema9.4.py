# 4. logati-va pe pagina https://the-internet.herokuapp.com/login
#    verificati ca s-a facut logare cu success 3 verificari

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s=Service('C:/Users/dan_1/PycharmProjects/Automationproject/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://the-internet.herokuapp.com/login')
username = driver.find_element(By.ID, 'username')
username.send_keys('tomsmith')
time.sleep(3.0)
password = driver.find_element(By.ID, 'password')
password.send_keys('SuperSecretPassword!')
time.sleep(3.0)
login_button = driver.find_element(By.CSS_SELECTOR, '#login > button > i')
login_button.click()
logout = driver.find_element(By.CSS_SELECTOR, '#content > div > a > i')
if logout.is_displayed():
    print("The Logout button is present so this is the first sign your login is successful!")
else:
    print("Your login does not look successful.")
green_message = driver.find_element(By.CSS_SELECTOR, '#flash')
if "You logged into a secure area!" in green_message.text:
    print("The 'You logged into a secure area!' message is present on the page so this is the second sign your login is successful!")
else:
    print("Your login does not look successful.")
secure_area = driver.find_element(By.CSS_SELECTOR, '#content > div > h2')
if secure_area.is_displayed():
    print("The 'Secure Area' message appears on the page so this is the third sign your login is successful!")
else:
    print("Your login does not look successful.")
invalid_password = driver.find_element(By.CSS_SELECTOR, '#flash')
if "Your password is invalid!" in invalid_password.text:
    print("Your login does not look successful.")
else:
    print("Your login looks successful!")
logout.click()
time.sleep(3.0)
driver.quit()
