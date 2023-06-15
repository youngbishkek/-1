from telethon import TelegramClient, events

api_id = '20904033'
api_hash = '76d5b1af83337d4a2129aed1456dc2b7'

source_channel_ids = [-1001708761316,-1001050820672,-1001394050290,-1001101170442,-1001117628569, -1001099860397]
destination_channel_id = -1001988868149

# Создаем клиента Telegram
client = TelegramClient('session_name', api_id, api_hash)


# Обработчик событий для новых входящих сообщений в исходных каналах
@client.on(events.NewMessage(chats=source_channel_ids))
async def handle_new_message(event):
    # Получаем новое сообщение
    message = event.message
    
    # Пересылаем сообщение в целевой канал
    await message.forward_to(destination_channel_id)


# Запускаем клиента Telegram
with client:
    client.run_until_disconnected()
добавь функцию чтобы бот мог пересылать рандомное сообщение в боте каждый час , но чтобы в начале работы бота можно было также выбрать чтобы пересылал только новые посты
