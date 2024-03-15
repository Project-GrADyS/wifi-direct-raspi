import asyncio
import abc
from typing import (List, Type)
from .device import Device

class BaseScanner(abc.ABC):

    found_devices: List[Device]

    def create_or_update_device(self, mac_address: str) -> Device:
        for device in self.found_devices:
            if device.mac_address == mac_address:
                return device
            
        device = Device(mac_address=mac_address)
        self.found_devices.append(device)

        return device

    @abc.abstractmethod
    async def start(self, mode: str) -> None:
        """Start scanning for devices"""
        raise NotImplementedError
    
    @abc.abstractmethod
    async def stop(self) -> None:
        """Start scanning for devices"""
        raise NotImplementedError

def get_backend() -> Type[BaseScanner]:
    return 