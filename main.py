from wifi_direct_raspi.discovery import Discovery
from wifi_direct_raspi.conf import Conf

#class Main:
    

if __name__ == "__main__":
    #lib = Main()
    Conf.disable_dhcpcd()
    Conf.configure_wpa_supplicant()
    Conf.configure_wlan0_p2p_go_address()
    Conf.install_dnsmasq()
    Conf.configure_dnsmasq()
    Conf.enable_and_start_systemd_networkd()]
    Conf.reboot()
    discovered_devices = Discovery.discover_devices()
    print(discovered_devices)