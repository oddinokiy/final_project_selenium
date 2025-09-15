from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        url = self.browser.current_url
        assert "login" in url , "Login URL is not correct"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        element = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        assert element, "Логин форма не найдена"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        sec_element = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        assert sec_element, "Form reqistration not found"



    def register_new_user(self,email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_1)
        password_field.send_keys(password)
        return_password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_2)
        return_password_field.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        reg_button.click()







