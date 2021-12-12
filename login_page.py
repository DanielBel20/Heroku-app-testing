from selenium.webdriver.common.by import By


class LoginPage:
    # locators
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, 'a.button.secondary.radius')
    GREEN_MESSAGE_RED_MESSAGE = (By.CSS_SELECTOR, '#flash')
    SECURE_AREA = (By.CSS_SELECTOR, '#content > div > h2')
    LOGIN_PAGE_MESSAGE = (By.CSS_SELECTOR, "div>h2")

    # URL
    URL = 'https://the-internet.herokuapp.com/login'

    def __init__(self, browser):
        self.browser = browser

    def loadPage(self):
        self.browser.get(self.URL)

    def userNameFieldFill(self, username):
        self.browser.find_element(*self.USERNAME).send_keys(username)

    def passwordFieldFill(self, password):
        self.browser.find_element(*self.PASSWORD).send_keys(password)

    def clickLoginButton(self):
        self.browser.find_element(*self.LOGIN_BUTTON).click()

    def clickLogoutButton(self):
        self.browser.find_element(*self.LOGOUT_BUTTON).click()

    def getGreenMessageOrRedMessage(self):
        return self.browser.find_element(*self.GREEN_MESSAGE_RED_MESSAGE).text

    def getSecureArea(self):
        return self.browser.find_element(*self.SECURE_AREA).text

    def isLogoutButtonDisplayed(self):
        return self.browser.find_element(*self.LOGOUT_BUTTON).is_displayed()

    def isLoginButtonDisplayed(self):
        return self.browser.find_element(*self.LOGIN_BUTTON).is_displayed()

    def isLoginPageMessageDisplayed(self):
        return self.browser.find_element(*self.LOGIN_PAGE_MESSAGE).is_displayed()


    # def clickAddButton(self):
    #     self.browser.find_element(*self.ADD_ELEMENT_BUTTON).click()
    # def clickDeleteButton(self):
    #     self.browser.find_element(*self.DELETE_BUTTON).click()
    #
    # # ce incepe cu get este ok sa returneze un text
    # def getTitlePage(self):
    #     return self.browser.find_element(*self.TITLE).text
    # # cand vrem sa verificam ceva cu true sau false incepem cu is
    # def isDeleteButtonDisplayed(self):
    #     return self.browser.find_element(*self.DELETE_BUTTON).is_displayed()
    # #daca e get returneaza/ returneaza numarul de butoane delete care sunt pe pagina
    # def getNumberOfDeleteButton(self):
    #     return len(self.browser.find_elements(*self.DELETE_BUTTON))