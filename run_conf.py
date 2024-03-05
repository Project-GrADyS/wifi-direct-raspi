from wifi_direct_raspi.conf import Conf


Conf.disable_dhcpcd()
Conf.configure_wpa_supplicant(True)
Conf.configure_wlan0_p2p_go_address()
Conf.install_dnsmasq()
Conf.configure_dnsmasq()
Conf.enable_and_start_systemd_networkd()
Conf.reboot()