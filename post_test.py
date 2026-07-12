import requests
from Configs import API


# Создание проекта
def test_post_project():
    post_project = API()
    url = post_project.base_url
    payload = {
        "title": post_project.title,
        "users":
            {
                post_project.user: "worker"
            },
        "idempotencyKey": "string"
                }
    headers = {
                "Content-Type": post_project.Content_Type,
                "Authorization": post_project.auth
                }
    response = requests.request("POST", url, json=payload, headers=headers)
    print(response.text)
    assert response.status_code == 201
