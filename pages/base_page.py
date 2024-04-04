from selenium.webdriver.support.ui import WebDriverWait
class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, args):
        return self.browser.find_element(*args)

    def wait(self):
        return WebDriverWait(self.browser, 10, 2)

    # def find_elements(self, args):
    #     return self.browser.find_elements(*args)
