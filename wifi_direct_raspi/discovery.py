import subprocess
import time

class Discovery:
    """
    Scans for available Wi-Fi Direct devices and returns a list with their MAC addresses.
    """
    def discover_devices():
        devices = []

        #["wpa_cli", "p2p_stop"],
        #["wpa_cli", "set", "config_methods", "virtual_push_button"],

        commands = [
            ["wpa_cli", "p2p_stop"],
            ["wpa_cli", "p2p_find", "5"],
            ["wpa_cli", "p2p_peers"],
        ]

        for command in commands:
            process = subprocess.Popen(
                command, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE, 
                universal_newlines=True
            )
            output, err = process.communicate()
            output_list = output.split()
            if output != 'Ok' and err == '':
                devices = output_list[3:]
            else:
                print("error= ", err)
        return devices