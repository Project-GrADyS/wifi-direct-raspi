import subprocess
import time

class Connection:
    def __init__(self, mac_address):
        self.mac_address = mac_address

    """
    Connects to a Wi-Fi Direct device using its MAC address.
    """
    def connect_to_device(mac_addresss):
        command = ["wpa_cli", "p2p_connect", mac_addresss, "pbc"]
        
        process = subprocess.Popen(
            command, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            universal_newlines=True
        )
        time.sleep(10)
        output, err = process.communicate()
        output = output.split()
        print(output)
        if output == 'Ok':
            return True
        else:
            return err
        

        