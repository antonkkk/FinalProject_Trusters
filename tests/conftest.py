import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Включение безглавого режима
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()
