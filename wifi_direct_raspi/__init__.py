import asyncio
from typing import (List, Literal)
from .backends.raspberry.methods.discovery import Discovery
from .device import Device
from .backends.raspberry.client import WDRaspiClient


class WDScanner:
    """
    Interface for Wi-Fi Direct Scanner
    """

    def __init__(self, mode: Literal["virtual_push_button", "keypad"] = "virtual_push_button") -> None:
        self._backend = WDRaspiClient

    async def start(self, mode: str) -> None:
        """Start scanning devices"""
        await Discovery.start()
    
    async def stop(self) -> None:
        await Discovery.stop()
    
    @classmethod
    async def discover(cls, timeout=5):
        async with cls() as scanner:
            await asyncio.sleep(timeout)
        return scanner.discovered_devices()
    
    @property
    def discovered_devices(self) -> List[Device]:
        return self._backend.found_devices

