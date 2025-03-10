import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture()
def index_url():
    return "https://qa-scooter.praktikum-services.ru"

@pytest.fixture()
def expected_url():
    return  "https://dzen.ru"