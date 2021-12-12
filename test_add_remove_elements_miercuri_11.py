from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def test_add_element():
    driver = webdriver.Chrome('C:/Users/dan_1/PycharmProjects/Automationproject/chromedriver.exe')
    driver.get('https://the-internet.herokuapp.com/add_remove_elements/')
    title = driver.find_element(By.CSS_SELECTOR, 'div h3')
    assert title.text == "Add/Remove Elements", "title is not correct"
    add_button = driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]')
    add_button.click()
    time.sleep(2)
    # check delete button is displayed
    delete_button = driver.find_element(By.CSS_SELECTOR, 'button[class="added-manually"]')
    assert delete_button.is_displayed() is True, 'Delete button is not displayed'
    time.sleep(2)
    driver.quit()
    print("test add element")
