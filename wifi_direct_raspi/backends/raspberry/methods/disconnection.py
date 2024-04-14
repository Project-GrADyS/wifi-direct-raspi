import subprocess

class Disconnection:
    
    def __init__(self):
        pass

    """
    Disconnects the device from the P2P Group using the group's address.
    """

    def disconnect(self, group_addresss):
        command = ["wpa_cli", "p2p_group_remove", group_addresss]
        
        process = subprocess.Popen(
            command, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            universal_newlines=True
        )
        
        output, err = process.communicate()
        
        if output == 'Ok':
            return True
        else:
            return err
        
    def disconnect_from_group(group_addresss):
        command = ["wpa_cli", "p2p_group_remove", group_addresss]
        
        process = subprocess.Popen(
            command, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            universal_newlines=True
        )
        
        output, err = process.communicate()
        
        if output == 'Ok':
            return True
        else:
            return err
