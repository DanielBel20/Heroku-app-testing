# 5.intra pe adresa ta de email, da click pe compose, completeaza cu adresa ta de email, un titlu, un text  trimite
# apoi dute la search si scrie titlu care l-ai dat, da enter verifici ca iti apare numa un mail si il stergi

from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import Select

option1 = Options()
option1.add_argument("--disable-notifications")

def test_email_check():
    driver = webdriver.Chrome('C:/Users/dan_1/PycharmProjects/Automationproject/chromedriver.exe', chrome_options=option1)
    driver.get('https://login.yahoo.com/')
    time.sleep(1)
    username = driver.find_element(By.ID, 'login-username')
    username.send_keys("dan_1st@yahoo.ro")
    username.send_keys(Keys.ENTER)
    time.sleep(1)
    password = driver.find_element(By.ID, 'login-passwd')
    password.send_keys("macarena2040")
    password.send_keys(Keys.ENTER)
    # remind_me_button = driver.find_element(By.CSS_SELECTOR, 'div>a:nth-child(2)')
    # remind_me_button.click()
    driver.maximize_window()
    time.sleep(4)
    mail_icon = driver.find_element(By.CSS_SELECTOR, "[class='ybar-icon-sprite _yb_emil2 _yb_aub9n']")
    mail_icon.click()
    time.sleep(2)
    compose = driver.find_element(By.CSS_SELECTOR, "nav>div>div>a")
    compose.click()
    time.sleep(3)
    input_receiver = driver.find_element(By.ID, 'message-to-field')
    input_receiver.send_keys("dan_1st@yahoo.com")
    time.sleep(2)
    subject = driver.find_element(By.CSS_SELECTOR, 'input[data-test-id="compose-subject"]')
    subject.send_keys("Acesta este un titlu")
    time.sleep(2)
    text_field = driver.find_element(By.CSS_SELECTOR, 'div[data-test-id="rte"]')
    text_field.click()
    time.sleep(1)
    text_field.send_keys("Acesta este un mesaj")
    time.sleep(2)
    send_button = driver.find_element(By.CSS_SELECTOR, '[data-test-id="compose-send-button"]')
    send_button.click()
    time.sleep(2)
    search_box = driver.find_element(By.CSS_SELECTOR, '[aria-label="Search box. Find messages, documents, photos or '
                                                      'people"]')
    search_box.send_keys("Acesta este un titlu")
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)
    lista = driver.find_elements(By.CSS_SELECTOR, '[data-test-id="message-subject"][title="Acesta este un titlu"]')
    assert len(lista) == 1, 'There are many e-mails with this subject'
    print("There is just one result with this subject")
    time.sleep(3)
    driver.quit()
