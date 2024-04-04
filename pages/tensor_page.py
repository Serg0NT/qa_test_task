from pages.base_page import BasePage
from selenium.webdriver.common.by import By

block_selector = (By.XPATH, '//p[contains(text(), "Сила в людях")]')
about_people_selector = (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')


class TensorPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://tensor.ru/')

    def block(self):
        return self.find(block_selector)

    @property
    def about_people(self):
        return self.find(about_people_selector)

    def click_about_people(self):
        self.browser.execute_script('arguments[0].click()', self.about_people)

    def get_url(self):
        return self.browser.current_url
