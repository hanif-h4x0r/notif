from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = int(input("Masukkan API ID: "))
api_hash = input("Masukkan API Hash: ")

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("\nSimpan kode String Session di bawah ini ke GitHub Secrets:\n")
    print(client.session.save())

