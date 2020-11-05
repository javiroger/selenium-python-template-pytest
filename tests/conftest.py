import os
import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(params=['chrome_browser', 'firefox_browser'])
def browser(request):
    return request.getfixturevalue(request.param)


@pytest.fixture
def chrome_browser():
    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("disable-infobars")

    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

    driver.maximize_window()
    driver.implicitly_wait(60)
    driver.get("https://www.google.com/")

    yield driver

    driver.quit()


@pytest.fixture
def firefox_browser():
    options = FirefoxOptions()
    options.headless = True
    
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    
    driver.maximize_window()
    driver.implicitly_wait(60)
    driver.get("https://www.google.com/")

    yield driver

    driver.quit()