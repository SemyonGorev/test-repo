class API:
    def __init__(self):
        self.base_url = "https://ru.yougile.com/api-v2/projects/"
        self.auth = "Bearer 5wLbiVIgeukerjL1L0eQ8al7cy6J806" \
            "PEQsgKQrZo7Vy2enbBoNUfEQxJj2xHOY-"
        self.id = "d201760c-0628-4688-9a7e-799691a2340b"
        self.Content_Type = "application/json"
        self.title = "Госуслуги"
        self.user = "35e6960b-10a5-4018-a0c0-e0447c8487c8"


config = API()
print(config.base_url)
