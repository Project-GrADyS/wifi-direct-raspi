from dataclasses import dataclass

@dataclass
class Peer:
    mac_address: str
    name: str
    manufacturer: str