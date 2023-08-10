from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color


class LoginPage:

    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, 'a.button.secondary.radius')
    FLASH_MESSAGE = (By.ID, 'flash')
    LOGIN_PAGE_MESSAGE = (By.CSS_SELECTOR, "div>h2")

    URL = 'https://the-internet.herokuapp.com/login'

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def user_name_field_fill(self, username):
        self.browser.find_element(*self.USERNAME).send_keys(username)

    def password_field_fill(self, password):
        self.browser.find_element(*self.PASSWORD).send_keys(password)

    def click_login_button(self):
        self.browser.find_element(*self.LOGIN_BUTTON).click()

    def get_flash_message(self):
        return self.browser.find_element(*self.FLASH_MESSAGE).text

    def is_login_button_displayed(self):
        return self.browser.find_element(*self.LOGIN_BUTTON).is_displayed()

    def is_login_page_message_displayed(self):
        return self.browser.find_element(*self.LOGIN_PAGE_MESSAGE).text

    def is_button_green_or_red(self):
        rgb = self.browser.find_element(*self.FLASH_MESSAGE).value_of_css_property('background-color')
        button_color = Color.from_string(rgb).hex
        return button_color

    def get_current_url(self):
        return self.browser.current_url
