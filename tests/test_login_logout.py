from pages.login_page import LoginPage
from pages.secure_page import SecurePage


def test_login_logout(browser):
    """login-logout and test if the logout was made successfully"""

    login = LoginPage(browser)
    logout = SecurePage(browser)
    login.load_page()
    login.user_name_field_fill('tomsmith')
    login.password_field_fill('SuperSecretPassword!')
    login.click_login_button()
    logout.click_logout_button()
    assert "https://the-internet.herokuapp.com/login" in login.get_current_url(), "Your current url is not ok"
    assert login.is_login_button_displayed(), "Login button is not displayed"
    assert "You logged out of the secure area!" in login.get_flash_message(), "Your message is not as expected"
    assert "Login Page" in login.is_login_page_message_displayed(), "'Login Page' message is not displayed"

