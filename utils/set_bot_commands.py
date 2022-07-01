from aiogram import types


async def set_default_commands(dp):
    """Формирует список основых команд"""
    await dp.bot.set_my_commands([
        types.BotCommand('start', ' Запустить бота'),
        types.BotCommand('help', 'Помощь'),
    ])
