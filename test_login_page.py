from pages.login_page import LoginPage

def test_guest_can_see_login_page(browser):
    page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/ru/accounts/login/")
    page.open()
    page.should_be_login_page()
    page.should_be_login_form()
    page.should_be_register_form()
