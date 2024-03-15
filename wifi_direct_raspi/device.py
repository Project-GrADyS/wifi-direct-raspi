

class Device:

    def __init__(self, mac_address: str):
        self.mac_address = mac_address
    
    def __str__(self):
        return f"{self.mac_address}"