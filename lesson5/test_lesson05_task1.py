from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/")
    driver.maximize_window()
    element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, 'HTML form')))
    element.click()
    print(driver.current_url)
    driver.back()
    print(driver.current_url)
    driver.quit()


test_navigation()
