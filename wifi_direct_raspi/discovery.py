import subprocess
import re

class Discovery:
    """
    """
    def __init__(self):
        print("oi")
    
    def discover_devices():
        """
        Scans for available Wi-Fi Direct devices and returns a list with their MAC addresses.
        """
        '''process = subprocess.Popen(
            ["wpa_cli", "set", "config_methods", "virtual_push_button"], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            universal_newlines=True
        )
        output, err = process.communicate()
        print("output= ", output)
        print("-------------------------------")
        print("error= ", err)'''

        devices = []
        process = subprocess.Popen(
            ["wpa_cli", "p2p_peers"], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            universal_newlines=True
        )
        output, err = process.communicate()
        output_list = output.split()
        devices = output_list[3:]
        return devices