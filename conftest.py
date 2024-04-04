from selenium import webdriver
import pytest


@pytest.fixture()
def browser() -> webdriver:
    chrome_browser = webdriver.Chrome()
    # chrome_browser.implicitly_wait(10)
    return chrome_browser
