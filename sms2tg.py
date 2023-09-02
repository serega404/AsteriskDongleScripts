#!/usr/bin/python3.6

import sys, requests, urllib.parse
from datetime import datetime

bot_token = "123456789:ABCdefghIJKlmnOPQrstuVWXYz"
chat_id = "123456789"

# Remove non-utf8 chars
sys.argv[2]=bytes(sys.argv[2], 'utf-8').decode('utf-8', 'ignore')

log = "[" + datetime.now().strftime("%d-%m-%Y %H:%M:%S") + "] SMS: От: " +  sys.argv[1] + " Текст: " + sys.argv[2] + "\n"

print(log)

# Save message to log

text_file = open("/var/log/sms.txt", "a+")
text_file.write(log)
text_file.close()

# Send message

message = "Пришла SMS:\n\nОт: <code>" +  urllib.parse.quote(sys.argv[1]) + "</code>\nТекст: <b>" + urllib.parse.quote(sys.argv[2]) + "</b>"
req = requests.get("https://api.telegram.org/bot" + bot_token + "/sendMessage?parse_mode=HTML&chat_id=" + chat_id + "&text=" + message)
if (req.status_code != 200):
    print("Сообщение не отправлено! Статус код: " + str(req.status_code))
else:
    print("Сообщение отправлено, mess id: " + str(req.json()['result']['message_id']))
