from selenium import webdriver
import pytest


@pytest.fixture()
def browser() -> webdriver:
    chrome_browser = webdriver.Chrome()
    return chrome_browser
