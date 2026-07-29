from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")
    driver.maximize_window()
    click_button = driver.find_element(By.NAME, 'custname')
    click_button.send_keys("Semyon")
    sleep(2)
    submit_btn = driver.find_element(By.XPATH, "/html/body/form/p[6]/button")
    submit_btn.click()
    sleep(2)
    print(driver.current_url) 
    driver.quit()


test_form_submission()
