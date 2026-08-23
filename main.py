import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["@fanfinfunfenfon"]  # ID Grup / Username Channel tujuan
PESAN = "1 core"                 # Pesan yang ingin dikirim

def send_message():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": PESAN
    }
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        print("Pesan berhasil dikirim!")
    else:
        print(f"Gagal mengirim: {response.text}")

if __name__ == "__main__":
    send_message()
