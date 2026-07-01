import pytest
from selenium import webdriver
from calcpage import Calculator

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_calculator(driver):
    calc_page = Calculator(driver)
    calc_page.open()
    calc_page.set_delay()
    calc_page.number_seven()
    calc_page.operator_plus()
    calc_page.number_eight()
    calc_page.EQUALS_BUTTON()
    calc_page.get_result()
    assert calc_page.get_result() == "15"

