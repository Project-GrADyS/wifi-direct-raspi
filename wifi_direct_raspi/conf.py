import subprocess

class Conf:
    """
    Configuration files
    """
    def __init__(self):
        print("oi")
    
    '''
    
    def check_and_install_packages():
        """
        Checks if required packages are installed and installs them if needed.
        """
        required_packages = ["wpasupplicant", "wireless-tools", "iw"]
        for package in required_packages:
            try:
                subprocess.run(["dpkg", "--status", package], check=True, capture_output=True)
            except subprocess.CalledProcessError:
                subprocess.run(["sudo", "apt-get", "install", "-y", package])
                print(f"Package '{package}' installed successfully.")
    '''
    '''
    Installs nmap package: nmap is needed to seach the connected device
    '''
    def check_and_install_packages():
        """
        Checks if required packages are installed and installs them if needed.
        """
        required_packages = ["nmap"]
        for package in required_packages:
            try:
                subprocess.run(["dpkg", "--status", package], check=True, capture_output=True)
            except subprocess.CalledProcessError:
                subprocess.run(["sudo", "apt-get", "install", "-y", package])
                print(f"Package '{package}' installed successfully.")
    
    def disable_dhcpcd():
        with open("/etc/dhcpcd.conf", "a") as f:
            f.write("denyinterfaces p2p-wlan0-*\n")
    
    def configure_wpa_supplicant():
        with open("/etc/wpa_supplicant/wpa_supplicant.conf", "a") as f:
            f.write("device_name=DIRECT-RasPi1\n")
            f.write("p2p_go_ht40=1\n")
    
    def configure_wlan0_p2p_go_address():
        subprocess.run(["sudo -Es"], check=True)
        subprocess.run(["cat > /etc/systemd/network/12-p2p-wlan0.network <<\EOF"], check=True)
        subprocess.run(["sudo -Es"], check=True)
        subprocess.run(["sudo -Es"], check=True)
        subprocess.run(["sudo -Es"], check=True)
        subprocess.run(["sudo -Es"], check=True)
        subprocess.run(["sudo -Es"], check=True)