from dataclasses import dataclass

from telethon import TelegramClient

from app.bots.base_bot import BaseBot, BaseEvent


class CyberChirikBotEvents(BaseEvent):
    pass


@dataclass
class CyberChirikBot(BaseBot):
    client: TelegramClient = None

    def process(self):
        pass
