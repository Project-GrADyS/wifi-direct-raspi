

class Device:

    def __init__(self, mac_address: str, name: str):
        self.mac_address = mac_address
        self.name = name
    
    def __str__(self):
        return f"{self.mac_address} : {self.name}"
    
    def __repr__(self):
        return f"Device({self.mac_address}, {self.name})"