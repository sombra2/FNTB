import reddit
import os
import urllib.parse
import requests
import time
import credentials

cwd = os.path.dirname(os.path.realpath(__file__))

[x.encode('utf-8') for x in reddit.posts] # the data scraped from reddit is encoded in utf-8

def telegram_bot_sendtext(bot_message):
  send_text = 'https://api.telegram.org/bot' + credentials.bot_token + '/sendMessage?chat_id=' + credentials.bot_chatID + '&parse_mode=markdown&text=' + bot_message
  response = requests.get(send_text)
  return response.json()


for i in range(1,4):
    telegram_bot_sendtext(urllib.parse.quote(reddit.posts[i])) #urllib.parse.quote URL encodes the message
    time.sleep(21600)
