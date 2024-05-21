from wifi_direct_raspi.backends.scanner import BaseScanner
from .methods.discovery import Discovery
from typing import Literal
import asyncio
import logging

logger = logging.getLogger(__name__)

class RaspiScanner(BaseScanner):

    def __init__(self, mode: Literal["virtual_push_button", "virtual_display", "keypad"]):
        super(BaseScanner, self).__init__()
        self.mode = mode
        self.discovery_instance = Discovery(self.mode)
        self._task = None
        self._stop = False

    async def start(self) -> None:
        self.found_devices = []
        #loop = asyncio.get_event_loop()
        #self._stopped_loop = asyncio.Event()
        self.discovery_instance.start()

        self._task = asyncio.create_task(self._discover_task())
        await self._task
    
    async def _discover_task(self):
        discovered_devices = []
        while discovered_devices == []:
            await asyncio.sleep(10)
            discovered_devices = await self.discovery_instance.discover_devices()
            if discovered_devices != []:
                for device in discovered_devices:
                    device_info = await self.discovery_instance.get_device_info(device)
                    self.create_or_update_device(mac_address=device, name=device_info["device_name"])
    
    async def stop(self):
        self._stop = True
        self._task.cancel()
        await self.discovery_instance.stop()
    