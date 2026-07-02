from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Shop_Log_In:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self):
        self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')

    def password(self):
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')

    def login_btn(self):
        self.driver.find_element(By.ID, 'login-button').click()


class Shop_Main_Page:
    def __init__(self, driver):
        self.driver = driver

    def add_Sauce_Labs_Backpack(self):
        self.driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-backpack').click()

    def add_Sauce_Labs_Bikelight(self):
        self.driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-bike-light').click()

    def add_Sauce_Labs_Tshirt(self):
        self.driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()

    def add_Sauce_Labs_Fleece_Jacket(self):
        self.driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-fleece-jacket').click()

    def add_Sauce_Labs_Onesie(self):
        self.driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-onesie').click()

    def add_Sauce_Labs_Red_Tshirt(self):
        self.driver.find_element(
            By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)').click()

    def go_to_cart(self):
        self.driver.find_element(
            By.CSS_SELECTOR, '.shopping_cart_link').click()


class Cart:
    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        self.driver.find_element(By.ID, 'checkout').click()


class Checkout_Page:
    TOTAL_VALUE = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 45)

    def First_name(self):
        self.driver.find_element(By.ID, 'first-name').send_keys('Semyon')

    def Last_name(self):
        self.driver.find_element(By.ID, 'last-name').send_keys('Gorev')

    def Postal(self):
        self.driver.find_element(By.ID, 'postal-code').send_keys('123456')

    def Continue(self):
        self.driver.find_element(By.ID, 'continue').click()

    def get_result(self):
        self.wait.until(EC.text_to_be_present_in_element
                        (self.TOTAL_VALUE, "Total: $58.29"))
        result_element = self.driver.find_element(*self.TOTAL_VALUE)
        return result_element.text
