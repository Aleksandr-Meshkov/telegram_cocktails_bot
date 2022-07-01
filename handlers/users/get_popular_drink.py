from aiogram import types

from loader import dp
from filters.popular_filter import IsPopular_drink
from get_parse_api import (get_api, get_new_image,
                           get_information_drink)

from data.config import ENDPOINT


@dp.message_handler(IsPopular_drink())
async def get_info_drink(message: types.Message):
    """Отправляет сообщение с полной информацией запрашиваемого напитка."""
    response = get_api(ENDPOINT['url_search'], message.text)
    image = get_new_image(response)
    await message.answer_photo(image)
    text = get_information_drink(response)
    await message.answer(text, parse_mode=types.ParseMode.HTML)
