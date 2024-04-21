
from hikkatl.types import Message
from ... import loader, utils

import requests
from bs4 import BeautifulSoup

def get_fact():
    try:
        response = requests.get('https://randstuff.ru/fact/')
        page = BeautifulSoup(response.content, 'html.parser')
        fact = page.find('table', {'class': 'text'}).get_text(strip=True)
        return fact
    except Exception as error:
        return "Извините, не смог найти интересный факт для вас. Попробуйте ещё раз!"


@loader.tds
class YtkasFactModule(loader.Module):
    developer = "@ytkamods"
    """YtkasModule"""
    strings = {"name": "YtkasFact", "fact": "Random fact"}
    strings_ru = {"fact": "Случайный факт"}

    @loader.command(
        ru_doc="Вывести случайный факт",
        en_doc="send random fact",
        # ...
    )
    async def fact(self, message: Message):
        """Send random fact"""
        await utils.answer(message, self.strings(get_fact()))
