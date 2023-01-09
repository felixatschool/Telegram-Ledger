from .users import getUser
from .users import pushMoney

from .users import getUser
from .users import pushMoney
from .users import getMoney
from .report import report
from .logger import log

command = []

def getInputCommand(message, userCommand):
        command = []
        index = 4;
        c_pos = 0;
        if message.count('-') > 1:
            return []
        while message[index:].find('-') != -1:
            print('in while')
            c_pos = message[index:].find('-') + 1 + index
            if c_pos == -1 or c_pos == len(message):
                print('no cpos')
                return []
            print('index + c_pos : '+str(index+c_pos))
            e_pos = message[index + c_pos:].find(' ') + 2 + index + c_pos
            print('e_pos : '+str(e_pos))

            d_pos = message[index + c_pos:].find(' ') 
            print('d_pos : '+str(d_pos))
            if d_pos == -1:
                d_pos = len(message)
            else:
                d_pos = index + c_pos + d_pos

            char = message[c_pos:d_pos]

            '''
            print('c_pos : '+str(c_pos))
            print('e_pos : '+str(e_pos))
            print('char : '+str(char))
            print('len : '+str(len(char)))
            print('totallen : '+str(len(message)))
            '''

            if char not in userCommand:
                print('no target')
                print(char)
                print(userCommand)
                return []
            command.append(char)
            if 'Everyone' in command and len(command)>1:
                return []
            index = c_pos
            print('end of loop')
        return command


def transfer(update, context):
    global command
    """
    /transfer:
    Declare a refund to someone
    """

    userid = update.message.from_user.id
    print('userid: '+str(userid))
    user = getUser(update.message.from_user.id)

    if user is None:
            update.message.reply_text('<b> User not found </b>', parse_mode='HTML')
            return
    try:
        if len(update.message.text) == 9:
            raise Exception('Please specify an amount and target.\nTo get more help type \'/buy -help\'')
        if update.message.text == '/buy -help':
            raise Exception('<b><u>Help</u></b> \n Command : buy \n \n Enter the total amount you paid and who to split the cost with. \n \n <b> Usage : </b> \n /buy Number -Target \n Replace Numebr with total paid. \n Replace Target with : Anouk, Daphne, Kevin, Felix, Everyone\n\n Exemple to split a 20$ purchase with Anouk and Daphne type : \n /buy 20 -Anouk -Daphne')

        f_pos = update.message.text.find(' ') + 1
        e_pos = update.message.text[f_pos:].find(' ')

        if f_pos != 10:
            raise Exception('Plase specify an amount.\nTo get more help type \'/buy -help\'')

        if e_pos == -1:
            raise Exception('Plase specify an amount and a target.\nTo get more help type \'/buy -help\'')

        value = update.message.text[f_pos:f_pos + e_pos]
        if not value.isdigit():
            raise Exception('Plase specify an amount.\nTo get more help type \'/buy -help\'')

        command = getInputCommand(update.message.text, user.getCommand())
        if len(command) == 0:
            raise Exception('Not a valid target.\nTo get more help type \'/buy -help\'')

        oldLink = getMoney(userid)
        link = pushMoney(user, value, command, True)
        out = ''
        if update.message.text[-6:] == "/nolog":
            out += user.name + ': '+update.message.text[1:-7] + '\n'
        out += '<b>Dear '+user.name+', citizen of Clémence</b> \n<u>Here\'s your account updated report:</u>\n\n'
        for k, v in link.items():
            if(v == oldLink[k]):
                continue
            out += k + ' : ' + str(oldLink[k]) + '$ --> ' + str(v)+'$\n'
        print('done')

    except Exception as e:
        out = str(e)
    log(userid, update.message.text)
    update.message.reply_text(out, parse_mode='HTML')
