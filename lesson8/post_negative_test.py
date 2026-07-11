import requests


# Создание проекта с пустым именем
def test_post_project_negative():
    url = "https://ru.yougile.com/api-v2/projects"
    payload = {
        "title": "",
        "users": {
                "35e6960b-10a5-4018-a0c0-e0447c8487c8": "worker"
                },
        "idempotencyKey": "string"
                }
    headers = {
                "Content-Type": "application/json",
                "Authorization": ""
                }
    response = requests.request("POST", url, json=payload, headers=headers)
    print(response.text)
    assert response.status_code == 400
