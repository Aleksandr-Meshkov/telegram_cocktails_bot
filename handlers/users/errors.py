from aiogram import types

from loader import dp


@dp.message_handler()
async def catch_some_text(message: types.Message):
    await message.answer(
        'Упс, такой команды нет, но возможно она появится потом!'
    )


@dp.message_handler(content_types=types.ContentType.ANY)
async def cath_some_not_text(message: types.Message):
    await message.answer(
        'Ух, классно, но я пока что не умею отвечать правильно\n'
        f'на такие сообщения: <b>{message.content_type}</b>'
        )
