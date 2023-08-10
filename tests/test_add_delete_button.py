import pytest
from pages.add_remove_elements_page import AddRemoveElementsPage
import time


class TestAddRemoveElements:
    @pytest.mark.usefixtures("browser")
    def test_add_element(self, browser):
        """Check the title of the page and presence of delete button"""

        add_element = AddRemoveElementsPage(browser)
        add_element.load_page()
        add_element.is_delete_button_displayed()
        add_element.click_add_button(1)
        assert add_element.is_delete_button_displayed(), "Delete button is not displayed"

    def test_add_remove_element(self, browser):
        """test if the number of Delete buttons is correct when you click Add Element"""

        add_remove = AddRemoveElementsPage(browser)
        add_remove.load_page()
        add_remove.click_add_button(2)
        time.sleep(2)
        assert add_remove.get_number_of_delete_buttons() == 2, "There are more or less than 2 delete buttons"
        add_remove.click_delete_button()
        time.sleep(2)
        assert add_remove.get_number_of_delete_buttons() == 1, "There is more are less than 1 delete button"

    def test_button_x10(self, browser):
        """Test if 10 delete buttons are displayed after clicking 10 times on Add Element"""

        add_remove_page = AddRemoveElementsPage(browser)
        add_remove_page.load_page()
        add_remove_page.click_add_button(10)
        # for i in range(10):
        #     add_remove_page.click_add_button()
        assert add_remove_page.get_number_of_delete_buttons() == 10, 'There are less or more than 10 buttons'
