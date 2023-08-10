import time

from pages.add_remove_elements_page import AddRemoveElementsPage
from time import sleep

def test_add_remove_element(browser):
    """test if the number of Delete buttons is correct when you click Add Element"""

    add_remove = AddRemoveElementsPage(browser)
    add_remove.load_page()
    add_remove.click_add_button()
    add_remove.click_add_button()
    time.sleep(10)
    assert add_remove.get_number_of_delete_buttons() == 2, "There are more or less than 2 delete buttons"
    add_remove.click_delete_button()
    time.sleep(10)
    assert add_remove.get_number_of_delete_buttons() == 1, "There is more are less than 1 delete button"
