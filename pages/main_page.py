from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    def go_to_login(self):
        self.click_when_clickable(MainPageLocators.LOGIN_LINK)
        self.should_url_contain("login")