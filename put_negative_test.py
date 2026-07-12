import requests


# Изменение имени проекта на пустое
def test_put_negative():
    url = "https://ru.yougile.com/api-v2/projects/" \
        "d201760c-0628-4688-9a7e-799691a2340b"
    payload = {
        "deleted": False,
        "title": "",
        "users": {
                "35e6960b-10a5-4018-a0c0-e0447c8487c8": "worker"
                }
                }
    headers = {
                "Content-Type": "application/json",
                "Authorization": ""
                }
    response = requests.request("PUT", url, json=payload, headers=headers)
    print(response.text)
    assert response.status_code == 400
