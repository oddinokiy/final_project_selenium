from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket is not empty"

    def should_has_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_TEXT), \
            "Basket empty text is absent"