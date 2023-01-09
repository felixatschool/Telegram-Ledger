import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from .users import getUser
from .users import getAllUsers
from .users import User
from .transfer import transfer
from .buy import buy
from .report import report
from .logger import fetchlog
from .logger import getLogs
from .logger import restore
from .logger import Log

"""
admin.py
---------
admin commands
"""

Admin = User("Admin", 5503217122)
users = getAllUsers();

def admin(update, context):
    print('--- in admin ---')
    print(update.message.from_user.id)
    print(update.message.text)
    userid = update.message.from_user.id
    out = 'good bye'

    message = update.message.text
    c_pos = message[7:].find(' ')+7
    username = message[7:c_pos]
    print('sending command as :'+username)

    if(message[c_pos+1:c_pos+4] == 'log'):
        fetchlog()
        return

    if(message[c_pos+1:c_pos+8] == 'restore'):
        restore(update, context)
        logs = getLogs()
        print('got logs')
        for log in logs:
            update.message.from_user.id = log.user
            text = '/admin '
            name = getUser(log.user).name + ' '
            update.message.text = text + name + log.action + ' /nolog'
            print('call recurs')
            admin(update, context)
        return

    if(message[c_pos+1:c_pos+7] == 'report'):
        for u in users:
            update.message.from_user.id = u.id
            report(update, context)
        return
    

    for u in users:
        if(u.name == username):
            update.message.from_user.id = u.id

    update.message.text = '/'+message[c_pos+1:]
    if(message[c_pos+1:c_pos+4] == 'buy'):
        buy(update, context)
    if(message[c_pos+1:c_pos+9] == 'transfer'):
        transfer(update, context)

def callFromRestore(user, action):
    #admin(update, context)
    print(user+action)
