from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

in_kb_help = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='популярные коктейли', callback_data='популярные коктейли'
            ),
            InlineKeyboardButton(
                text='случайный коктейль', callback_data='случайный коктейль'
            ),
        ],
        [
            InlineKeyboardButton(
                text='Ссылка на сайт по которому я сделан',
                url='https://www.thecocktaildb.com/'
            ),
        ],
        [
            InlineKeyboardButton(
                text='Открыть меню', callback_data='Открыть меню'
            ),
        ],
    ]
)
