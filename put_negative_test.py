import requests
from Configs import API


# Изменение имени проекта на пустое
def test_put_negative():
    put_negative = API()
    url = put_negative.base_url + put_negative.id
    payload = {
        "deleted": False,
        "title": "",
        "users": {
                put_negative.user: "worker"
                }
                }
    headers = {
                "Content-Type": put_negative.Content_Type,
                "Authorization": put_negative.auth
                }
    response = requests.request("PUT", url, json=payload, headers=headers)
    print(response.text)
    assert response.status_code == 400
