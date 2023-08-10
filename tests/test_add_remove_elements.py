from pages.add_remove_elements_page import AddRemoveElementsPage


def test_page_title_is_correct(browser):
    """Check if page title is correct"""

    add_remove_page = AddRemoveElementsPage(browser)
    add_remove_page.load_page()
    assert add_remove_page.get_title() == "Add/Remove Elements", "Page title is not ok"


def test_add_element_button(browser):
    """Check if Add Element button is displayed and works"""

    add_remove_page = AddRemoveElementsPage(browser)
    add_remove_page.load_page()
    add_remove_page.click_add_button(1)
    assert add_remove_page.is_delete_button_displayed(), 'Delete button is not displayed'


def test_delete_button(browser):
    """Check if delete button is not displayed after clicking it"""

    add_remove_page = AddRemoveElementsPage(browser)
    add_remove_page.load_page()
    add_remove_page.click_add_button(1)
    add_remove_page.click_delete_button()
    assert add_remove_page.get_number_of_delete_buttons() == 0, "Button is displayed on page"


def test_presence_of_delete_button(browser):
    """Check the presence of Delete button after clicking on Add Element"""

    add_remove_page = AddRemoveElementsPage(browser)
    add_remove_page.load_page()
    add_remove_page.click_add_button(1)
    assert add_remove_page.get_number_of_delete_buttons() > 0, "Button is not displayed on page"


def test_button_x10(browser):
    """Test if 10 delete buttons are displayed after clicking 10 times on Add Element"""

    add_remove_page = AddRemoveElementsPage(browser)
    add_remove_page.load_page()
    add_remove_page.click_add_button(10)
    # for i in range(10):
    #     add_remove_page.click_add_button()
    assert add_remove_page.get_number_of_delete_buttons() == 10, 'There are less or more than 10 buttons'
