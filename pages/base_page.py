from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.timeout = timeout

    def open(self):
        self.browser.get(self.url)

    def click_when_clickable(self, by_locator):
        WebDriverWait(self.browser, self.timeout).until(
            EC.element_to_be_clickable(by_locator)
        ).click()

    def should_url_contain(self, text):
        WebDriverWait(self.browser, self.timeout).until(
            EC.url_contains(text)
        )
        assert text in self.browser.current_url.lower()