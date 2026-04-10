import hashlib
from Base.file import FileHandler

class User(FileHandler):

    def __init__(self,name):
        super().__init__("Data/"+ name +".json")
        
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()