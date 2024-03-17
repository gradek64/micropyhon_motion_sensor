
from readWriteConfig import Config

class Colors:
     OKCYAN = "\033[96m"

class Bluetooth:
    def __init__(self):
        global config_reader
        self.initiated = False
        #read and write config
        config_reader = Config("configuration.txt")
        #read and write config
       
    def runBluetooth(self):
        if self.initiated == False:
            self.initiated = True
             # Read the current content of the file
            current_content = config_reader.read()  
            # update
            new_content = current_content + "\nGregi."
            # Save the modified content back to the file
            config_reader.write(new_content)
            print(f"{Colors.OKCYAN} current_content---: {current_content}")








            
            
