""" 
This is the adapter to system PHPIPAM (B)
"""
import os
import json
from diffsync import DiffSync

from models import Device, Interface
from api_pi import Session_PI


USERNAME = os.environ.get("USERNAME_PI")
PASSWORD = os.environ.get("PASSWORD")
HOST = os.environ.get("NA_HOST")

session = Session_PI(USERNAME, PASSWORD, HOST)
# url = "http://10.101.1.202:80/api/diffsync/sections/"
# response = session.make_request(method="GET", url=url)
# pprint(response)


def get_subnets():
    """Function gets all subnet data in system PHPIPAM"""
    url = f"http://{HOST}/api/diffsync/subnets/"
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

    device = Device
    interface = Interface

    top_level = ["device"]
    nb = None

    def load(self):
        """Initialize the BackendB Object by loading some site, device and interfaces from DATA."""

        for device_name, device_data in DATA.items():
            device = self.device(name=device_name)
            self.add(device)

            for intf_name in device_data["subnets"]:
                intf = self.interface(name=intf_name, device_name=device_name)
                self.add(intf)
                device.add_child(intf)

    def sync_to_na(self):
        """TODO"""
