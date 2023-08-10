from selenium.webdriver.common.by import By


class AddRemoveElementsPage:
    # Locators
    TITLE = (By.CSS_SELECTOR, "h3")
    ADD_ELEMENT_BUTTON = (By.CSS_SELECTOR, 'button[onclick="addElement()"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'button[onclick="deleteElement()"]')

    # URL
    URL = "https://the-internet.herokuapp.com/add_remove_elements/"

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def click_add_button(self, number):
        for i in range(0, number):
            self.browser.find_element(*self.ADD_ELEMENT_BUTTON).click()

    def click_delete_button(self):
        self.browser.find_element(*self.DELETE_BUTTON).click()

    # what starts with get returns a text or a value
    def get_title(self):
        return self.browser.find_element(*self.TITLE).text

    # what start with is check True or False and in both cases returns
    def is_delete_button_displayed(self):
        return self.browser.find_element(*self.DELETE_BUTTON).is_displayed()

    def get_number_of_delete_buttons(self):
        return len(self.browser.find_elements(*self.DELETE_BUTTON))

