import subprocess
import time
from typing import Literal
import asyncio

class Discovery:

    def __init__(self, mode: Literal["virtual_push_button", "virtual_display", "keypad"]):
        self.mode = mode

    def start(self) -> None:
        """
        Makes device available

        Sets the connection mode
        """
        commands = [
            ["wpa_cli", "set", "config_methods", self.mode],
            ["wpa_cli", "p2p_find"]
        ]

        for command in commands:
            process = subprocess.Popen(
                command, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE, 
                universal_newlines=True
            )
            output, err = process.communicate()

        if output == 'OK':
            return True
        else:
            return False, err

    async def discover_devices(self):
        """
        Scans for available Wi-Fi Direct devices and returns a list with their MAC addresses.
        """
        devices = []
        command = ["wpa_cli", "p2p_peers"]
        
        process = subprocess.Popen(
            command, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            universal_newlines=True
        )
        output, err = process.communicate()

        if output != '':
            output_list = output.split()
            devices = output_list[3:]
        return devices
    
    @staticmethod
    async def run_periodically(interval, function):
        while True:
            await asyncio.sleep(interval)
            await function()

    async def get_device_info(self, mac_address):
        command = ["wpa_cli", "p2p_peer", mac_address]
        
        process = subprocess.Popen(
            command, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            universal_newlines=True
        )
        output, err = process.communicate()
        output_list = output.splitlines()
        output_dict = {}
        for line in output_list:
            parts = line.strip().split("=")
            if len(parts) == 2:
                key, value = parts
                output_dict[key] = value
        return output_dict
        '''
        if output != '':
            output_list = output.split()
            devices = output_list[3:]
        return devices
        '''
    
    def discover_specific_device(mac_address):
        pass
    
    """
    Make device unavailable
    """
    async def stop(self):
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