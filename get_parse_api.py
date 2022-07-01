import logging
import requests

from data.config import BOT_TOKEN, ADMIN, ENDPOINT


def get_edpoint(part_urls):
    """Добавляет к эдпоинту название нужного коктейля."""
    part_urls = part_urls.replace(' ', '_').lower()
    endpoint = ENDPOINT['url_search'] + part_urls
    return endpoint


def get_api(endpoint, part_urls):
    """Делает запрос к Апи сервера."""
    if endpoint[-1] == '=':
        endpoint = get_edpoint(part_urls)
    try:
        logging.info('Начало запроса к серверу Api.')
        response = requests.get(endpoint).json()
    except Exception as err:
        logging.exception(f'Сбой в запросе к серверу Апи ошибка: {err}')
    return response


def get_information_drink(response):
    """Получает полную информацию о коктейле."""
    logging.info('Начало проверки ответа Апи')
    if not isinstance(response, dict):
        raise TypeError(
            f'ответ API не соответствует ожиданиям: {response}'
        )
    drink = response.get('drinks')[0]
    if 'drinks' not in response:
        logging.warning('key error')
    name_cocktail = drink.get('strDrink')
    if 'strDrink' not in drink:
        logging.warning('key error')
    category = drink.get('strAlcoholic')
    if 'strAlcoholic' not in drink:
        logging.warning('key error')
    glass = drink.get('strGlass')
    if 'strGlass' not in drink:
        logging.warning('key error')
    instructions = drink.get('strInstructions')
    if 'strInstructions' not in drink:
        logging.warning('key error')
    text_list = []
    for i in range(1, 16):
        if drink.get(f"strIngredient{i}") == None:
            continue
        ingridient = f'{drink.get(f"strIngredient{i}", None)}'
        if f"strIngredient{i}" not in drink:
            logging.warning('key error')
        measure = f'{drink.get(f"strMeasure{i}", None)}'
        if f"strMeasure{i}" not in drink:
            logging.warning('key error')
        if measure == None:
            measure = 'to your taste'
        text = ingridient + ' - ' + measure + '\n'
        text_list.append(text)
    message_text = (f"<b>Cocktail:</b> -- {name_cocktail}.\n"
                    f'<b>Category:</b> -- {category}\n'
                    f'<b>Glass:</b> -- {glass}\n'
                    f'<b>Instructions:</b> {instructions}.\n'
                    f'<b>Ingredients:</b> \n'
                    f'<u>{"".join(text_list)}</u>')
    return message_text


def get_new_image(response):
    """Получаем изображение коктейля."""
    drink = response.get('drinks')[0]
    if 'drinks' not in response:
        logging.warning('key error')
    image_drink = drink.get('strDrinkThumb')
    if 'strDrinkThumb' not in drink:
        logging.warning('key error')
    return image_drink


def check_tokens():
    """Проверяем доступность токенов."""
    return all((BOT_TOKEN, ADMIN))
