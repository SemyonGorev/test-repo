import pytest
from selenium import webdriver
from shoppage import Shop_Log_In
from shoppage import Shop_Main_Page
from shoppage import Cart
from shoppage import Checkout_Page


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop(driver):
    shop_page = Shop_Log_In(driver)
    shop_page.open()
    shop_page.login()
    shop_page.password()
    shop_page.login_btn()
    shop_page = Shop_Main_Page(driver)
    shop_page.add_Sauce_Labs_Backpack()
    shop_page.add_Sauce_Labs_Tshirt()
    shop_page.add_Sauce_Labs_Onesie()
    shop_page.go_to_cart()
    shop_page = Cart(driver)
    shop_page.checkout()
    shop_page = Checkout_Page(driver)
    shop_page.First_name()
    shop_page.Last_name()
    shop_page.Postal()
    shop_page.Continue()
    shop_page.get_result()
    assert shop_page.get_result() == 'Total: $58.29'
