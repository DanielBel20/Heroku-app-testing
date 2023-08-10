import pytest
from pages.keypress_page import KeypressPage
import sys


@pytest.mark.skipif(sys.version_info < (3, 8), reason="Python version not supported")
def test_check_if_enter_is_pressed(browser):
    """Press ENTER key and check if it is pressed"""

    keypress_page = KeypressPage(browser)
    keypress_page.load_page()
    keypress_page.press_enter_key()
    assert 'You entered: ENTER' in keypress_page.get_green_message(), "The ENTER key is not pressed"


def test_check_if_backspace_is_pressed(browser):
    """Press BACKSPACE key and check if it is pressed"""

    keypress_page = KeypressPage(browser)
    keypress_page.load_page()
    keypress_page.press_backspace_key()
    assert 'You entered: BACK_SPACE' in keypress_page.get_green_message(), 'The BACK_SPACE key is not pressed'


def test_check_if_delete_is_pressed(browser):
    """Press DELETE key and check if it is pressed"""

    keypress_page = KeypressPage(browser)
    keypress_page.load_page()
    keypress_page.press_delete_key()
    assert 'You entered: DELETE' in keypress_page.get_green_message(), 'The DELETE key is not pressed'
