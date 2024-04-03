from __future__ import annotations
import asyncio
from typing import (List, Literal, Optional, Set, Type)
from .backends.raspberry.methods.discovery import Discovery
from .backends.device import Device
from wifi_direct_raspi.backends.client import BaseClient, get_client
from wifi_direct_raspi.backends.scanner import BaseScanner, get_scanner
from types import TracebackType

_background_tasks: Set[asyncio.Task] = set()

class WDScanner:
    """
    Interface for Wi-Fi Direct Scanner
    """

    def __init__(self, mode: Literal["virtual_push_button", "virtual_display", "keypad"] = "virtual_push_button") -> None:
        PlatformScanner = (get_scanner())
        self._backend = PlatformScanner(mode=mode)
        self._task = None
    
    async def __aenter__(self):
        await self._backend.start()
        return self
    
    async def __aexit__(self, exc_type: Type[BaseException], exc_val: BaseException, exc_tb: TracebackType) -> None:
        await self._backend.stop()

    async def start(self, mode: str) -> None:
        """Start scanning devices"""
        await self._backend.start()
    
    async def stop(self) -> None:
        """Stop scanning devices"""
        await self._backend.stop()

    @classmethod
    async def discover(cls, timeout= 5, mode="virtual_push_button"):
        print("entrei")
        async with cls(mode) as scanner:
            await asyncio.sleep(timeout)
        return scanner.discovered_devices
    
    async def _dis(self):
        while True:
            await asyncio.sleep(5)
            return self._backend.found_devices
    
    @property
    def discovered_devices(self) -> List[Device]:
        print("oi2")
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
