from pages.login_page import LoginPage
from pages.secure_page import SecurePage


def test_login(browser):
    """Login and check if it was successful"""

    login = LoginPage(browser)
    logout = SecurePage(browser)
    login.load_page()
    login.user_name_field_fill('tomsmith')
    login.password_field_fill('SuperSecretPassword!')
    login.click_login_button()
    assert logout.is_logout_button_displayed(), "The Logout button is not displayed. Your login does not look successful."
    print("The Logout button is present so this is the first sign your login is successful!")
    assert "#5da423" == logout.is_button_green_or_red(), "Your login may not be successful"
    print(f"The color {logout.is_button_green_or_red()} match the color of the element")
    assert "You logged into a secure area!" in logout.get_flash_message(), "Your login does not look successful."
    print("The 'You logged into a secure area!' message is present on the page so this is the second sign your login "
          "is successful!")
    assert "Secure Area" in logout.get_secure_area(), "Your login does not look successful."
    print("The 'Secure Area' message appears on the page so this is the third sign your login is successful!")
