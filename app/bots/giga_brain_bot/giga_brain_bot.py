from dataclasses import dataclass
from telethon import TelegramClient, events
from openai import OpenAI
from json import loads

from app.lib.base_bot import BaseBot, BaseEvent


class GigaBrainBotEvents(BaseEvent):
    TOKEN_LIMIT = 3000
    GPT_MODEL = 'gpt-3.5-turbo-instruct'

    def __init__(self, client: TelegramClient, bot_path: str, params: dict = None) -> None:
        self.client = client
        self.openai_client = OpenAI(api_key=params['GigaBrainBot_chatgpt_token'])
        self.trusted_users = loads(params['GigaBrainBot_trusted_users'])

        self.context_enabled = False
        self.context = []

    def ask_gpt(self, user_msg: str):
        prompt = '\n'.join(self.context + [user_msg])
        response = self.openai_client.completions.create(
            model=self.GPT_MODEL,
            prompt=prompt,
            max_tokens=self.TOKEN_LIMIT
        )
        return response.choices[0].text.strip()

    async def handle_send_chatgpt(self, event):
        user_msg = event.raw_text
        if user_msg == '/context':
            self.context_enabled = True
            await event.reply("Контекст включен.")
            return None
        elif user_msg == '/cancel_context':
            self.context_enabled = False
            self.context = []
            await event.reply("Контекст отключен.")
            return None

        response = self.ask_gpt(user_msg)
        if self.context_enabled:
            self.context.append(response)
        await event.reply(response)

    def run_events(self, params: dict = None):
        self.client.add_event_handler(self.handle_send_chatgpt, events.NewMessage(from_users=self.trusted_users))


@dataclass
class GigaBrainBot(BaseBot):
    client: TelegramClient
    bot_path: str

    async def process(self, params: dict = None):
        GigaBrainBotEvents(self.client, self.bot_path, params).run_events()
        await self.client.run_until_disconnected()
