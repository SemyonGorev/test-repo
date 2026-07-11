import requests
# Получение проекта по id


def test_get_project():
    url = "https://ru.yougile.com/api-v2/projects/" \
          "d201760c-0628-4688-9a7e-799691a2340b"
    headers = {
        "Content-Type": "application/json",
        "Authorization": ""
        }
    response = requests.request("GET", url, headers=headers)
    print(response.text)
    assert response.status_code == 200
