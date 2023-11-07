from os import path, getcwd
from dataclasses import dataclass
from jinja2 import Environment, FileSystemLoader
from telethon import TelegramClient, events

from app.bots.base_bot import BaseBot, BaseEvent
from app.bots.cyber_chirik_bot.logic.sender_variations import send_greeting_personal


class CyberChirikBotEvents(BaseEvent):

    def __init__(self, client: TelegramClient, bot_path: str) -> None:
        self.client = client
        self.templates = Environment(loader=FileSystemLoader(path.join(bot_path, 'templates')))

    async def handle_greeting(self, event):
        sender = await event.get_sender()
        await event.respond(send_greeting_personal(name=sender.first_name))

    async def handle_info(self, event):
        sender = await event.get_sender()
        template = self.templates.get_template('info_template.jinja').render(
            greeting=send_greeting_personal(name=sender.first_name))
        await event.respond(template)

    def run_events(self):
        self.client.add_event_handler(self.handle_info, events.NewMessage(pattern='/info'))
        self.client.add_event_handler(self.handle_greeting, events.NewMessage(pattern='/hi'))


@dataclass
class CyberChirikBot(BaseBot):
    client: TelegramClient
    bot_path: str

    async def process(self):
        CyberChirikBotEvents(self.client, self.bot_path).run_events()
        await self.client.run_until_disconnected()

