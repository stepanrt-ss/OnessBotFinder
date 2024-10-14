from telethon import TelegramClient, events
from newLib import FindWords
import asyncio


api_id = 26189911
api_hash = '5148ff2d0ce585928a6cbcc7e6b2f9b5'
searcher = FindWords()
client = TelegramClient('../andrey.session', api_id, api_hash)


@client.on(events.NewMessage())
async def handler(event):
    message = event.message.message
    check_message = await searcher.checker(message)
    if check_message == 'success':
        print(message)

    # data_send = searcher.createMessage(data=event, msg=event.message.message)
    # if data_send == 'None':
    #     pass
    # else:
    #     message_link = data_send.split(':')[0]
    #     msg = data_send.split(':')[1]
    #     print(f"""--------------------------\n{message_link}\n{msg}\n--------------------------""")



async def main():
    await client.start()
    await asyncio.gather(client.run_until_disconnected())


if __name__ == '__main__':
    asyncio.run(main())
# UpdateShortChatMessage частный
# UpdateNewChannelMessage публичный