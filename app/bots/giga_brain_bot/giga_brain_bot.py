from os import path, getcwd
from dataclasses import dataclass
from jinja2 import Environment, FileSystemLoader
from telethon import TelegramClient, events

from app.bots.base_bot import BaseBot, BaseEvent
from app.bots.cyber_chirik_bot.logic.sender_variations import send_greeting_personal


class GigaBrainBotEvents(BaseEvent):

    def __init__(self, client: TelegramClient, bot_path: str) -> None:
        self.client = client

    def run_events(self):
        pass


@dataclass
class GigaBrainBot(BaseBot):
    client: TelegramClient
    bot_path: str

    async def process(self):
        GigaBrainBotEvents(self.client, self.bot_path).run_events()
        await self.client.run_until_disconnected()
