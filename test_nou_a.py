# 2. adaugati un test nou la pagina pe care am facut-o la ora
# - dati de doua ori click pe butonul de add -> verificati ca va apar doua butoane
# - stergeti un buton  -> verificati ca va apare doar unul

from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def test_nou_a():
    driver = webdriver.Chrome('C:/Users/dan_1/PycharmProjects/Automationproject/chromedriver.exe')
    driver.get('https://the-internet.herokuapp.com/add_remove_elements/')
    time.sleep(2)
    add_button = driver.find_element(By.CSS_SELECTOR, 'div>button')
    add_button.click()
    time.sleep(2)
    add_button_2 = driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']")
    add_button_2.click()
    time.sleep(2)
    # check 2 delete buttons are displayed
    delete_button_1 = driver.find_element(By.CSS_SELECTOR, 'button[class="added-manually"]:nth-child(1)')
    assert delete_button_1.is_displayed() is True, "First delete button is not displayed"
    print("First delete button is displayed")
    delete_button_2 = driver.find_element(By.CSS_SELECTOR, 'button[class="added-manually"]:nth-child(2)')
    assert delete_button_2.is_displayed() is True, 'Second delete button is not displayed'
    print("Second delete button is displayed")
    time.sleep(2)
    delete_button_1.click()
    time.sleep(2)
    list = driver.find_elements(By.CSS_SELECTOR, "button[class='added-manually']")
    assert len(list) == 1, 'The are more delete buttons displayed'
    "Only one delete button is displayed"
    time.sleep(2)
    driver.quit()
