import requests
from Configs import API


# Создание проекта с пустым именем
def test_post_project_negative():
    post_project_negative = API()
    url = post_project_negative.base_url
    payload = {
        "title": "",
        "users": {
                post_project_negative.user: "worker"
                },
        "idempotencyKey": "string"
                }
    headers = {
                "Content-Type": post_project_negative.user,
                "Authorization": post_project_negative.auth
                }
    response = requests.request("POST", url, json=payload, headers=headers)
    print(response.text)
    assert response.status_code == 400
