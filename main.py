from wifi_direct_raspi.discovery import Discovery
from wifi_direct_raspi.conf import Conf

#class Main:
    

if __name__ == "__main__":
    #lib = Main()
    Conf.check_and_install_packages()
    discovered_devices = Discovery.discover_devices()
    print(discovered_devices)