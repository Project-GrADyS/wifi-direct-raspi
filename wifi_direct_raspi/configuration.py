import subprocess

"""
Configuration file
"""
class Configuration:
    """
    Disable processing P2P GO interfaces, by adding this line to the top
    of the file
    """
    def disable_dhcpcd():
        with open("/etc/dhcpcd.conf", "w") as f:
            f.write("denyinterfaces p2p-wlan0-*\n")

    """
    Configures the wpa_supplicant configuration file, adding P2P settings.
    If the parameter group_owner=false, the raspberry pi will be a client,
    is group_owner=true or the parameter is not passed, the raspberry pi 
    will be the group owner.
    """
    def configure_wpa_supplicant(group_owner):
        with open("/etc/wpa_supplicant/wpa_supplicant.conf", "w") as f:
            f.write("device_name=DIRECT-RasPi1\n")
            f.write("device_type=1-0050F204-1\n")
            f.write("driver_param=p2p_device=1\n")
            '''
            if not group_owner:
                f.write("p2p_go_intent=0\n")
            else:
                f.write("p2p_go_intent=15\n")
            f.write("p2p_go_ht40=1\n")
            '''
    
    """
    Configures wlan0 P2P GO (group owner) address and systemd-networkd DHCP server
    """
    def configure_wlan0_p2p_go_address(mac_address):
        with open("/etc/systemd/network/12-p2p-wlan0.network", "w") as f:
            f.write("[Match]\n")
            f.write("Name=p2p-wlan0-*\n")
            f.write("[Network]\n")
            f.write("#LLMNR=no\n")
            f.write("#MulticastDNS=yes\n")
            f.write("#IPMasquerade=yes\n")
            f.write("Address=192.168.4.1/24\n")
            f.write("# Comment out the following lines to disable the internal DHCP Server function and use, e.g., dnsmasq\n")
            f.write("DHCPServer=yes\n")
            f.write("[DHCPServer]\n")
            f.write("#DNS=84.200.69.80 1.1.1.1\n")
            f.write("EOF\n")


    """
    Installs external DHCP server dnsmasq
    """
    def install_dnsmasq():
        subprocess.run(["sudo", "apt", "install", "dnsmasq"])
    
    """
    Configures dnsmasq
    """
    def configure_dnsmasq():
        with open("/etc/dnsmasq.conf", "w") as f:
            f.write("interface=p2p-wlan*\n")
            f.write("no-dhcp-interface=lo,wlan0\n")
            f.write("domain-needed\n")
            f.write("bogus-priv\n")
            f.write("dhcp-range=192.168.4.50,192.168.4.199,12h\n")
            f.write("dhcp-option=3,192.168.50.1\n")

    def enable_and_start_systemd_networkd():
        subprocess.run(["systemctl", "enable", "systemd-networkd.service"], check=True)
        subprocess.run(["systemctl", "start", "systemd-networkd.service"], check=True)
    
    """
    Reboots Raspberry Pi
    """
    def reboot():
        subprocess.run(["sudo", "reboot"], check=True)