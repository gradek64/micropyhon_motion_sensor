class Colors:
    OKBLUE = "\033[94m"


class Config:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r') as file:
            content = file.read()
        return content

    def write(self, new_content):
        with open(self.filename, 'w') as file:
            file.write(new_content)
            
            
