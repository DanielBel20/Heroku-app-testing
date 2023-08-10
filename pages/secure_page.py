from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color


class SecurePage:
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, 'a.button.secondary.radius')
    FLASH_MESSAGE = (By.ID, 'flash')
    SECURE_AREA = (By.CSS_SELECTOR, '#content h2')

    URL = 'https://the-internet.herokuapp.com/secure'

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def get_secure_area(self):
        return self.browser.find_element(*self.SECURE_AREA).text

    def is_logout_button_displayed(self):
        return self.browser.find_element(*self.LOGOUT_BUTTON).is_displayed()

    def get_flash_message(self):
        return self.browser.find_element(*self.FLASH_MESSAGE).text

    def is_button_green_or_red(self):
        rgb = self.browser.find_element(By.ID, 'flash').value_of_css_property('background-color')
        button_color = Color.from_string(rgb).hex
        return button_color

    def click_logout_button(self):
        self.browser.find_element(*self.LOGOUT_BUTTON).click()
