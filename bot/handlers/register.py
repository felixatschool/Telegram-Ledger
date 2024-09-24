from .users import addNewUser

def register(update, context):
    """
    /register
    just say hello and register
    """
    msg = addNewUser(update.message.from_user.id, update.message.from_user.first_name)
    update.message.reply_text(msg)
