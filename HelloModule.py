from hikkatl.types import Message
from ... import loader


@loader.tds
class HelloModule(loader.Module):
    """HelloModule"""
    strings = {"name": "HelloModule", "hello": "Hello world!"}
    strings_ru = {"hello": "Привет мир!"}

    @loader.command(
        ru_doc="Привет мир!",
        # ...
    )
    async def hi(self, message: Message):
        """Say Hello World"""
        await utils.answer(message, self.strings("hello"))
