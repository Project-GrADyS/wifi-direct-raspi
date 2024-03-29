from wifi_direct_raspi.configuration import Configuration
from wifi_direct_raspi.backends.raspberry.dataclasses.config import Config
import subprocess

def get_mac_address():
    # Run the command to get MAC address
    result = subprocess.run(["ip", "link"], capture_output=True, text=True)
    
    # Extract MAC address from the command output
    output_lines = result.stdout.split("\n")
    for line in output_lines:
        if "link/ether" in line:
            mac_address = line.split(" ")[1]
            return mac_address

#mac_address = get_mac_address()
#print("mac address", mac_address)
#config_instance = Config(my_address=mac_address, mode="some_mode")


Configuration.disable_dhcpcd()
Configuration.configure_wpa_supplicant(True)
Configuration.configure_wlan0_p2p_go_address()
Configuration.install_dnsmasq()
Configuration.configure_dnsmasq()
Configuration.enable_and_start_systemd_networkd()
Configuration.reboot()