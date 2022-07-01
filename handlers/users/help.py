from aiogram import types
from loader import dp
from keybords.inline.inline_help import in_kb_help


@dp.message_handler(text='/help')
async def command_help(message: types.Message):
    """Отправляет информационное сообщение о возможностях бота."""
    await message.answer(
        f'<b>Привет {message.from_user.first_name}!</b> \n'
        f'Я телеграм Бот, мое имя Мистер Дринк.\n'
        f'Моя задача найти тебе подходящий '
        f'напиток и способ его приготовления.\n'
        f'Чтобы меня активировать нужно ввести команду /start \n'
        f'Эта команда вызывает меню с инструкциями использования бота /help \n'
        f'У меня есть определенные кнопки для взаимодействия со мной\n'
        f'их функционал начинает работать в главном меню, '
        f'список кнопок ниже!',
        reply_markup=in_kb_help
    )
