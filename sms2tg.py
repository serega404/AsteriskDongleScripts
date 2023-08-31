#!/usr/bin/python3.6

import sys, requests

bot_token = "123456789:ABCdefghIJKlmnOPQrstuVWXYz"
chat_id = "123456789"

log = "SMS: От: " +  sys.argv[1] + " Текст: " + sys.argv[2]

print(log)

# Save message to log

text_file = open("/var/log/sms", "a+")
text_file.write(log)
text_file.close()

# Send message

message = "Пришла SMS:\n\nОт: <b>" +  sys.argv[1] + "</b>\nТекст: <code>" + sys.argv[2] + "</code>"
req = requests.get("https://api.telegram.org/bot" + bot_token + "/sendMessage?parse_mode=HTML&chat_id=" + chat_id + "&text=" + message)
if (req.status_code != 200):
    print("Сообщение не отправлено! Статус код: " + str(req.status_code))
else:
    print("Сообщение отправлено, mess id: " + str(req.json()['result']['message_id']))
