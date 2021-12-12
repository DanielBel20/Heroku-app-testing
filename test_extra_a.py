# 4.https://the-internet.herokuapp.com/dropdown
# si pe pagina de heruko selectezi o optiune si apoi verifici ca e selectata cea care trebuie
# cu un asert

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test_drop_down():
    driver = webdriver.Chrome('C:/Users/dan_1/PycharmProjects/Automationproject/chromedriver.exe')
    driver.get('https://the-internet.herokuapp.com/dropdown')
    time.sleep(2)
    dropdown_list = Select(driver.find_element(By.ID, 'dropdown'))
    dropdown_list.select_by_value('1')
    time.sleep(2)
    option1 = driver.find_element(By.CSS_SELECTOR, "#dropdown > option:nth-child(2)")
    assert option1.is_selected(), "Option 1 is not selected"
    print("Option 1 is selected!")
    time.sleep(2)
    driver.quit()
