from pages.base_page import BasePage
from selenium.webdriver.common.by import By

logo_tensor = (By.XPATH, '//a[@class="sbisru-Contacts__logo-tensor mb-12"]')


class SbisContacts(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://sbis.ru/contacts/')

    @property
    def button(self):
        return self.find(logo_tensor)

    def click_button(self):
        self.button.click()
