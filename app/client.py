from dataclasses import dataclass
from telethon import TelegramClient


@dataclass
class TgClient:
    api_id: int
    api_hash: str
    token: str

    @property
    def instance(self):
        return TelegramClient('bot', self.api_id, self.api_hash)

    @property
    def start(self):
        return self.instance.start(bot_token=self.token)
