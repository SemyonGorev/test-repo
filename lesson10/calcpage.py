from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Calculator:

    DELAY_BUTTON = (By.ID, "delay")
    """
    Кнопка задержки
    """
    RESULT_SCREEN = (By.CSS_SELECTOR, '.screen')
    """
    Экран с результатом
    """

    def __init__(self, driver):
        """
        Конструктор класса Calculator.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 45)

    @allure.step("Открытие страницы калькулятора")
    def open(self):
        """
        Открывает страницу калькулятора.
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver"
            "-java/slow-calculator.html")

    @allure.step("Установка задержки 45 секунд")
    def set_delay(self):
        """
        Устанавливает задержку для выполнения операций на калькуляторе.
        """
        delay_input = self.wait.until(EC.presence_of_element_located(
            self.DELAY_BUTTON)
            )
        delay_input.clear()
        delay_input.send_keys("45")

    @allure.step("Нажатие кнопки '1'")
    def number_one(self):
        """
        Нажимает на кнопку '1'.
        """
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[9]').click()

    @allure.step("Нажатие кнопки '2'")
    def number_two(self):
        """
        Нажимает на кнопку '2'.
        """
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[10]').click()

    @allure.step("Нажатие кнопки '3'")
    def number_three(self):
        """
        Нажимает на кнопку '3'.
        """
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[11]').click()

    @allure.step("Нажатие кнопки '4'")
    def number_four(self):
        """
        Нажимает на кнопку '4'.
        """
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[5]').click()

    @allure.step("Нажатие кнопки '5'")
    def number_five(self):
        """
        Нажимает на кнопку '5'.
        """
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[6]').click()

    @allure.step("Нажатие кнопки '6'")
    def number_six(self):
        """
        Нажимает на кнопку '6'.
        """
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[7]').click()

    @allure.step("Нажатие кнопки '7'")
    def number_seven(self):
        """
        Нажимает на кнопку '7'.
        """
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()

    @allure.step("Нажатие кнопки '8'")
    def number_eight(self):
        """
        Нажимает на кнопку '8'.
        """
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()

    @allure.step("Нажатие кнопки '9'")
    def number_nine(self):
        """
        Нажимает на кнопку '9'.
        """
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[3]').click()

    @allure.step("Нажатие кнопки '0'")
    def number_zero(self):
        """
        Нажимает на кнопку '0'.
        """
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[13]').click()

    @allure.step("Нажатие кнопки '+'")
    def operator_plus(self):
        """
        Нажимает на кнопку '+'.
        """
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()

    @allure.step("Нажатие кнопки '-'")
    def operator_minus(self):
        """
        Нажимает на кнопку '-'.
        """
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[8]').click()

    @allure.step("Нажатие кнопки '/'")
    def operator_divide(self):
        """
        Нажимает на кнопку '/'.
        """
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[12]').click()

    @allure.step("Нажатие кнопки '*'")
    def operator_multiply(self):
        """
        Нажимает на кнопку '*'.
        """
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[16]').click()

    @allure.step("Нажатие кнопки 'Очистить'")
    def CLEAR_BUTTON(self):
        """
        Нажимает на кнопку 'Очистить'.
        """
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[1]/span').click()

    @allure.step("Нажатие кнопки '='")
    def EQUALS_BUTTON(self):
        """
        Нажимает на кнопку '='.
        """
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()

    @allure.step("Нажатие кнопки '.'")
    def dot(self):
        """
        Нажимает на кнопку '.'.
        """
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[14]').click()

    @allure.step("Получение результата с экрана калькулятора")
    def get_result(self):
        """
        Возвращает текущий результат с экрана калькулятора.

        :return: str — текст результата на экране калькулятора.
        """
        self.wait.until(EC.text_to_be_present_in_element
                        (self.RESULT_SCREEN, "15"))
        result_element = self.driver.find_element(*self.RESULT_SCREEN)
        return result_element.text
