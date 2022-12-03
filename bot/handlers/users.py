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


Anouk = user("Anouk", 5503217123)
Daphne = user("Daphne", 5725343334)
Felix = user("Felix", 5503217122)
Kevin = user("Kevin", 5765549475)


users_list = [Anouk, Daphne, Felix, Kevin]
path = './firebasekey.json'
cred = credentials.Certificate(path)
app = firebase_admin.initialize_app(cred)
db = firestore.client()

def pushMoney(identifier):
    doc_ref = db.collection(u'users').document(str(identifier))
    doc_ref.set({
        u'Anouk': 23,
        u'Daphne': 39,
        u'Kevin': 1815
        })

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
