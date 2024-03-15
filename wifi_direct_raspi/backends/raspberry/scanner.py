from ..scanner import BaseScanner
from typing import Literal
import asyncio

class RaspiScanner(BaseScanner):

    def __init__(self, mode: Literal["virtual_push_button", "keypad"]):
        super(BaseScanner, self).__init__()
        self.mode = mode

    async def start(self) -> None:
        self.found_devices = []

        event_loop = asyncio.Event()

    def _handle_discovered_devices(self, mac_address: str) -> None:

        device = self.create_or_update_device(mac_address=mac_address)
    