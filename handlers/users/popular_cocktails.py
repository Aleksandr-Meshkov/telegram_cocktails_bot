from aiogram import types

from loader import dp
from keybords.default import kb_pop_cock


@dp.message_handler(text='Популярные коктейли')
async def popular_cocktail(message: types.Message):
    """Открывает клавиатуру с кнопками."""
    await message.answer(
        'Здесь собраны наиболее популярные коктейли!\n'
        'Выбери понравившейся себе из списка ниже и \n'
        'узнай, что понадобится для его приготовления!',
        reply_markup=kb_pop_cock
    )
