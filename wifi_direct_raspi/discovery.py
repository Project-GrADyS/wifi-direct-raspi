import subprocess

class Discovery:
    """
    """
    def __init__(self):
        print("oi")
    
    def discover_devices():
        """
        Scans for available Wi-Fi Direct devices and returns a list of their MAC addresses.
        """
        result = subprocess.run(["iw", "dev", "wlan0", "scan", "| grep", "p2p"], capture_output=True, text=True)
        devices = []
        for line in result.stdout.splitlines():
            if "p2p_dev_addr" in line:
                mac_address = line.split()[2]
                devices.append(mac_address)
        return devices