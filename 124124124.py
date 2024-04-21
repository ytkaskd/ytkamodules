
from hikkatl.types import Message
from ... import loader, utils

import requests
#from bs4 import BeautifulSoup # type: ignore



@loader.tds
class FactModule(loader.Module):
    """FactModule"""
    developer = "@ytkamods"
    strings = {"name": "YtkasFact", "fact": "Random fact"}
    strings_ru = {"fact": "Случайный факт"}

    def get_fact():
        try:
            response = requests.get('https://randstuff.ru/fact/')
            page = BeautifulSoup(response.content, 'html.parser')
            fact = page.find('table', {'class': 'text'}).get_text(strip=True)
            return fact
        except Exception as error:
            return "Извините, не смог найти интересный факт для вас. Попробуйте ещё раз!"


    @loader.command(
        ru_doc="Вывести случайный факт",
        # ...
    )
    async def fact(self, message: Message):
        """Send random fact"""
        await utils.answer(message, self.strings(get_fact()))
