from wifi_direct_raspi.raspberry.methods.discovery import Discovery
from wifi_direct_raspi.raspberry.methods.connection import Connection
from wifi_direct_raspi.configuration import Configuration
from wifi_direct_raspi.raspberry.methods.group_management import GroupManagement
import subprocess
import threading
import time
#class Main:
    

if __name__ == "__main__":
    #lib = Main()
    #Conf.disable_dhcpcd()
    #Conf.configure_wpa_supplicant(True)
    #Conf.configure_wlan0_p2p_go_address()
    #Conf.install_dnsmasq()
    #Conf.configure_dnsmasq()
    #Conf.enable_and_start_systemd_networkd()
    #Conf.reboot()

    #Discovery.start("virtual_push_button")
    #discovered_devices = Discovery.discover_devices()
    #print(discovered_devices)
    #resp = Connection.connect_to_device(discovered_devices[0])
    
    #print(resp)

    r = GroupManagement.group_status()

    print(r)

    '''
    while True:
        command = ["wpa_cli", "-i", "wlan0", "SUBSCRIBE"]
        
        process = subprocess.Popen(
            command, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            universal_newlines=True
        )
        #time.sleep(10)
        output, err = process.communicate()
        output = output.split()
        print(output)
    '''