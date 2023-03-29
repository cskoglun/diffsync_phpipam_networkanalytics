"""
This script defines the DiffSync models
"""

from typing import List
from diffsync import DiffSyncModel


class Device(DiffSyncModel):
    """Example model of a network Device."""

    _modelname = "device"
    _identifiers = ("name",)
    _attributes = ()
    _children = {"interface": "interfaces"}

    name: str

    interfaces: List = []


class Interface(DiffSyncModel):
    """Example model of a network Interface."""

    _modelname = "interface"
    _identifiers = ("device_name", "name")
    _shortname = ("name",)
    _attributes = ()

    name: str
    device_name: str
