from ..scanner import BaseScanner
from .methods.discovery import Discovery
from typing import Literal
import asyncio
import logging

logger = logging.getLogger(__name__)

class RaspiScanner(BaseScanner):

    def __init__(self, mode: Literal["virtual_push_button", "keypad"]):
        super(BaseScanner, self).__init__()
        self.mode = mode

    def start(self) -> None:
        self.found_devices = []

        #event_loop = asyncio.Event()

        Discovery.start()
    
    async def _received_handler(self) -> None:
        #listens to discovered devices asyncio
        discovered_devices = await Discovery.run_periodically(5, Discovery.discover_devices)
        print(discovered_devices)
        if discovered_devices != []:
            for device in discovered_devices:
                self.create_or_update_device(mac_address=device)
    
    '''
    def _handle_discovered_devices(self, mac_address: str) -> None:

        device = self.create_or_update_device(mac_address=mac_address)
    '''
    