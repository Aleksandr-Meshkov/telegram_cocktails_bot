from aiogram import types

from loader import dp
from keybords.default import kb_choice


@dp.message_handler(commands='start')
async def command_start(message: types.Message):
    text = (
        f'<b>Приветствую, {message.from_user.full_name}!</b> \n'
        f'Это телеграм бот, который поможет тебе создать хорошее настроение.\n'
        f'Здесь ты сможешь подобрать для себя напиток по вкусу!\n'
        f'Если вдруг тебе понадобиться помощь, просто набери команду\n/help'
    )
    await message.answer(text, reply_markup=kb_choice)
