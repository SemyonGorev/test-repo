from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_02_calc():
    driver = webdriver.Edge()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    input_delay = driver.find_element(By.CSS_SELECTOR, "#delay")
    input_delay.clear()
    input_delay.send_keys("45")
    button1 = driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]')
    button1.click()
    button2 = driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]')
    button2.click()
    button3 = driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]')
    button3.click()
    button4 = driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[15]')
    button4.click()
    result = WebDriverWait(driver, 45).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
    assert result
    driver.quit()


test_02_calc()
