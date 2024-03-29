import subprocess
import time
from typing import Literal
import asyncio

class Discovery:

    def __init__(self, mode: Literal["virtual_push_button", "virtual_display"]):
        pass

    """
    Make device available

    mode -> virtual_push_button or keypad

    p2p_find [timeout in seconds]
    """
    def start( mode) -> None:
        commands = [
            ["wpa_cli", "set", "config_methods", mode],
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


    """
    Scans for available Wi-Fi Direct devices and returns a list with their MAC addresses.
    """
    async def discover_devices():
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
    
    async def run_periodically(interval, function):
        while True:
            await asyncio.sleep(interval)
            await function()

    
    def _get_device_info(self, mac_address):
        command = ["wpa_cli", "p2p_peer", mac_address]
        
        process = subprocess.Popen(
            command, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            universal_newlines=True
        )
        output, err = process.communicate()
        print(output)
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