from telethon import TelegramClient, sync
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.custom import Message
from telethon.client.messages import _MessagesIter

import json
#https://t.me/Krsk_deto44ka
api_id = 26879719
api_hash = 'e0fd576f80e6729a5770c206bd70288a'

def start():
    client = TelegramClient('pars_gruop', api_id, api_hash)
    client.start()
    chanel = client.get_entity('https://t.me/Krsk_deto44ka')
    offset_msg = 0  # номер записи, с которой начинается считывание
    limit_msg = 100  # максимальное число записей, передаваемых за один раз

    all_messages = []  # список всех сообщений
    total_messages = 0
    total_count_limit = 0
    history = client(Message(
			peer=chanel,
			offset_id=offset_msg,
			offset_date=None, add_offset=0,
			limit=limit_msg, max_id=0, min_id=0,
			hash=0))
    histora = client.iter_messages('https://t.me/Krsk_deto44ka')
    print(history)

    #for i in Message(history.messages):
        #print(i)

    #for mesaga in client.iter_messages(chanel):

        #if mesaga.message:
            #print(mesaga.photo)
            #break



#https://t.me/Krsk_deto44ka/5844
#https://t.me/Krsk_deto44ka/5843
if __name__ == '__main__':
    start()


