import json
import os

class FileHandler:

    def __init__(self, filename):
        self.filename = filename

    def ensure_file(self):
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump({}, f)

    def read(self):
        self.ensure_file()
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}

    def write(self, data):
        self.ensure_file()
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)