
from hikkatl.types import Message
from .. import loader

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
class MyModule(loader.Module):
    """YtkasFact"""
    strings = {"name": "MyModule", "hello": "Hello world!"}
    strings_ru = {"hello": "Привет мир!"}

    @loader.command(
        ru_doc="Привет мир!",
        # ...
    )
    async def helloworld(self, message: Message):
        """Hello world"""
        await utils.answer(message, self.strings("hello"))