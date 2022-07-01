from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_choice = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Популярные коктейли'),
            KeyboardButton(text='Случайный коктейль'),
        ]
    ],
    resize_keyboard=True
)
