import logging

from aiogram import dispatcher

from data.config import ADMIN


async def on_startup_notify(dp: dispatcher):
    try:
        text = 'Бот запущен'
        await dp.bot.send_message(chat_id=ADMIN, text=text)
    except Exception as err:
        logging.exception(err)
