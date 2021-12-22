from selenium.webdriver.common.by import By
class AddRemoveElementsPage:
    # locators
    TITLE = (By.CSS_SELECTOR, "div h3")
    ADD_ELEMENT_BUTTON = (By.CSS_SELECTOR, 'button[onclick="addElement()"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'button[onclick="deleteElement()"]')

    # URL
    URL = "https://the-internet.herokuapp.com/add_remove_elements/"
    def __init__(self, browser):
        self.browser = browser

    def loadPage(self):
        self.browser.get(self.URL)

    def clickAddButton(self):
        self.browser.find_element(*self.ADD_ELEMENT_BUTTON).click()
    def clickDeleteButton(self):
        self.browser.find_element(*self.DELETE_BUTTON).click()

    # ce incepe cu get este ok sa returneze un text
    def getTitlePage(self):
        return self.browser.find_element(*self.TITLE).text
    # cand vrem sa verificam ceva cu true sau false incepem cu is
    def isDeleteButtonDisplayed(self):
        return self.browser.find_element(*self.DELETE_BUTTON).is_displayed()
    #daca e get returneaza/ returneaza numarul de butoane delete care sunt pe pagina
    def getNumberOfDeleteButton(self):
        return len(self.browser.find_elements(*self.DELETE_BUTTON))
