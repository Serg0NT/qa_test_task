import time
from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

banner_tensor_selector = (By.XPATH, '//a[@class="sbisru-Contacts__logo-tensor mb-12"]')
region_selector = (By.CSS_SELECTOR, 'span[class="sbis_ru-Region-Chooser__text sbis_ru-link"]')
list_partners_selector = (By.CSS_SELECTOR, 'div[data-qa="items-container"]')
expected_region_selector = (By.XPATH, '//*[@title="Камчатский край"]')
expected_url = '41-kamchatskij-kraj'

my_region = 'Свердловская обл.'
expected_region = 'Камчатский край'


class SbisContacts(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        """Opens the page """
        self.browser.get('https://sbis.ru/contacts/')

    @property
    def banner_tensor(self):
        """Finds the banner 'Тензор' """
        return self.find(banner_tensor_selector)

    def click_banner_tensor(self):
        """Clicks on the banner 'Тензор' """
        self.banner_tensor.click()

    @property
    def get_region(self):
        """Finds and gives current region"""
        return self.find(region_selector)

    def click_region(self):
        """clicks on a region to open a list of regions """
        self.get_region.click()

    def check_current_region(self) -> bool:
        """Compare current region and our region"""
        return self.get_region.text == my_region

    def get_list_partners(self):
        """Check list_partners is displayed"""
        return self.find(list_partners_selector)

    def click_expected_region(self):
        """Clicks on expected region"""
        self.wait().until(EC.element_to_be_clickable(expected_region_selector)).click()
        sleep(0.5)

    def check_expected_region(self) -> bool:
        return self.get_region.text == expected_region

    def check_expected_url_and_title(self):
        current_url = self.browser.current_url
        title = self.browser.title
        return expected_region in title.split(' — ') and expected_url in current_url.split('/')[-1].split('?')
