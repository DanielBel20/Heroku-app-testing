from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class KeypressPage:

    FIELD = (By.CLASS_NAME, 'no-js')
    GREEN_MESSAGE = (By.ID, 'result')
    EMPTY_FIELD = (By.ID, 'target')

    URL = 'https://the-internet.herokuapp.com/key_presses?'

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def press_enter_key(self):
        self.browser.find_element(*self.FIELD).send_keys(Keys.ENTER)

    def press_backspace_key(self):
        self.browser.find_element(*self.EMPTY_FIELD).send_keys(Keys.BACKSPACE)

    def press_delete_key(self):
        self.browser.find_element(*self.EMPTY_FIELD).send_keys(Keys.DELETE)

    def get_green_message(self):
        return self.browser.find_element(*self.GREEN_MESSAGE).text
