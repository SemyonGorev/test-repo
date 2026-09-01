from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_01_form():
    driver = webdriver.Edge()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    first_name = driver.find_element(By.NAME, 'first-name')
    first_name.send_keys("Иван")
    last_name = driver.find_element(By.NAME, 'last-name')
    last_name.send_keys("Петров")
    address = driver.find_element(By.NAME, 'address')
    address.send_keys("Ленина, 55-3")
    city = driver.find_element(By.NAME, 'city')
    city.send_keys("Москва")
    country = driver.find_element(By.NAME, 'country')
    country.send_keys("Россия")
    email = driver.find_element(By.NAME, 'e-mail')
    email.send_keys("test@skypro.com")
    phone_number = driver.find_element(By.NAME, 'phone')
    phone_number.send_keys("+7985899998787")
    job_position = driver.find_element(By.NAME, 'job-position')
    job_position.send_keys("QA")
    company = driver.find_element(By.NAME, 'company')
    company.send_keys("SkyPro")
    click_btn = driver.find_element(By.XPATH, "/html/body/main/div/form/div[5]/div/button")
    click_btn.click()
    zip_code_field = driver.find_element(By.ID, "zip-code")
    color_zip_code = zip_code_field.value_of_css_property('border-color')
    assert color_zip_code == "rgb(245, 194, 199)"
    fields = ["first-name",
              "last-name",
              "address",
              "city",
              "country",
              "e-mail",
              "phone",
              "job-position",
              "company"]
    for field_id in fields:
        field_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, field_id)))
        border_color = field_element.value_of_css_property("border-color")
        assert border_color == "rgb(186, 219, 204)", f"Поле {field_id} не подсвечено зеленым"
    driver.quit()


test_01_form()
