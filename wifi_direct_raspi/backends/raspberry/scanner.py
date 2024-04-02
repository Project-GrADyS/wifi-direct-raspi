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

    async def start(self, callback=None) -> None:
        self.found_devices = []
        loop = asyncio.get_event_loop()
        self._stopped_loop = asyncio.Event()
        await self.discovery_instance.start()

        #self._task = asyncio.create_task(self._discover_task())
        #await self._task
        #self._task = asyncio.ensure_future(self.discover_task())
        #if callback:
            #asyncio.create_task(self.discover_task())
        #await self.discovery_instance.discover_devices()
        #await self.discovery_instance.run_periodically(5, Discovery.discover_devices)
    
    async def _discover_task(self):
        #até que não mande comando de stop
        while True:
            discovered_devices = await self.discovery_instance.discover_devices()
            if discovered_devices != []:
                for device in discovered_devices:
                    self.create_or_update_device(mac_address=device)
            await asyncio.sleep(5)
    
    #async def _run_callback_periodically(self, callback, interval):
        #while true:
            #await
    '''
    async def _received_handler(self) -> None:
        #listens to discovered devices asyncio
        discovered_devices = await self.discovery_instance.run_periodically(5, self.discovery_instance.discover_devices)
        #print(discovered_devices)
        if discovered_devices != []:
            for device in discovered_devices:
                self.create_or_update_device(mac_address=device)
    '''

    async def discover(self):
        self._task = asyncio.create_task(self._discover_task())
        await self._task
    
    async def stop(self):
        self._stop = True
        self._task.cancel()
        await self.discovery_instance.stop()
        '''
        discovered_devices = await self.discovery_instance.run_periodically(5, Discovery.discover_devices)
        #print(discovered_devices)
        if discovered_devices != []:
            for device in discovered_devices:
                self.create_or_update_device(mac_address=device)
        '''
    
    '''
    def _handle_discovered_devices(self, mac_address: str) -> None:

        device = self.create_or_update_device(mac_address=mac_address)
    '''
    