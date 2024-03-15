import asyncio
from typing import (Any, MutapleMapping)
from weakref import WeakKeyDictionary

# This class will get commands from the terminal about the ongoing wi-fi direct related events

class EventManagement:
    def __init__(self):
        self._bus_lock = asyncio.Lock()

    

_global_instances: MutapleMapping[Any, EventManagement] = WeakKeyDictionary()

async def get_event_management() -> EventManagement:
    loop = asyncio.get_running_loop()
    try:
        instance = _global_instances[loop]
    except KeyError:
        instance = _global_instances[loop] = EventManagement()

    await instance.async_init()

    return instance

