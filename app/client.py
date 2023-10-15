from os import path, getcwd
from configparser import ConfigParser
from dataclasses import dataclass
from telethon import TelegramClient

from app.bots.cyber_chirik_bot import CyberChirikBot
from app.bots.techno_max_bot import TechnoMaxBot


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
    SESSION_PATH = path.join(getcwd(), 'app', 'bots', 'sessions')

    def __init__(self):
        super().__post_init__()

        self.bots = (
            CyberChirikBot(
                self.start_client('CyberChirikBot', token=self.token1)
            ).process(),
            TechnoMaxBot(
                self.start_client('TechnoMaxBot', token=self.token2)
            ).process()
        )

    def start_client(self, bot_name: str, token: str):
        return self.get_client(bot_name).start(bot_token=token)

    def get_client(self, bot_name: str) -> TelegramClient:
        bot_session_path = path.join(self.SESSION_PATH, bot_name)
        return TelegramClient(bot_session_path, self.api_id, self.api_hash)
