"""
This script defines the DiffSync models
"""

from typing import List
from diffsync import DiffSyncModel


class CustomField(DiffSyncModel):
    """Example model of a network Device."""

    _modelname = "custom_field"
    _identifiers = ("name",)
    _attributes = ()
    _children = {"subnets": "subnets"}

    name: str

    subnets: List = []
    #subnets: str


class Subnets(DiffSyncModel):
    """Example model of a network Interface."""

    _modelname = "subnets"
    _identifiers = ("custom_field", "name")
    _shortname = ("name",)
    _attributes = ()

    name: str
    custom_field: str
