from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from data.config import POPULAR_COCKTAILS


class IsPopular_drink(BoundFilter):

    async def check(self, message: types.Message):
        if message.text in POPULAR_COCKTAILS:
           return message.text