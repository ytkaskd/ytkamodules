from hikkatl.types import Message
from .. import loader, utils

import requests
from bs4 import BeautifulSoup # type: ignore


def get_fact():
        try:
            response = requests.get('https://randstuff.ru/fact/')
            page = BeautifulSoup(response.content, 'html.parser')
            fact = page.find('table', {'class': 'text'}).get_text(strip=True)
            return fact
        except Exception as error:
            return "Извините, не смог найти интересный факт для вас. Попробуйте ещё раз!"

@loader.tds
class FactModule(loader.Module):
    """Fact module"""
    strings = {"name": "FactModule", "fact": "Random Fact"}

    @loader.command(
              en_doc="Random Fact",
    )
    async def fact(self, message: Message):
        """Random fact"""
        await utils.answer(message, get_fact())
