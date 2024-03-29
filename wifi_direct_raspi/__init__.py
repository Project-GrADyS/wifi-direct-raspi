import asyncio
from typing import (List, Literal, Optional, Type)
from .backends.raspberry.methods.discovery import Discovery
from .backends.device import Device
from wifi_direct_raspi.backends.client import BaseClient, get_client
from wifi_direct_raspi.backends.scanner import BaseScanner, get_scanner


class WDScanner:
    """
    Interface for Wi-Fi Direct Scanner
    """

    def __init__(self, mode: Literal["virtual_push_button", "keypad"] = "virtual_push_button") -> None:
        self._backend = get_scanner()

    async def start(self, mode: str) -> None:
        """Start scanning devices"""
        await self._backend.start(mode=mode)
    
    async def stop(self) -> None:
        """Stop scanning devices"""
        await self._backend.stop()
    
    @classmethod
    async def discover(cls, timeout: float = 5.0):
        async with cls() as scanner:
            await asyncio.sleep(timeout)
        return scanner.discovered_devices()
    
    @property
    def discovered_devices(self) -> List[Device]:
        return self._backend.found_devices
    

class WDClient:
    """
    Interface for Wi-Fi Direct Client
    """

    def __init__(self) -> None:
        self._backend = get_client()

    async def connect(self, mac_address) -> bool:
        """Connect to a device"""
        return await self._backend.connect(mac_address)
    
    async def disconnect(self) -> bool:
        return await self._backend.disconnect()
    
    @property
    def is_connected(self) -> bool:
        return self._backend.is_connected
