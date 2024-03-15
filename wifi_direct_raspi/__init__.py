"""Top-level package"""

import asyncio
from typing import (List, Literal)
from .discovery import Discovery
from .device import Device


class WDScanner:
    """
    Interface for Wi-Fi Direct Scanner
    """

    def __init__(self, mode: Literal["virtual_push_button", "keypad"] = "virtual_push_button") -> None:
        pass

    async def start(self, mode: str) -> None:
        """Start scanning devices"""
        await Discovery.start()
    
    async def stop(self) -> None:
        await Discovery.stop()
    
    @classmethod
    async def discover(timeout=5):
        await Discovery.discover_devices()
    
    @property
    def discovered_devices(self) -> List[Device]:

