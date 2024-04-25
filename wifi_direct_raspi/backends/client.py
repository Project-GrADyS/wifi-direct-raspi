import abc
from typing import Type
from .device import Device

class BaseClient(abc.ABC):

    def __init__(self, device: Device):
        self.device = device

    @abc.abstractmethod
    async def connect(self) -> bool:
        raise NotImplementedError()
    
    @property
    @abc.abstractmethod
    def is_connected(self, device) -> bool:
        raise NotImplementedError()
    
    @abc.abstractmethod
    async def disconnect(self) -> bool:
        raise NotImplementedError()
    
    @abc.abstractmethod
    async def get_group_status(self, group) -> bool:
        raise NotImplementedError()
    
def get_client() -> Type[BaseClient]:
    from wifi_direct_raspi.backends.raspberry.client import RaspiClient
    return RaspiClient
