import pytest
from selenium import webdriver
from calcpage import Calculator
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тестирование калькулятора:")
@allure.description("Тест проверяет корректность работы калькулятора "
                    "с различными операциями.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator(driver):
    """
    Тест проверяет работу калькулятора с различными операциями.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.

    """
    calc_page = Calculator(driver)
    with allure.step("Открытие страницы калькулятора"):
        calc_page.open()
    with allure.step("Установка задержки 45 секунд"):
        calc_page.set_delay()
    with allure.step("Нажатие кнопки '7'"):
        calc_page.number_seven()
    with allure.step("Нажатие кнопки '+'"):
        calc_page.operator_plus()
    with allure.step("Нажатие кнопки '8'"):
        calc_page.number_eight()
    with allure.step("Нажатие кнопки '='"):
        calc_page.EQUALS_BUTTON()
    with allure.step("Получение результата с экрана калькулятора"):
        calc_page.get_result()
    with allure.step("Проверка результата"):
        assert calc_page.get_result() == "15"
