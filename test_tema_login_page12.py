from pages.login_page import LoginPage
from pages.secure_page import SecurePage


def test_check_if_login_is_successful(browser):
    login_page = LoginPage(browser)
    secure_page = SecurePage(browser)
    login_page.loadPage()
    login_page.userNameFieldFill('tomsmith')
    login_page.passwordFieldFill('SuperSecretPassword!')
    login_page.clickLoginButton()
    assert secure_page.isLogoutButtonDisplayed(), 'Logout button is not displayed'
    assert secure_page.getSecureArea() == "Secure Area", 'Secure Area is not displayed'
    assert "You logged into a secure area!" in secure_page.getGreenMessageOrRedMessage(), "Your login does not look successful."
    assert "Secure Area" in secure_page.getSecureArea(), 'Your login does not look successful.'


def test_login_with_invalid_username(browser):
    login_page = LoginPage(browser)
    login_page.loadPage()
    login_page.userNameFieldFill('tomsmithu')
    login_page.passwordFieldFill('SuperSecretPassword!')
    login_page.clickLoginButton()
    assert 'Your username is invalid!' in login_page.getGreenMessageOrRedMessage(), "Something is not working as it should"


def test_login_with_invalid_password(browser):
    login_page = LoginPage(browser)
    login_page.loadPage()
    login_page.userNameFieldFill('tomsmith')
    login_page.passwordFieldFill('SuperSecretPasswordd!')
    login_page.clickLoginButton()
    assert "Your password is invalid!" in login_page.getGreenMessageOrRedMessage(), "Something is not working as it should"


def test_login_logut_successfully(browser):
    login_page = LoginPage(browser)
    login_page.loadPage()
    login_page.userNameFieldFill('tomsmith')
    login_page.passwordFieldFill('SuperSecretPassword!')
    login_page.clickLoginButton()
    login_page.clickLogoutButton()
    assert "https://the-internet.herokuapp.com/login" in browser.current_url, "Your current url is not ok"
    assert login_page.isLoginButtonDisplayed(), "Login button is not available"
    assert "You logged out of the secure area!" in login_page.getGreenMessageOrRedMessage(), "The message is not displayed"
    assert login_page.isLoginPageMessageDisplayed(), "The Login Page message is not displayed"


def test_login_without_username(browser):
    login_page = LoginPage(browser)
    login_page.loadPage()
    login_page.passwordFieldFill('SuperSecretPassword!')
    login_page.clickLoginButton()
    assert 'Your username is invalid!' in login_page.getGreenMessageOrRedMessage(), "Something is not working as it should"


def test_login_without_password(browser):
    login_page = LoginPage(browser)
    login_page.loadPage()
    login_page.userNameFieldFill('tomsmith')
    login_page.clickLoginButton()
    assert "Your password is invalid!" in login_page.getGreenMessageOrRedMessage(), "Something is not working as it should"
