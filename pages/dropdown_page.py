from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class DropdownPage:
    DROPDOWN_LIST = (By.ID, 'dropdown')
    OPTION_1 = (By.CSS_SELECTOR, "#dropdown [value='1']")
    OPTION_2 = (By.CSS_SELECTOR, "#dropdown [value='2']")

    URL = "https://the-internet.herokuapp.com/dropdown"

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def select_option_1(self):
        Select(self.browser.find_element(*self.DROPDOWN_LIST)).select_by_value("1")

    def is_option_1_selected(self):
        return self.browser.find_element(*self.OPTION_1).is_selected()

    def select_option_2(self):
        Select(self.browser.find_element(*self.DROPDOWN_LIST)).select_by_value("2")

    def is_option_2_selected(self):
        return self.browser.find_element(*self.OPTION_2).is_selected()

