import qrcode
import telethon
from telethon import TelegramClient

TELEGRAM_API_ID = 26189911
TELEGRAM_API_HASH = '5148ff2d0ce585928a6cbcc7e6b2f9b5'

def gen_qr(token:str):
    img = qrcode.make(token)
    type(img)
    img.save("QR_Code.png")

def display_url_as_qr(url):
    print(url)
    gen_qr(url)

async def main(client: telethon.TelegramClient):
    if(not client.is_connected()):
        await client.connect()
    client.connect()
    qr_login = await client.qr_login()
    print(client.is_connected())
    display_url_as_qr(qr_login.url)
    await qr_login.wait(10)


client = TelegramClient("andrey", TELEGRAM_API_ID, TELEGRAM_API_HASH)
client.loop.run_until_complete(main(client))