import requests
# Получение проекта c неправильным id


def test_get_negative():
    url = "https://ru.yougile.com/api-v2/projects/x"
    headers = {
        "Content-Type": "application/json",
        "Authorization":
            ""
            }
    response = requests.request("GET", url, headers=headers)
    print(response.text)
    assert response.status_code == 404
