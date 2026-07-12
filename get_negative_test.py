import requests
from Configs import API


# Получение проекта c неправильным id
def test_get_negative():
    get_negative = API()
    url = get_negative.base_url + "x"
    headers = {
        "Content-Type": get_negative.Content_Type,
        "Authorization": get_negative.auth
            }
    response = requests.request("GET", url, headers=headers)
    print(response.text)
    assert response.status_code == 404
