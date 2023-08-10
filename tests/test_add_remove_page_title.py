from pages.add_remove_elements_page import AddRemoveElementsPage


def test_add_remove_title(browser):
    """Check if the title is displayed on the page"""

    add_remove = AddRemoveElementsPage(browser)
    add_remove.load_page()
    assert "Add/Remove Elements" in add_remove.get_title(), "title is not correct"

