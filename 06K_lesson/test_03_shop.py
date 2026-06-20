from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_03_shop():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    user_name = driver.find_element(By.ID, 'user-name')
    user_name.send_keys("standard_user")
    password = driver.find_element(By.ID, 'password')
    password.send_keys("secret_sauce")
    click_btn = driver.find_element(By.ID, "login-button")
    click_btn.click()
    sauce_labs_backpack = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    sauce_labs_backpack.click()
    sauce_labs_bolt_t_shirt = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    sauce_labs_bolt_t_shirt.click()
    sauce_labs_onesie = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
    sauce_labs_onesie.click()
    shopping_cart = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    shopping_cart.click()
    checkout = driver.find_element(By.ID, "checkout")
    checkout.click()
    first_name = driver.find_element(By.ID, 'first-name')
    first_name.send_keys("Sam")
    last_name = driver.find_element(By.ID, 'last-name')
    last_name.send_keys("Lensherr")
    postal_code = driver.find_element(By.ID, 'postal-code')
    postal_code.send_keys("123456")
    continue_btn = driver.find_element(By.ID, "continue")
    continue_btn.click()
    total_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
    print (total_element.text)
    result = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "summary_total_label"), "Total: $58.29"))
    assert result
    driver.quit()


test_03_shop()
