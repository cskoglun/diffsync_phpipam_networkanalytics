""" 
This is the adapter to system Network Analytics (A)
"""
import os
import json
import requests

from diffsync import DiffSync
from models import CustomField, Subnets
from api_na import Session_NA

try:
    requests.packages.urllib3.disable_warnings()
except:
    pass

# System credentials
HOST = os.environ.get("SMC_HOST")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
TENANT_ID = "301"


def create_data_set():
    ''' Function requests and creates dataset from System A: Network Analytics'''
    session = Session_NA(
        smc_password=PASSWORD, smc_host=HOST, smc_user=USERNAME, smc_tenant_id=TENANT_ID
    )
    url = (
        "https://" + HOST + "/smc-configuration/rest/v1/tenants/" + TENANT_ID + "/tags/"
    )

    tags_data = session.make_request(method="GET", url=url)
    tag_list = json.loads(tags_data.content)["data"]
    dataset = {}

    for item in tag_list:
        url = (
            "https://"
            + HOST
            + "/smc-configuration/rest/v1/tenants/"
            + TENANT_ID
            + "/tags/"
            + str(item["id"])
        )
        response = session.make_request("GET", url)

        if response.status_code == 200:

            tag_details = json.loads(response.content)
            if "ranges" not in tag_details["data"].keys():
                pass
            else:
                if tag_details["data"]["ranges"]:
                    custom_name = tag_details["data"]["name"]
                    inner_dataset = {}
                    inner_dataset["subnets"] = tag_details["data"]["ranges"]
                    dataset[custom_name] = inner_dataset

                else:
                    pass
    return dataset


DATA = create_data_set()

class BackendA(DiffSync):
    """DiffSync adapter implementation."""

    custom_field = CustomField
    subnets = Subnets

    top_level = ["custom_field"]

    type = "Backend A"

    nb = None

    def load(self):
        """Initialize the BackendA Object by loading custom field and subnets from DATA."""

        for custom_field, device_data in DATA.items():  
            customfield = self.custom_field(name=custom_field)
            self.add(customfield)

            for intf_name in device_data["subnets"]:  
                intf = self.subnets(name=intf_name, custom_field=custom_field)
                self.add(intf)
                customfield.add_child(intf)
