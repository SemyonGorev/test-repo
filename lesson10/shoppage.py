from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Shop_Log_In:
    def __init__(self, driver):
        """
        Конструктор класса Shop_Log_In.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Открытие страницы магазина")
    def open(self):
        """
        Открывает страницу магазина.
        """
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Ввод логина")
    def login(self):
        """
        Вводит логин.
        """
        self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')

    @allure.step("Ввод пароля")
    def password(self):
        """
        Вводит пароль.
        """
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')

    @allure.step("Нажатие на кнопку входа")
    def login_btn(self):
        """
        Нажимает на кнопку входа.
        """
        self.driver.find_element(By.ID, 'login-button').click()


class Shop_Main_Page:
    def __init__(self, driver):
        """
        Конструктор класса Shop_Main_Page.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Добавить в корзину 'Sauce Labs Backpack'")
    def add_Sauce_Labs_Backpack(self):
        """
        Добавляет в корзину 'Sauce Labs Backpack'.
        """
        self.driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-backpack').click()

    @allure.step("Добавить в корзину 'Sauce Labs Bikelight'")
    def add_Sauce_Labs_Bikelight(self):
        """
        Добавляет в корзину 'Sauce Labs Bikelight'.
        """
        self.driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-bike-light').click()

    @allure.step("Добавить в корзину 'Sauce Labs Bolt Tshirt'")
    def add_Sauce_Labs_Tshirt(self):
        """
        Добавляет в корзину 'Sauce Labs Bolt Tshirt''.
        """
        self.driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()

    @allure.step("Добавить в корзину 'Sauce Labs Fleece Jacket'")
    def add_Sauce_Labs_Fleece_Jacket(self):
        """
        Добавляет в корзину 'Sauce Labs Fleece Jacket''.
        """
        self.driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-fleece-jacket').click()

    @allure.step("Добавить в корзину 'Sauce Labs Onesie")
    def add_Sauce_Labs_Onesie(self):
        """
        Добавляет в корзину 'Sauce Labs Labs Onesie''.
        """
        self.driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-onesie').click()

    @allure.step("Добавить в корзину 'Sauce Labs Red Tshirt")
    def add_Sauce_Labs_Red_Tshirt(self):
        """
        Добавляет в корзину 'Sauce Labs Red Tshirt'.
        """
        self.driver.find_element(
            By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)').click()

    @allure.step("Открыть корзину")
    def go_to_cart(self):
        """
        Открывает корзину.
        """
        self.driver.find_element(
            By.CSS_SELECTOR, '.shopping_cart_link').click()


class Cart:
    def __init__(self, driver):
        """
        Конструктор класса Cart.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Нажатие на кнопку 'Checkout'")
    def checkout(self):
        """
        Нажимает на кнопку 'Checkout'
        """
        self.driver.find_element(By.ID, 'checkout').click()


class Checkout_Page:
    TOTAL_VALUE = (By.CLASS_NAME, "summary_total_label")
    """
    Общая сумма товаров
    """
    def __init__(self, driver):
        """
        Конструктор класса Cart.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 45)

    @allure.step("Отправка имени")
    def First_name(self):
        """
        Вводит имя
        """
        self.driver.find_element(By.ID, 'first-name').send_keys('Semyon')

    @allure.step("Отправка фамилии")
    def Last_name(self):
        """
        Вводит фамилию
        """
        self.driver.find_element(By.ID, 'last-name').send_keys('Gorev')

    @allure.step("Отправка почтового кода")
    def Postal(self):
        """
        Вводит почтовый код
        """
        self.driver.find_element(By.ID, 'postal-code').send_keys('123456')

    @allure.step("Нажатие кнопки 'Продолжить'")
    def Continue(self):
        """
        Нажимает на кнопку 'Продолжить'
        """
        self.driver.find_element(By.ID, 'continue').click()

    @allure.step("Получение результата")
    def get_result(self):
        """
        Возвращает общую суммму покупки.

        :return: str — текст результата на экране калькулятора.
        """
        self.wait.until(EC.text_to_be_present_in_element
                        (self.TOTAL_VALUE, "Total: $58.29"))
        result_element = self.driver.find_element(*self.TOTAL_VALUE)
        return result_element.text
