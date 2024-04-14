from typing import List
from .device import Device

class Group:

    __slots__ = ("id", "name", "devices")

    def __init__(self, id: str, name: str, devices: List[Device]):
        self.id = id
        self.name = name
        self.devices = devices
    
    def __str__(self):
        return f"{self.id} : {self.name} : {self.devices}"
    
    def __repr__(self):
        return f"Group({self.id}, {self.name}, {self.devices})"