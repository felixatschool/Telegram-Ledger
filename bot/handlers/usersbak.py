import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

"""
users.py
---------
define users of the ledger
"""

class user:
    def __init__(self, n, i):
        self.name = n
        self.id = i
        self.value = 0
        self.output = ' : '+f'{self.value}'+'$\n'

    def setlink(self, link):
        self.link = link

    def getlink(self, link):
        return self.link

    def getCommand(self):
        command = []
        for k,v in self.link.items():
            command.append(k)
        return command

Anouk = user("Anouk", 5503217123)
Daphne = user("Daphne", 5725343334)
Felix = user("Felix", 5503217122)
Kevin = user("Kevin", 5765549475)

users_list = [Anouk, Daphne, Felix, Kevin]
path = './firebasekey.json'
cred = credentials.Certificate(path)
app = firebase_admin.initialize_app(cred)
db = firestore.client()

def updateForeign(u, name, value):
    users_ref = db.collection(u'name')
    docs = users_ref.stream()
    for doc in docs:
        if doc.id == str(name):
            for k, v in doc.to_dict().items():
                identifier = v

    map = getMoney(identifier)
    map[u] += -int(value)
    doc_ref = db.collection(u'users').document(str(user.id))
    doc_ref.set(map)


def pushMoney(user, value, command):
    map = getMoney(user.id)
    split = len(command)
    print('nb of split'+str(split))
    for c in command:
        map[c] += int(value)
        #updateForeign(user.id, c, value)

    doc_ref = db.collection(u'users').document(str(user.id))
    doc_ref.set(map)

    return map

def getMoney(identifier):
    users_ref = db.collection(u'users')
    docs = users_ref.stream()
    link = {}

    for doc in docs:
        if doc.id == str(identifier):
            for k, v in doc.to_dict().items():
                link[k] = v
    return link

# --------------------------------------
def getUser(identifier):
    for user in users_list:
        if user.id == identifier:
            user.setlink(getMoney(user.id))
        return user
    return None
