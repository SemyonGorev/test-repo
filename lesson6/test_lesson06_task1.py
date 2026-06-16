from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    start_btn = driver.find_element(By.XPATH, "//button[text()='Start']")
    start_btn.click()
    message = wait.until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="finish"]/h4'), "Hello World!")
    )
    driver.save_screenshot("screenshots/full_page.png")
    message_element = driver.find_element(By.XPATH, '//*[@id="finish"]/h4')
    assert message_element.text == "Hello World!"
    driver.quit()


test_dynamic_loading()
