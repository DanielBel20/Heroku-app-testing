from selenium.webdriver.common.by import By


class SecurePage:
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, 'a.button.secondary.radius')
    GREEN_MESSAGE_RED_MESSAGE = (By.CSS_SELECTOR, '#flash')
    SECURE_AREA = (By.CSS_SELECTOR, '#content > div > h2')
    # LOGIN_PAGE_MESSAGE = (By.CSS_SELECTOR, "div>h2")

    # URL
    URL = 'https://the-internet.herokuapp.com/secure'

    def __init__(self, browser):
        self.browser = browser

    def loadPage(self):
        self.browser.get(self.URL)

    def getSecureArea(self):
        return self.browser.find_element(*self.SECURE_AREA).text

    def isLogoutButtonDisplayed(self):
        return self.browser.find_element(*self.LOGOUT_BUTTON).is_displayed()

    def getGreenMessageOrRedMessage(self):
        return self.browser.find_element(*self.GREEN_MESSAGE_RED_MESSAGE).text

