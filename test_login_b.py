# 1. creati un file nou test_login si acolo faceti teste pt pagina de login
# b) logati-va cu un username gresit -> verificati textul de la eroare

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


def test_login_b():
    s = Service('C:/Users/dan_1/PycharmProjects/Automationproject/chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    driver.get('https://the-internet.herokuapp.com/login')
    username = driver.find_element(By.ID, 'username')
    username.send_keys('tomsmithu')
    time.sleep(2)
    password = driver.find_element(By.ID, 'password')
    password.send_keys('SuperSecretPassword!')
    time.sleep(2)
    login_button = driver.find_element(By.CSS_SELECTOR, 'button')
    login_button.click()
    time.sleep(2)
    red_message = driver.find_element(By.CSS_SELECTOR, '#flash')
    assert "Your username is invalid!" in red_message.text, "Something is not working as it should"
    print("You tried to login with an invalid username")

    time.sleep(3)
    driver.quit()
