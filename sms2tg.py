#!/usr/bin/python3.6

import sys, requests

bot_token = "123456789:ABCdefghIJKlmnOPQrstuVWXYz"
chat_id = "123456789"

message = "Пришла новая SMS:\nОтправитель: " +  sys.argv[1] + "\nТекст: " + sys.argv[2]

print(message)

# Save message to log

text_file = open("/var/log/sms", "a+")
text_file.write(message)
text_file.close()

# Send message

req = requests.get("https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + chat_id + "&text=" + message)
if (req.status_code != 200):
    print("Сообщение не отправлено! Статус код: " + str(req.status_code))
else:
    print("Сообщение отправлено, mess id: " + str(req.json()['result']['message_id']))
