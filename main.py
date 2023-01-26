from tinydb import TinyDB
from tinydb.table import Document
import os
TOKEN = os.environ['TOKEN']
db = TinyDB('db.json',indent=4)
print(db.default_table_name)


user = Document({
    'firstname':'Shaxzod',
    'job':'Developer'
    },doc_id=9)

for doc in Document:
    if doc_id==True:
        db+1
    if doc_id == False:
        db.contains(doc_id)

def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    bot.sendMessage(
    chat_id=chat_id,

db.insert(user)