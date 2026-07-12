import requests
from Configs import API


# Изменение проекта
def test_put_project():
    put_project = API()
    url = put_project.base_url + put_project.id
    payload = {
        "deleted": False,
        "title": put_project.title,
        "users": {
            put_project.user: "worker"
                }
                }
    headers = {
                "Content-Type": put_project.Content_Type,
                "Authorization": put_project.auth
                }
    response = requests.request("PUT", url, json=payload, headers=headers)
    print(response.text)
    assert response.status_code == 200
