"""
This module communicates with Cisco Network Analytics and 
collects Host Pool data. 
"""
import requests


class Session_NA:
    """
    Object that authenticates against and making requests to 
    system Network Analytics (A)
    """
    def __init__(self, smc_user, smc_password, smc_host, smc_tenant_id):
        self.smc_user = smc_user
        self.smc_password = smc_password
        self.smc_host = smc_host
        self.smc_tenant_id = smc_tenant_id
        self.xsrf_header_name = "X-XSRF-TOKEN"
        self.api_session = requests.Session()
        self.login()

    def login(self) -> None:
        """
        Authentication function
        """
        url = f"https://{self.smc_host}/token/v2/authenticate"
        login_request_data = {"username": self.smc_user, "password": self.smc_password}
        response = self.api_session.request(
            "POST", url, verify=False, data=login_request_data
        )
        if response.status_code == 200:
            for cookie in response.cookies:
                if cookie.name == "XSRF-TOKEN":
                    self.api_session.headers.update(
                        {self.xsrf_header_name: cookie.value}
                    )
                    break
        else:
            print(
                f"Error: {response.status_code}"
            )

    def make_request(self, method, url, **kwargs):
        """
        REST API request function
        """
        response = self.api_session.request(method, url, **kwargs)
        return response
