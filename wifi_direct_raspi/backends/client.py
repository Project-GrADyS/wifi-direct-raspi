import abc
from typing import Type

class BaseClient(abc.ABC):

    def __init__(self, mac_address):
        self.mac_address = mac_address

    @abc.abstractmethod
    async def connect(self, mac_address) -> bool:
        raise NotImplementedError()
    
    @property
    @abc.abstractmethod
    def is_connected(self, mac_address) -> bool:
        raise NotImplementedError()
    
    @abc.abstractmethod
    async def disconnect(self) -> bool:
        raise NotImplementedError()
    
    @abc.abstractmethod
    async def get_group_status(self, group_id) -> bool:
        raise NotImplementedError()
    
def get_client() -> Type[BaseClient]:
    from wifi_direct_raspi.backends.raspberry.client import RaspiClient
    return RaspiClient
