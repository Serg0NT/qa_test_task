import requests
import os
from pages.base import BasePage
from selenium.webdriver.common.by import By

plugin_selector = (By.CSS_SELECTOR, 'div[data-id="plugin"]')
windows_download_selector = (By.XPATH, '//*[text()="Скачать (Exe 8.30 МБ) "]')


class SbisDownload(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        """Opens the page """
        self.browser.get('https://sbis.ru/download/')

    @property
    def get_plugin(self):
        return self.find(plugin_selector)

    def click_plugin(self):
        self.get_plugin.click()

    def download_file(self):
        element = self.find(windows_download_selector)
        file_url = element.get_attribute("href")
        response = requests.get(file_url)
        response.raise_for_status()
        with open(r'E:\PythonProject\QA\qa_test_task\downloads\plugin.exe', 'wb') as file:
            file.write(response.content)

    def get_file_size(self):
        file_size = os.path.getsize(r'E:\PythonProject\QA\qa_test_task\downloads\plugin.exe')
        return round((file_size / 1024 / 1024), 2)

    def get_element_size(self):
        return round(float(self.find(windows_download_selector).text.split()[2]), 2)
