from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator:

    DELAY_BUTTON = (By.ID, "delay")
    RESULT_SCREEN = (By.CSS_SELECTOR, '.screen')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 45)

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver"
            "-java/slow-calculator.html")

    def set_delay(self):
        delay_input = self.wait.until(EC.presence_of_element_located(
            self.DELAY_BUTTON)
            )
        delay_input.clear()
        delay_input.send_keys("45")

    def number_one(self):
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[9]').click()

    def number_two(self):
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[10]').click()

    def number_three(self):
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[11]').click()

    def number_four(self):
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[5]').click()

    def number_five(self):
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[6]').click()

    def number_six(self):
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[7]').click()

    def number_seven(self):
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()

    def number_eight(self):
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()

    def number_nine(self):
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[3]').click()

    def operator_plus(self):
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()

    def operator_minus(self):
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[8]').click()

    def operator_divide(self):
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[12]').click()

    def operator_multiply(self):
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[16]').click()

    def CLEAR_BUTTON(self):
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[1]/span').click()

    def EQUALS_BUTTON(self):
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()

    def dot(self):
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[14]').click()

    def get_result(self):
        self.wait.until(EC.text_to_be_present_in_element
                        (self.RESULT_SCREEN, "15"))
        result_element = self.driver.find_element(*self.RESULT_SCREEN)
        return result_element.text
