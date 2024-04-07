from pages.base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

section_selector = (
    By.XPATH, '//img[@class="tensor_ru-About__block3-image new_lazy loaded"]')

selector_to_scroll = (
    By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[1]/p/a/span[1]')


class AboutPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://tensor.ru/about')

    def scroll_to(self):
        element = self.find(selector_to_scroll)
        element.location_once_scrolled_into_view

    def check_size_images(self, ):
        images = self.wait().until(
            EC.presence_of_all_elements_located(section_selector))
        return all(
            x.size['height'] == images[0].size['height'] for x in images) \
               and all(
            x.size['width'] == images[0].size['width'] for x in images)
