from pages.dropdown_page import DropdownPage


def test_drop_down(browser):
    """Test if the dropdown options are correctly selected"""

    dropdown = DropdownPage(browser)
    dropdown.load_page()
    dropdown.select_option_1()
    assert dropdown.is_option_1_selected(), "Option 1 is not selected"
    dropdown.select_option_2()
    assert dropdown.is_option_2_selected(), "Option 2 is not selected"
