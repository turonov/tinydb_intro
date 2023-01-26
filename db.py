import json

class DB:
    def __init__(self,path):
        self.path = path
        # Read the data from the file
        self.data = {}
        with open(self.path,'r') as f:
            self.data = json.load(f)

def getID(self,chat_id,name):
    db = self.data[chat_id][name]
    data = {
        
    }