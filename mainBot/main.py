# from newLib import FindWords
# import asyncio
# import tgcrypto
#
#
# api_id = 26189911
# api_hash = '5148ff2d0ce585928a6cbcc7e6b2f9b5'
# searcher = FindWords()
# client = TelegramClient('work.session', api_id, api_hash)
from mailbox import Message

from pyrogram import Client, filters
from newLib import FindWords
import asyncio

api_id = 26189911
api_hash = '5148ff2d0ce585928a6cbcc7e6b2f9b5'
searcher = FindWords()

# Создаем клиент Pyrogram
# app = Client("andrey_session", api_id=api_id, api_hash=api_hash)
app = Client("work", api_id=api_id, api_hash=api_hash)


a = 0

@app.on_message(filters.text)
async def checkMsg(client, message):
    print(message.chat.type)
    # message_check = await searcher.checker(message.text)
    # if message_check == 'success':
    #     if str(message.chat.type) == 'ChatType.GROUP':
    #         searcher.sendMessageManger(message, 'SuperGroup')
    #     elif str(message.chat.type) == 'ChatType.SUPERGROUP':
    #         searcher.sendMessageManger(message, 'SuperGroup')


        # print(message)
        # print(message.text)

        # check_msg = await searcher.checker(message.text)
        # if check_msg == 'success':

#ChatType.PRIVATE
#ChatType.SUPERGROUP
#ChatType.GROUP

# @client.on_message()
# async def handler(client, message):
#     print('Получено новое сообщение')
#     print(message.text)
    # message_text = message.text
    # check_message = await searcher.checker(message_text)
    # if check_message == 'success':
    #     print(message_text)

    # data_send = searcher.createMessage(data=message, msg=message_text)
    # if data_send == 'None':
    #     pass
    # else:
    #     message_link = data_send.split(':')[0]
    #     msg = data_send.split(':')[1]
    #     print(f"""--------------------------\n{message_link}\n{msg}\n--------------------------""")

app.run()