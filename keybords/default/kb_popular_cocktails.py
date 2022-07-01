from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_pop_cock = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Mojito'),
            KeyboardButton(text='Old Fashioned'),
        ],
        [
            KeyboardButton(text='Long Island Tea'),
            KeyboardButton(text='Negroni'),
        ],
        [
            KeyboardButton(text='Whiskey Sour'),
            KeyboardButton(text='Dry Martini'),
        ],
        [
            KeyboardButton(text='Daiquiri'),
            KeyboardButton(text='Margarita'),
        ],
        [
            KeyboardButton(text='Go back to the menu'),
        ]
    ],
    resize_keyboard=True
)
