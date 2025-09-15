from pages.base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):
    def add_to_basket(self):
         self.browser.find_element(*ProductPageLocators.BASKET_BUTTON).click()

    def should_be_product_name_correct(self):
        element = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name = element.text
        sec_element = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME)
        success_name = sec_element.text
        assert product_name == success_name, "Название товара в сообщении не совпадает с названием на странице"

    def should_be_price_correct(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        price_name = price.text
        message_price = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRICE)
        message_name = message_price.text
        assert price_name == message_name




   # Это второе задание!
    def get_product_name(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        prod_name = name.text
        return prod_name

    def get_product_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        prod_price = price.text
        return prod_price


    def get_success_message_name(self):
        mes_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME)
        text_for_name = mes_name.text
        return text_for_name

    def get_success_message_price(self):
        mes_price = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRICE)
        text_for_price = mes_price.text
        return text_for_price


    def have_to_be_product_name_correct(self):
        prod_name = self.get_product_name()
        success_name = self.get_success_message_name()
        assert prod_name == success_name, "Название товара не совпадает"

    def have_to_be_price_correct(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ProductPageLocators.SUCCESS_MESSAGE_PRICE)
        )
        message_price = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRICE).text
        assert product_price == message_price, "Price in message is wrong"




    def should_not_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
            "Success message is presented, but it should not be"





