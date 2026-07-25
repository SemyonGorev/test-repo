import pytest
from selenium import webdriver
from shoppage import Shop_Log_In
from shoppage import Shop_Main_Page
from shoppage import Cart
from shoppage import Checkout_Page
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тестирование магазина:")
@allure.description("Тест проверяет корректность работы онлайн-магазина "
                    "с различными покупками.")
@allure.feature("Магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(driver):
    """
    Тест проверяет работу магазина с различными покупками.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.

    """
    shop_page = Shop_Log_In(driver)
    with allure.step("Открытие страницы магазина"):
        shop_page.open()
    with allure.step("Ввод логина"):
        shop_page.login()
    with allure.step("Ввод пароля"):
        shop_page.password()
    with allure.step("Нажатие на кнопку входа"):
        shop_page.login_btn()
    shop_page = Shop_Main_Page(driver)
    with allure.step("Добавить в корзину 'Sauce Labs Backpack'"):
        shop_page.add_Sauce_Labs_Backpack()
    with allure.step("Добавить в корзину 'Sauce Labs Bolt Tshirt'"):
        shop_page.add_Sauce_Labs_Tshirt()
    with allure.step("Добавить в корзину 'Sauce Labs Onesie'"):
        shop_page.add_Sauce_Labs_Onesie()
    with allure.step("Открыть корзину"):
        shop_page.go_to_cart()
    shop_page = Cart(driver)
    with allure.step("Нажатие на кнопку 'Checkout"):
        shop_page.checkout()
    shop_page = Checkout_Page(driver)
    with allure.step("Отправка имени"):
        shop_page.First_name()
    with allure.step("Отправка фамилии"):
        shop_page.Last_name()
    with allure.step("Отправка почтового кода"):
        shop_page.Postal()
    with allure.step("Нажатие кнопки 'Продолжить'"):
        shop_page.Continue()
    with allure.step("Получение результата"):
        shop_page.get_result()
    assert shop_page.get_result() == 'Total: $58.29'
