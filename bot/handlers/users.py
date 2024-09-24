import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

"""
users.py
---------
define users of the ledger
"""

class User:
    def __init__(self, n, i):
        self.name = n            
        self.id = i
        self.value = 0

    def setlink(self, link):
        self.link = link
         
    def getlink(self):    
        return self.link    

    def getCommand(self):
        command = []
        for k,v in self.link.items():
            command.append(k)
        return command

#path = '/home/uthceare/Documents/telegram-ledgerbot/bot/firebasekey.json'
path = './firebasekey.json'
cred = credentials.Certificate(path)
app = firebase_admin.initialize_app(cred)
db = firestore.client()
db_users = []

def updateForeign(u, name, value):
    t = getIDFromName(name)
    newData = getMoney(t)
    print('int value : '+str(int(value)))
    print('float value : '+str(float(value)))
    print('value : '+str(value))
    print('newData[u]: '+str(newData[u]))
    v = round(newData[u] - value, 2)
    print('newData[u]: '+str(v))
    newData[u] = v
    print('newData[u]: '+str(newData[u]))
    doc_ref2 = db.collection(u'users').document(str(t))
    doc_ref2.set(newData)


def pushMoney(user, value, command, refund):
    keymap = getMoney(user.id)
    if refund:
        split = 1
    else:
        split = len(command)+1

    if 'Everyone' in command:
        split = len(db_users)

    v = round(int(value) / split,2)

    print('paid : '+str(value)+'$')
    print('split between : '+str(split))
    print('spliting : '+str(v)+'$')
    if 'Everyone' not in command:
        for c in command:
            value = round(keymap[c] + v, 2)
            keymap[c] = value
            updateForeign(user.name, c, v)
    else:
        for k in keymap:
            value = round(keymap[k] + v, 2)
            keymap[k] = value
            updateForeign(user.name, k, v)

    doc_ref = db.collection(u'users').document(str(user.id))
    doc_ref.set(keymap)

    return keymap

def getMoney(identifier):
    users_ref = db.collection(u'users')
    docs = users_ref.stream()
    link = {}

    for doc in docs:
        if doc.id == str(identifier):
            for k, v in doc.to_dict().items():
                link[k] = v
    return link

def getIDFromName(name):
    users_ref = db.collection(u'name')
    docs = users_ref.stream()
    for doc in docs:
        if doc.id == str(name):
            for k, v in doc.to_dict().items():
                return v

def fetchUsers():
    print('fetch users')
    users_ref = db.collection(u'name')
    docs = users_ref.stream()
    for doc in docs:
            for k, v in doc.to_dict().items():
                    db_users.append(User(doc.id, v))

    for x in db_users:
        print(x.name+':'+x.id)


# --------------------------------------

def getUser(identifier):
    for user in getAllUsers():
        if int(user.id) == int(identifier):
            user.setlink(getMoney(user.id))
            return user
    return None

def getAllUsers():
    if len(db_users) == 0:
        fetchUsers()
    return db_users

def addNewUser(user_id, user_name):
    users_ref = db.collection('users')
    user_id = str(user_id)
    already_created = False

    for user_doc in users_ref.stream():
        if(user_doc.id == user_id):
            already_created = True

    if already_created:
        return "User already exists."
    else:
        name_collection_ref = db.collection('name')
        name_docs = name_collection_ref.stream()
        new_user_data = {}
        for name_doc in name_docs:
            name = name_doc.id
            new_user_data[name] = 0

        users_ref.document(user_id).set(new_user_data)
        name_collection_ref.document(user_name).set({'id': user_id})

        for user_doc in users_ref.stream():
            if(user_doc.id == user_id): continue
            user_ref = user_doc.reference
            user_ref.set({user_name: 0}, merge=True)

        return(f"New user {user_name} added with ID '{user_id}'.")


def dbHandlerUpdate(collection, document, data, time):
    db.collection(collection).document(time).set(data)

def dbHandlerFetchlog():
    logs_ref = db.collection(u'logger')
    return logs_ref.stream()

def dbHandlerWipe():
    docs_ref = db.collection(u'users')
    for doc in docs_ref.stream():
        obj = {}
        for k, v in doc.to_dict().items():
            obj[k] = 0
        docs_ref = db.collection(u'users').document(doc.id).set(obj)
