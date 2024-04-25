import logging
from .methods.connection import Connection
from ..device import Device
from ..group import Group
from .methods.group_management import GroupManagement

logger = logging.getLogger(__name__)

class RaspiClient:
    """
    Interface for connecting with a device
    """

    def __init__(self, device: Device):
        self.device = device
        self.group_owner = None
        self.group = None
        self.connection_instance = Connection(self.device.mac_address)
        self.group_management_instance = GroupManagement()

    async def connect(self) -> bool:
        logger.debug(f"Connecting to device {self.device.mac_address}")

        """
        There are 3 ways to create a group: standard, autonomous and persistent

        Standart: P2P devices discover each other and negotiate who will act as P2P GO
        Autonomous: the device create their own group and invites peers to join
        Persistent: devices recall if they've had a previous connection with persistent flag set
        """

        #Check if device is connected
        #if self._is_connected:
        await self.connection_instance.connect_to_device(self.device.mac_address)
    
    async def _create_autonomous_group(self):
        self.group_management_instance.set_autonomous_group()
    
    async def _invite_device_to_group(self):
        # if the device A is a group owner and already has a group, it invites device B to group
        pass
    
    async def disconnect(self):
        pass



