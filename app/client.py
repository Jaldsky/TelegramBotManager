from os import path, getcwd
from configparser import ConfigParser
from dataclasses import dataclass
from telethon import TelegramClient


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


class TgClient(Config):

    @property
    def instance(self):
        return TelegramClient('bot', self.api_id, self.api_hash)

    @property
    def start(self):
        return self.instance.start(bot_token=self.token)
