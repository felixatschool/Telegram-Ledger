import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from .users import getUser
from .users import User
from .buy import buy
from .transfer import transfer

"""
admin.py
---------
admin commands
"""

Anouk = User("Anouk", 5646886949)
Daphne = User("Daphne", 5725343334)
Felix = User("Felix", 5503217122)
Kevin = User("Kevin", 5765549475)

users = {Anouk, Daphne, Felix, Kevin}


def admin(update, context):
    userid = update.message.from_user.id
    out = 'good bye'

    if(userid != Felix.id):
        out = 'no.'
        return

    message = update.message.text
    c_pos = message[7:].find(' ')+7
    username = message[7:c_pos]

    for u in users:
        if(u.name == username):
            update.message.from_user.id = u.id

    if(userid == update.message.from_user.id):
        out = 'no user found'
        update.message.reply_text(out, parse_mode='HTML')
        return

    update.message.text = '/'+message[c_pos+1:]
    if(message[c_pos+1:c_pos+4] == 'buy'):
        buy(update, context)
    if(message[c_pos+1:c_pos+9] == 'transfer'):
        transfer(update, context)
    
    #user = getUser(update.message.from_user.id)
    #update.message.reply_text(out, parse_mode='HTML')
