# 1. creati un file nou test_login si acolo faceti teste pt pagina de login
# a)logati-va pe pagina https://the-internet.herokuapp.com/login
# verificati ca s-a facut logare cu success 3 aserturi
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


def test_login_a():
    s = Service('C:/Users/dan_1/PycharmProjects/Automationproject/chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    driver.get('https://the-internet.herokuapp.com/login')
    username = driver.find_element(By.ID, 'username')
    username.send_keys('tomsmith')
    time.sleep(2)
    password = driver.find_element(By.ID, 'password')
    password.send_keys('SuperSecretPassword!')
    time.sleep(2)
    login_button = driver.find_element(By.CSS_SELECTOR, 'button')
    login_button.click()
    logout_button = driver.find_element(By.CSS_SELECTOR, 'a.button.secondary.radius')
    assert logout_button.is_displayed(), "The Logout button is not displayed. Your login does not look successful."
    print("The Logout button is present so this is the first sign your login is successful!")
    time.sleep(2)
    green_message = driver.find_element(By.CSS_SELECTOR, '#flash')
    assert "You logged into a secure area!" in green_message.text, "Your login does not look successful."
    print("The 'You logged into a secure area!' message is present on the page so this is the second sign your login "
          "is successful!")
    time.sleep(2)
    secure_area = driver.find_element(By.CSS_SELECTOR, '#content > div > h2')
    assert "Secure Area" in secure_area.text, "Your login does not look successful."
    print("The 'Secure Area' message appears on the page so this is the third sign your login is successful!")

    time.sleep(3)
    driver.quit()
