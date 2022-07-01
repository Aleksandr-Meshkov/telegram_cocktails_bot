import logging
import sys

from get_parse_api import check_tokens
from data.config import TOKEN_ERROR


async def on_startup(dp):
    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)

    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)

    print('Бот запущен')


if __name__ == '__main__':

    from aiogram import executor
    from handlers import dp

    logging.basicConfig(
        level=logging.INFO,
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler('main.log', mode='a', encoding='UTF-8')
        ],
        format=(
            '%(asctime)s, %(levelname)s, %(funcName)s, %(lineno)s, %(message)s'
        )
    )
    if not check_tokens():
        logging.critical(TOKEN_ERROR)
        sys.exit(TOKEN_ERROR)

    executor.start_polling(dp, on_startup=on_startup)
