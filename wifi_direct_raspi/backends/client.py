import abc
from typing import Type
from ..backends.raspberry.client import WDRaspiClient

class BaseClient(abc.ABC):

    @abc.abstractmethod
    async def connect(self, **kwargs) -> bool:
        raise NotImplementedError()
    
    @abc.abstractmethod
    async def disconnect(self, **kwargs) -> bool:
        raise NotImplementedError()
    
    @abc.abstractmethod
    async def get_group_status(self, **kwargs) -> bool:
        raise NotImplementedError()
    
def get_client() -> Type[BaseClient]:
    return WDRaspiClient
