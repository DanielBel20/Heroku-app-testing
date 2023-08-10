from pages.login_page import LoginPage


def test_login_with_wrong_password(browser):
    """Attempt to login with wrong password and check error message"""

    login = LoginPage(browser)
    login.load_page()
    login.user_name_field_fill('tomsmith')
    login.password_field_fill('SuperSecretPasswordd!')
    login.click_login_button()
    assert "Your password is invalid!" in login.get_flash_message(), "Something is not working as it should"
