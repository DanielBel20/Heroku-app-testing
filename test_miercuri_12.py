from pages.add_remove_elements_page import AddRemoveElementsPage

# check title page is correct Add/Remove Elements


def test_page_title_is_correct(browser):
    add_remove_page = AddRemoveElementsPage(browser)
# load the page
    add_remove_page.loadPage()
# check title is correct
    assert add_remove_page.getTitlePage() == "Add/Remove Elements", "Page title is not ok"

# butonul de add element exista si este functional
def test_add_element_button(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    # load page
    add_remove_page.loadPage()
    # click pe butonul de Add
    add_remove_page.clickAddButton()
    # check delete button is displayed
    assert add_remove_page.isDeleteButtonDisplayed(), 'Delete button is not displayed'

def test_delete_button(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    # loadPage
    add_remove_page.loadPage()
    # clickAddButton
    add_remove_page.clickAddButton()
    # clickDeleteButton
    add_remove_page.clickDeleteButton()
    # check Delete Button is not displayed
    assert add_remove_page.getNumberOfDeleteButton() == 0, "Button is displayed on page"

# apasam de 10 ori add element


def test_button_x10(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    # loadPage
    add_remove_page.loadPage()
    # clickAddButton
    for i in range(10):
        add_remove_page.clickAddButton()
    assert add_remove_page.getNumberOfDeleteButton() == 10, 'There are less or more than 10 buttons'
