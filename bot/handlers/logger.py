import time
from .users import dbHandlerUpdate
from .users import dbHandlerFetchlog
from .users import dbHandlerWipe

class Log:
    def __init__(self, u, a):
        self.user = u
        self.action = a
        

def log(user, message):
    if message[-6:] == "/nolog":
        return
    print('------------------')
    print('LOGGER')
    print('user :'+str(user))
    print('message :' + message)
    print('------------------')
    t = str(time.time())
    out = str(user) +'/'+ message
    data = {
            str(user) : message
            }
    dbHandlerUpdate('logger', '01', data, str(time.time()))

def fetchlog():
    out = ''
    logs = []
    docs = dbHandlerFetchlog()
    for doc in docs:
        for user, action in doc.to_dict().items():
            logs.append(Log(user,action[1:]))
    return logs

def restore(update, context):
    dbHandlerWipe()

def getLogs():
    return fetchlog()
