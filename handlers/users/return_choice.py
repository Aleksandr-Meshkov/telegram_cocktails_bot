from aiogram import types

from loader import dp
from keybords.default import kb_choice


@dp.message_handler(text='Go back to the menu')
async def go_to_menu(message: types.Message):
    await message.answer(
        f'<b>{message.from_user.first_name}</b> '
        f'вы вернулись в главное меню бота!',
        reply_markup=kb_choice
    )
