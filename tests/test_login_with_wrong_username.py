from pages.login_page import LoginPage


def test_login_with_wrong_username(browser):
    """Attempt to login with wrong user name and check error message"""

    login = LoginPage(browser)
    login.load_page()
    login.user_name_field_fill("tomsmithu")
    login.password_field_fill('SuperSecretPassword!')
    login.click_login_button()
    assert "Your username is invalid!" in login.get_flash_message(), "Error message is not displayed"
