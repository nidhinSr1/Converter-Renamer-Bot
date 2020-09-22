@run_async

def slist(bot: Bot, update: Update):

    message = update.effective_message

    text1 = "My sudo users are:"

    text2 = "My support users are:"

    for user_id in SUDO_USERS:

        try:

            user = bot.get_chat(user_id)

            name = "[{}](tg://user?id={})".format(user.first_name + (user.last_name or ""), user.id)

            if user.username:

                name = escape_markdown("@" + user.username)

            text1 += "\n - `{}`".format(name)

        except BadRequest as excp:

            if excp.message == 'Chat not found':

                text1 += "\n - ({}) - not found".format(user_id)

    for user_id in SUPPORT_USERS:

        try:

            user = bot.get_chat(user_id)

            name = "[{}](tg://user?id={})".format(user.first_name + (user.last_name or ""), user.id)

            if user.username:

                name = escape_markdown("@" + user.username)

            text2 += "\n - `{}`".format(name)

        except BadRequest as excp:

            if excp.message == 'Chat not found':

                text2 += "\n - ({}) - not found".format(user_id)

    message.reply_text(text1 + "\n" + text2 + "\n", parse_mode=ParseMode.MARKDOWN)

    #message.reply_text(text2 + "\n", parse_mode=ParseMode.MARKDOWN)

def __user_info__(user_id, chat_id):

    if user_id == dispatcher.bot.id:

        return tld(chat_id, "I've seen them in... Wow. Are they stalking me? They're in all the same places I am... oh. It's me.")

    num_chats = sql.get_user_num_chats(user_id)

    return tld(chat_id, "I've seen them in <code>{}</code> chats in total.").format(num_chats)

def __stats__():

    return "{} users, across {} chats".format(sql.num_users(), sql.num_chats())

def __gdpr__(user_id):

    sql.del_user(user_id)

def __migrate__(old_chat_id, new_chat_id):

    sql.migrate_chat(old_chat_id, new_chat_id)

__help__ = ""  # no help string

__mod_name__ = "Users"
