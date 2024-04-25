from __future__ import annotations
import asyncio
from typing import (List, Literal, Set, Type)
from .backends.device import Device
from wifi_direct_raspi.backends.client import get_client
from wifi_direct_raspi.backends.scanner import get_scanner
from types import TracebackType

_background_tasks: Set[asyncio.Task] = set()

class WDScanner:
    """
    Interface for Wi-Fi Direct Scanner
    """

    def __init__(self, mode: Literal["virtual_push_button", "virtual_display", "keypad"] = "virtual_push_button") -> None:
        PlatformScanner = (get_scanner())
        self._backend = PlatformScanner(mode)
        self._task = None
    
    async def __aenter__(self) -> WDScanner:
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
        async with cls(mode) as scanner:
            await asyncio.sleep(timeout)
        return scanner.discovered_devices
    
    @property
    def discovered_devices(self) -> List[Device]:
        return self._backend.found_devices
    

class WDClient:
    """
    Interface for Wi-Fi Direct Client
    """

    def __init__(self, device: Device, group_mode: Literal["standard", "autonomous", "persistent"]) -> None:
        PlatformClient = (get_client())
        self._backend = PlatformClient(device, group_mode)

    async def connect(self) -> bool:
        """Connect to a device"""
        return await self._backend.connect()
    
    async def disconnect(self) -> bool:
        return await self._backend.disconnect()
    
    @property
    def mac_address(self) -> str:
        return self._backend.mac_address
    
    @property
    def name(self) -> str:
        return self._backend.name
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}, {self.mac_address}"
    
    async def __aenter__(self) -> WDClient:
        await self.connect()
        return self

    async def __aexit__(self, exc_type: Type[BaseException], exc_val: BaseException, exc_tb: TracebackType) -> None:
        await self.disconnect()
    
    @property
    def is_connected(self) -> bool:
        return self._backend.is_connected
