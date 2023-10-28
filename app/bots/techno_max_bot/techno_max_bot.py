from dataclasses import dataclass

from telethon import TelegramClient

from app.bots.base_bot import BaseBot, BaseEvent


class TechnoMaxEvents(BaseEvent):
    pass


@dataclass
class TechnoMaxBot(BaseBot):
    client: TelegramClient
    bot_path: str

    def process(self):
        pass
