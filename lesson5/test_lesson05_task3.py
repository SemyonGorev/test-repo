from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/links/10")
    links = driver.find_elements(By.TAG_NAME, "a")
    print(len(links))
    assert len(links) == 9
    for link in links:
        assert link.is_displayed()
    assert "1" in links[0].text
    driver.quit()


test_multiple_elements()
