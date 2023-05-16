from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from bot_config import telegram_token

bot = Bot(telegram_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start','cтарт'])
async def send_hellow(message: types.message):
    await bot.send_message(message.from_user.id,'Привет! Я - телеграм бот.\nЯ помогаю Лиане вести ее персональный '
                                                'телеграм канал.\nОтправь мне команду или воспользуйся '
                                                'командами на клавиатуре. Надеюсь, вы останетесь довольны '
                                                'моей работой!')










@dp.message_handler()
async def send_echo(message: types.message):
    try:
        await bot.send_message(message.from_user.id, 'Данная команда мне не известна.\nЕсли у Вас есть идеи '
                                                     'по улучшению моей работы, обратитесь к разработчику '
                                                     'или владельцу')
        await message.delete()
    except:
        await message.reply('Для общения с ботом, напишите ему личное сообщение:\nhttps://t.me/liana_blogger_bot')
        await message.delete()






executor.start_polling(dp, skip_updates=True)