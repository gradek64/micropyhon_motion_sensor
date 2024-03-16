class Colors:
    OKBLUE = "\033[94m"

class Bluetooth:
    def __init__(self):
        self.initiated = False
        print(f"{Colors.OKBLUE} BLUETOOTH SETTING STARTED")
    def runBluetooth(self):
        if self.initiated == False:
            self.initiated = True
            # Open the file in read-write mode
            with open('configuration.txt', 'r+') as file:
                # Read the contents of the file
                content = file.read()

                # Modify the content (for example, add some text)
                content += "\nThis line is added to the file."

                # Move the file pointer to the beginning
                file.seek(0)

                # Write the modified content back to the file
                file.write(content)
                print(f"{Colors.OKBLUE} CONFIGURATION SET")
            
