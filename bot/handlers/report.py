from .users import getUser
from .users import pushMoney

def report(update, context):
    """
    /report:
    return the ledger of all accounts
    """

    userid = update.message.from_user.id
    user = getUser(update.message.from_user.id)
    if user is None:
            update.message.reply_text('<b> User not found </b>', parse_mode='HTML')
            return
            
    text = '<b>Dear '+user.name+', citizen of Clémence</b> \n<u>Here\'s your account report:</u>\n\n'
    for k, v in user.getlink().items():
        text += k + ' : ' + str(v)+'$\n'
    update.message.reply_text(text, parse_mode='HTML')
