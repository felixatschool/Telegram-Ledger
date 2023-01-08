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

Anouk = User("Anouk", 5646886949)
Daphne = User("Daphne", 5725343334)
Felix = User("Felix", 5503217122)
Kevin = User("Kevin", 5765549475)

users_list = [Anouk, Daphne, Felix, Kevin]
path = './firebasekey.json'
cred = credentials.Certificate(path)
app = firebase_admin.initialize_app(cred)
db = firestore.client()

def updateForeign(u, name, value):
    t = getIDFromName(name)
    newData = getMoney(t)
    print('int value : '+str(int(value)))
    print('float value : '+str(float(value)))
    print('value : '+str(value))
    print('newData[u]: '+str(newData[u]))
    newData[u] = newData[u] - value
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
        split = 4

    v = round(int(value) / split,2)
    print('paid : '+str(value)+'$')
    print('split between : '+str(split))
    print('spliting : '+str(v)+'$')
    if 'Everyone' not in command:
        for c in command:
            keymap[c] += v
            updateForeign(user.name, c, v)
    else:
        for k in keymap:
            keymap[k] = keymap[k] + v
            updateForeign(user.name, k, v)

    doc_ref = db.collection(u'users').document(str(user.id))
    doc_ref.set(keymap)

    return keymap

def getMoney(identifier):
    print('get mony')
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


# --------------------------------------

def getUser(identifier):
    for user in users_list:
        print(str(user.id))
        if user.id == identifier:
            user.setlink(getMoney(user.id))
            return user
    return None
