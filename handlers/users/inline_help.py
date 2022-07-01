from aiogram.types import CallbackQuery

from loader import dp
from keybords.default import kb_choice


@dp.callback_query_handler(text='популярные коктейли')
async def message_info_popular(call: CallbackQuery):
    """Информирует о возможности кнопки."""
    await call.answer(
        'Эта команда перейдет в меню выбора\n популярных коктейлей!',
        show_alert=True
    )


@dp.callback_query_handler(text='случайный коктейль')
async def message_info_random(call: CallbackQuery):
    """Информирует о возможности кнопки."""
    await call.answer(
        'Эта команда выдаст случайный коктейль\n с его полным описанием!',
        show_alert=True
    )


@dp.callback_query_handler(text='Открыть меню')
async def message_info_menu(call: CallbackQuery):
    """Перенаправляет в главное меню бота."""
    await call.message.answer(
        'Окей! А теперь выбери себе напиток',
        reply_markup=kb_choice
    )
