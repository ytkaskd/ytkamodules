
from hikkatl.types import Message
from .. import loader

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
