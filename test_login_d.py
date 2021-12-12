# 1. creati un file nou test_login si acolofaceti teste pt pagina de login
# d) logati-va, click logout - > 4 aserturi (unul ca linkul pe care va redirectioneaza e ok, altul ca butonul de Login
# va apare , verificare ca va apare mesajul cu verde, si inca unul la care sa va ganditi voi)

from selenium import webdriver
import time
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


def test_login_d():
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
    logout_button.click()
    assert "https://the-internet.herokuapp.com/login" in driver.current_url, "Your current url is not ok"
    print("Your current url is ok")
    time.sleep(2)
    login_button = driver.find_element(By.CSS_SELECTOR, 'button>i')
    assert login_button.is_displayed(), "Login button is not available"
    print("Login button is available")
    time.sleep(2)
    green_message = driver.find_element(By.ID, 'flash-messages')
    assert "You logged out of the secure area!" in green_message.text, "The message is not displayed"
    print("The message appears")
    login_page_message = driver.find_element(By.CSS_SELECTOR, "div>h2")
    assert login_page_message.is_displayed(), "The Login Page message is not displayed"
    print("The Login Page message is displayed")
    time.sleep(3)
    driver.quit()
