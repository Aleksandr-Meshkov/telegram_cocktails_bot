import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

ADMIN = int(os.getenv("ADMIN"))

TOKEN_ERROR = (
    f'Отсутствует один из ключевых токенов:'
    f'{BOT_TOKEN}, {ADMIN}'
)

POPULAR_COCKTAILS = (
    'Mojito',
    'Old Fashioned',
    'Long Island Tea',
    'Negroni',
    'Whiskey Sour',
    'Dry Martini',
    'Daiquiri',
    'Margarita'
)

ENDPOINT = {
    'url_search': 'https://thecocktaildb.com/api/json/v1/1/search.php?s=',
    'url_random': 'https://thecocktaildb.com/api/json/v1/1/random.php'
}
