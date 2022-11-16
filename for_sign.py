from telethon import TelegramClient
from pathlib import Path


api_id = 22998293
api_hash = 'bce9f7a7a22733fd12ebef3840b60e48'
phone_number = "" #ФОРМА
test_signed_or_no = False

client = TelegramClient('sessionfile', api_id, api_hash)
if not Path("/sessionfile.session"):
    test_signed_or_no = False
else:
    test_signed_or_no = True


def getcode():
    code = input("Вводи: ") #ФОРМА get the code from somewhere ( bot, file etc.. )
    return code

client.start(phone=phone_number, password="151515", code_callback=getcode)