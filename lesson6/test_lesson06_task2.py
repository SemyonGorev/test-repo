from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.get("https://gitflic.ru/")
    driver.add_cookie({
           "name": "SESSION",
           "value": "YWMwY2M4NDItZWQxYy00NjM4LWIwY2UtOWM0ZmQ2Mjc4MmU3",
           "domain": "gitflic.ru"
           })
    driver.refresh()
    driver.get("https://gitflic.ru/user/sam_lensherr1")
    url1 = driver.execute_script("return window.location.href;")
    print(f"URL1: {url1}")
    driver.delete_all_cookies()
    driver.add_cookie({
           "name": "SESSION",
           "value": "NWIzMWFlNjQtMDYwYy00ZjhkLWEzZWMtOTJkOTM1MTQ2ODkx",
           "domain": "gitflic.ru"
           })
    driver.refresh()
    driver.get("https://gitflic.ru/user/sam_lensherr2")
    url2 = driver.execute_script("return window.location.href;")
    print(f"URL2: {url2}")
    assert not url1 == url2 
    driver.quit()
     

test_session_storage_auth()
