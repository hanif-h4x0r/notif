import os
import asyncio
from telethon import TelegramClient

# Mengambil data sensitif dari GitHub Secrets
API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
SESSION_STRING = os.environ["SESSION_STRING"]
TARGET = "@anything_notslava_bot"  # Ubah sesuai username tujuan
PESAN = "1 core"       # Ubah pesan yang ingin dikirim

async def main():
    # Menggunakan StringSession agar tidak perlu login ulang tiap jalan
    from telethon.sessions import StringSession
    async with TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH) as client:
        await client.send_message(TARGET, PESAN)
        print(f"Berhasil mengirim pesan ke {TARGET}")

if __name__ == "__main__":
    asyncio.run(main())
