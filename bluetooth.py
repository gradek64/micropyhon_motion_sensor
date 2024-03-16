class Colors:
    OKBLUE = "\033[94m"

class Bluetooth:
    def __init__(self):
        self.initiated = False
        print(f"{Colors.OKBLUE} BLUETOOTH SETTING STARTED")
    def runBluetooth(self):
        if self.initiated == False:
            self.initiated = True
            print(f"{Colors.OKBLUE} CONFIGURATION SET")
            
