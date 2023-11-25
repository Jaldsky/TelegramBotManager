from abc import ABC, abstractmethod
from dataclasses import dataclass

from telethon import TelegramClient


class BaseEvent(ABC):

    @abstractmethod
    def run_events(self):
        pass


@dataclass
class BaseBot(ABC):
    client: TelegramClient
    bot_path: str

    @abstractmethod
    async def process(self):
        pass
