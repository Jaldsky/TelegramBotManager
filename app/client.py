from os import path, getcwd
from configparser import ConfigParser
from dataclasses import dataclass
from telethon import TelegramClient

from app.lib.formate import camel_to_snake
from app.bots.cyber_chirik_bot.cyber_chirik_bot import CyberChirikBot
from app.bots.techno_max_bot.techno_max_bot import TechnoMaxBot


@dataclass
class Config:
    """Configuration class."""
    CONFIG_PATH: str = path.join(getcwd(), 'app', 'config.ini')

    def __post_init__(self) -> None:
        """Initialization of sensitive data."""
        conf: ConfigParser = ConfigParser()
        conf.read(self.CONFIG_PATH)

        self.api_id: int = int(conf.get('Application', 'ApiId'))
        self.api_hash: str = conf.get('Application', 'ApiHash')

        for token, value in conf.items('BotsSettings'):
            # the sequence of tokens holds significance
            setattr(self, token, value)


class Client(Config):
    BOTS_PATH = path.join(getcwd(), 'app', 'bots')

    def __init__(self):
        super().__post_init__()

        self.bots = (
            CyberChirikBot(
                self.start_client('CyberChirikBot', token=self.token1),
                self.get_bot_path('CyberChirikBot')
            ).process(),
            TechnoMaxBot(
                self.start_client('TechnoMaxBot', token=self.token2),
                self.get_bot_path('TechnoMaxBot')
            ).process()
        )

    def start_client(self, bot_name: str, token: str):
        return self.get_client(bot_name).start(bot_token=token)

    def get_client(self, bot_name: str) -> TelegramClient:
        bot_session_path = path.join(self.get_bot_path(bot_name), 'session', bot_name)
        return TelegramClient(bot_session_path, self.api_id, self.api_hash)

    def get_bot_path(self, bot_name: str) -> str:
        return path.join(self.BOTS_PATH, camel_to_snake(bot_name))
