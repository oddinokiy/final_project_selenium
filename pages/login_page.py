from .base_page import BasePage

class LoginPage(BasePage):
    def should_be_login_page(self):
        # проверка, что мы реально на странице логина
        assert "login" in self.browser.current_url.lower()

    def should_be_login_form(self):
        assert self.browser.find_element("id", "login_form")

    def should_be_register_form(self):
        assert self.browser.find_element("id", "register_form")