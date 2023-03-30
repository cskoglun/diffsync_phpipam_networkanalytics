"""
This module communicates with PHPIPAM and 
collects subnet data. 
"""
import requests
import base64


class Session_PI:
    """
    Object that authenticates against and making requests to 
    system PHPIPAM (B)
    """
    def __init__(self, user, password, host):
        self.user = user
        self.password = password
        self.host = host
        self.api_session = requests.Session()
        self.login()

    def login(self) -> str or bool:
        """
        Authentication function
        """
        url = f"http://{self.host}/api/diffsync/user"
        login_string = f"{self.user}:{self.password}"
        base64_string = base64.b64encode(login_string.encode("ascii")).decode("ascii")
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Basic {base64_string}",
        }
        payload = {}

        try:
            response = self.api_session.post(url=url, headers=headers, data=payload)
            data = response.json()
            token = data["data"]["token"]

            # update session headers
            self.api_session.headers.update({"token": token})

        except requests.exceptions.RequestException as e:
            token = None
            print(e)
            raise SystemError(e)
        return token

    def make_request(self, method, url, **kwargs):
        """
        REST API request function
        """
        response = self.api_session.request(method, url, **kwargs)
        return response
