from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class KeypressPage:
    # locators
    FIELD = (By.CLASS_NAME, 'no-js')
    GREEN_MESSAGE = (By.ID, 'result')
    EMPTY_FIELD = (By.ID, 'target')

    # URL
    URL = 'https://the-internet.herokuapp.com/key_presses?'

    def __init__(self, browser):
        self.browser = browser

    def loadPage(self):
        self.browser.get(self.URL)

    def pressEnterOnPageField(self):
        self.browser.find_element(*self.FIELD).send_keys(Keys.ENTER)

    def pressShiftOnEmptyField(self):
        self.browser.find_element(*self.EMPTY_FIELD).send_keys(Keys.BACKSPACE)

    def pressDeleteOnEmptyField(self):
        self.browser.find_element(*self.EMPTY_FIELD).send_keys(Keys.DELETE)

    def getGreenMessage(self):
        return self.browser.find_element(*self.GREEN_MESSAGE).text



