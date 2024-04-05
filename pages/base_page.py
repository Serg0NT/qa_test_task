from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, args):
        return self.browser.find_element(*args)
    #
    # def get_url(self):
    #     return self.browser.current_url

    def wait(self):
        return WebDriverWait(self.browser, 10, 1)
