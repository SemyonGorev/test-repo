import requests
from Configs import API


# Получение проекта по id
def test_get_project():
    get_project = API()
    url = get_project.base_url + get_project.id
    headers = {
        "Content-Type": get_project.Content_Type,
        "Authorization": get_project.auth
        }
    response = requests.request("GET", url, headers=headers)
    print(response.text)
    assert response.status_code == 200
