import logging
from .methods.connection import Connection

logger = logging.getLogger(__name__)

class RaspiClient:
    """
    Interface for connecting with a device
    """
    async def connect(self, mac_address: str, group_owner: bool = False) -> bool:
        logger.debug(f"Connecting to device {self.mac_address}")

        #Check if device is connected
        #if self._is_connected:

        await Connection.connect_to_device(mac_address)

