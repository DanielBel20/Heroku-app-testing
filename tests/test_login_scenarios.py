from pages.login_page import LoginPage
from pages.secure_page import SecurePage


def test_check_if_login_is_successful(browser):
    """Check if login was made with success"""

    login_page = LoginPage(browser)
    secure_page = SecurePage(browser)
    login_page.load_page()
    login_page.user_name_field_fill('tomsmith')
    login_page.password_field_fill('SuperSecretPassword!')
    login_page.click_login_button()
    assert secure_page.is_logout_button_displayed(), 'Logout button is not displayed'
    assert secure_page.get_secure_area() == "Secure Area", 'Secure Area is not displayed'
    assert "You logged into a secure area!" in secure_page.get_flash_message(), "Your login does not look successful."
    assert "Secure Area" in secure_page.get_secure_area(), 'Your login does not look successful.'


def test_login_with_invalid_username(browser):
    """Attempt to login with invalid username"""

    login_page = LoginPage(browser)
    login_page.load_page()
    login_page.user_name_field_fill('tomsmithu')
    login_page.password_field_fill('SuperSecretPassword!')
    login_page.click_login_button()
    assert 'Your username is invalid!' in login_page.get_flash_message(), "Something is not working as it should"


def test_login_with_invalid_password(browser):
    """Attempt to login with invalid password"""

    login_page = LoginPage(browser)
    login_page.load_page()
    login_page.user_name_field_fill('tomsmith')
    login_page.password_field_fill('SuperSecretPasswordd!')
    login_page.click_login_button()
    assert "Your password is invalid!" in login_page.get_flash_message(), "Something is not working as it should"


def test_login_logout_successfully(browser):
    """Login-logout then check if it was performed successfully"""

    login_page = LoginPage(browser)
    logout = SecurePage(browser)
    login_page.load_page()
    login_page.user_name_field_fill('tomsmith')
    login_page.password_field_fill('SuperSecretPassword!')
    login_page.click_login_button()
    logout.click_logout_button()
    assert "https://the-internet.herokuapp.com/login" in browser.current_url, "Your current url is not ok"
    assert login_page.is_login_button_displayed(), "Login button is not available"
    assert "You logged out of the secure area!" in login_page.get_flash_message(), "The message is not displayed"
    assert login_page.is_login_page_message_displayed(), "The Login Page message is not displayed"


def test_login_without_username(browser):
    """Attempt to login without username"""

    login_page = LoginPage(browser)
    login_page.load_page()
    login_page.password_field_fill('SuperSecretPassword!')
    login_page.click_login_button()
    assert 'Your username is invalid!' in login_page.get_flash_message(), "Something is not working as it should"


def test_login_without_password(browser):
    """Attempt to login without password"""

    login_page = LoginPage(browser)
    login_page.load_page()
    login_page.user_name_field_fill('tomsmith')
    login_page.click_login_button()
    assert "Your password is invalid!" in login_page.get_flash_message(), "Something is not working as it should"
