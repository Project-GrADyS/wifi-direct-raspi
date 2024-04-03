import asyncio
import abc
from typing import (Any, Dict, List, Tuple, Type)
from .device import Device

class BaseScanner(abc.ABC):

    found_devices: Dict[str, Tuple[Device]]

    def __init__(self):
        super(BaseScanner, self).__init__()
        self.found_devices = {}

    def create_or_update_device(self, mac_address: str, name: str) -> Device:
        '''
        if self.found_devices != []:
            for device in self.found_devices:
                if device.mac_address == mac_address:
                    return device
        '''
        try:
            device, _ = self.found_devices[mac_address]
            device.name = name
        except KeyError:
            device = Device(mac_address, name)
        #device = Device(mac_address)
        #self.found_devices.append(device)
        self.found_devices[mac_address] = (device)
        return device

    @abc.abstractmethod
    async def start(self, mode: str) -> None:
        """Start scanning for devices"""
        raise NotImplementedError
    
    @abc.abstractmethod
    async def stop(self) -> None:
        """Stop scanning for devices"""
        raise NotImplementedError

def get_scanner() -> Type[BaseScanner]:
    from wifi_direct_raspi.backends.raspberry.scanner import RaspiScanner
    return RaspiScanner