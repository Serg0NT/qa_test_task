from pages.base import BasePage
from selenium.webdriver.common.by import By

footer_download_selector = (By.CSS_SELECTOR, 'a[href="/download"]')


class SbisMain(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        """Opens the page """
        self.browser.get('https://sbis.ru/')

    @property
    def get_footer_element(self):
        return self.find(footer_download_selector)

    def scroll_to(self):
        element = self.get_footer_element
        element.location_once_scrolled_into_view

    def click_footer_element(self):
        self.get_footer_element.click()
