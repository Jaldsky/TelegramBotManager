from dataclasses import dataclass
from telethon import TelegramClient

from app.lib.base_bot import BaseBot, BaseEvent


class TechnoMaxEvents(BaseEvent):

    def run_events(self):
        pass


@dataclass
class TechnoMaxBot(BaseBot):
    client: TelegramClient
    bot_path: str

    async def process(self, params: dict = None):
        pass
