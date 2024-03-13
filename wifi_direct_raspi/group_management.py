import subprocess
import time

class GroupManagement:

    def __init__(self):
        pass

    def group_status(self):
        command = ["wpa_cli", "status"]
        
        process = subprocess.Popen(
            command, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            universal_newlines=True
        )
        time.sleep(10)
        output, err = process.communicate()
        output = output.split()
        print(output)
        if output == 'Ok':
            return True
        else:
            return err

    def set_autonomous_group(self):
        command = ["wpa_cli", "p2p_group_add", "persistent"]
        
        process = subprocess.Popen(
            command, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            universal_newlines=True
        )
        time.sleep(10)
        output, err = process.communicate()
        output = output.split()
        print(output)
        if output == 'Ok':
            return True
        else:
            return err
    
    def invite_to_group(self, group_id):
        command = ["wpa_cli", "p2p_invite", group_id]
        
        process = subprocess.Popen(
            command, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            universal_newlines=True
        )
        time.sleep(10)
        output, err = process.communicate()
        output = output.split()
        print(output)
        if output == 'Ok':
            return True
        else:
            return err

    def forget_group(self, group_id):
        command = ["wpa_cli", "p2p_group_remove", group_id]
        
        process = subprocess.Popen(
            command, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            universal_newlines=True
        )
        time.sleep(10)
        output, err = process.communicate()
        output = output.split()
        print(output)
        if output == 'Ok':
            return True
        else:
            return err