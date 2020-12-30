from pyrogram import Client


app = Client('my_account')
with app:
    chats = app.get_contacts()
    for chat_id in chats:
        try:
            app.send_message(chat_id=chat_id.id, text='your text')
            print(chat_id.username, 'sended')
        except:
            pass
