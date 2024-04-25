import subprocess
import time

class Connection:
    def __init__(self):
        pass

    """
    Connects to a Wi-Fi Direct device using its MAC address.
    """
    async def connect_to_device(self, mac_address):
        command = ["wpa_cli", "p2p_connect", mac_address, "pbc"]
        
        process = subprocess.Popen(
            command, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            universal_newlines=True
        )
        time.sleep(10)
        output, err = process.communicate()
        output = output.split()
        
        if output == 'Ok':
            return True
        else:
            return False, err
        

        