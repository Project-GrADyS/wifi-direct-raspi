import subprocess

class Conf:
    """
    Configuration files
    """
    def __init__(self):
        print("oi")
    
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