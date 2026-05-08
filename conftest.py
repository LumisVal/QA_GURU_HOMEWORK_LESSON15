import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    options = Options()
    options.add_argument("--start-maximized")

    service = Service(r"C:\drivers\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)

    browser.config.driver = driver
    browser.config.base_url = "https://demoqa.com"
    browser.config.timeout = 10

    print("BASE URL =", browser.config.base_url)

    yield

    driver.quit()

    yield

    driver.quit()