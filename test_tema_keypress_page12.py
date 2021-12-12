from pages.keypress_page import KeypressPage


def test_check_if_enter_is_pressed(browser):
    keypress_page = KeypressPage(browser)
    keypress_page.loadPage()
    keypress_page.pressEnterOnPageField()
    assert 'You entered: ENTER' in keypress_page.getGreenMessage(), "The ENTER key is not pressed"


def test_check_if_back_space_is_pressed(browser):
    keypress_page = KeypressPage(browser)
    keypress_page.loadPage()
    keypress_page.pressShiftOnEmptyField()
    assert 'You entered: BACK_SPACE' in keypress_page.getGreenMessage(), 'The BACK_SPACE key is not pressed'


def test_check_if_delete_is_pressed(browser):
    keypress_page = KeypressPage(browser)
    keypress_page.loadPage()
    keypress_page.pressDeleteOnEmptyField()
    assert 'You entered: DELETE' in keypress_page.getGreenMessage(), 'The DELETE key is not pressed'
