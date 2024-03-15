import subprocess
import time
from typing import Literal

class Discovery:

    def __init__(self, mode: Literal["virtual_push_button", "keypad"]):
        pass

    """
    Make device available

    mode -> virtual_push_button or keypad

    p2p_find [timeout in seconds]
    """
    def start(self, mode) -> None:
        self.found_devices = []
        commands = [
            ["wpa_cli", "set", "config_methods", mode],
            ["wpa_cli", "p2p_find", "5"]
        ]

        for command in commands:
            process = subprocess.Popen(
                command, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE, 
                universal_newlines=True
            )
            output, err = process.communicate()


    """
    Scans for available Wi-Fi Direct devices and returns a list with their MAC addresses.
    """
    def discover_devices():
        devices = []

        #["wpa_cli", "p2p_stop"],
        #["wpa_cli", "set", "config_methods", "virtual_push_button"],

        commands = [
            ["wpa_cli", "p2p_peers"],
        ]

        #for command in commands:
        process = subprocess.Popen(
            commands[0], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            universal_newlines=True
        )
        output, err = process.communicate()
        output_list = output.split()
        devices = output_list[3:]

        return devices
    
    """
    Make device unavailable
    """
    def stop(self):
        commands = [
            ["wpa_cli", "p2p_stop"],
        ]

        for command in commands:
            process = subprocess.Popen(
                command, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE, 
                universal_newlines=True
            )
            output, err = process.communicate()