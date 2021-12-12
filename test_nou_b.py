# 3.https://the-internet.herokuapp.com/key_presses?
#  apasati eneter si verificati mesajul cu verde ce va apare

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def test_press_enter():
    driver = webdriver.Chrome('C:/Users/dan_1/PycharmProjects/Automationproject/chromedriver.exe')
    driver.get('https://the-internet.herokuapp.com/key_presses?')
    time.sleep(2)
    field = driver.find_element(By.CLASS_NAME, 'no-js')
    field.send_keys(Keys.ENTER)
    time.sleep(2)
    green_message = driver.find_element(By.ID, 'result')
    assert green_message.is_displayed(), 'Something went wrong'
    time.sleep(2)
    print('The message is ', green_message.text)
    time.sleep(2)
    driver.quit()
