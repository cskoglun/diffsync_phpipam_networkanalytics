""" 
This is the adapter to system PHPIPAM (B)
"""
import os
import json
import yaml
from diffsync import DiffSync

from models import CustomField, Subnets
from api_pi import Session_PI


# USERNAME = os.environ.get("USERNAME_PI")
# PASSWORD = os.environ.get("PASSWORD")
# HOST = os.environ.get("PI_HOST")
cred_data = yaml.safe_load(open('credentials_chris.yaml'))["credentials"]
USERNAME_PI = cred_data["username_pi"]
PASSWORD_PI = cred_data["password_pi"]
HOST_PI = cred_data["host_pi"]

session = Session_PI(USERNAME_PI, PASSWORD_PI, HOST_PI)


def get_subnets():
    """Function gets all subnet data in system PHPIPAM"""
    url = f"http://{HOST_PI}/api/diffsync/subnets/"
    response = session.make_request(method="GET", url=url)
    data = json.loads(response.content)
    return data


def datasetfromphpipam():
    """
    Function creates a dictionary/dataset with necessary data
    -> {"custom_field" : [list of subnets]}
    """
    subnets = get_subnets()

    custom_names = []
    dataset = {}

    for item in subnets["data"]:
        if item["custom_Network_Analytics_Pool"] is None:
            pass
        else:
            custom_name = item["custom_Network_Analytics_Pool"]
            if custom_name not in custom_names:
                custom_names.append(custom_name)
            else:
                pass

    for item in custom_names:
        custom_field = item
        inner_dataset = {}
        dataset[custom_field] = inner_dataset
        subnetcidr = []
        for subnet_data in subnets["data"]:
            if subnet_data["custom_Network_Analytics_Pool"] == custom_field:
                subnet = subnet_data["subnet"] + "/" + subnet_data["mask"]
                subnetcidr.append(subnet)
                inner_dataset["subnets"] = subnetcidr
            else:
                pass

    return dataset

# Create dataset
DATA = datasetfromphpipam()


class BackendB(DiffSync):
    """DiffSync adapter implementation."""

    custom_field = CustomField
    subnets = Subnets

    top_level = ["custom_field"]

    type = "Backend B"

    nb = None

    def load(self):
        """Initialize the BackendB Object by loading custom field and subnets from DATA."""

        for custom_field, device_data in DATA.items():  # site_data.items():
            customfield = self.custom_field(name=custom_field)
            self.add(customfield)

            for intf_name in device_data["subnets"]:  # intf_name, desc
                intf = self.subnets(name=intf_name, custom_field=custom_field)          
                self.add(intf)
                customfield.add_child(intf)

    def sync_to_na(self):
        """TODO"""
