from configparser import ConfigParser
from dataclasses import dataclass
from telethon import TelegramClient


@dataclass
class Config:
    """Configuration class."""
    CONFIG_PATH: str

    def __post_init__(self):
        """Initialization of sensitive data."""
        conf: ConfigParser = ConfigParser()
        conf.read(self.CONFIG_PATH)
        self.api_id: int = int(conf.get('Application', 'ApiId'))
        self.api_hash: str = conf.get('Application', 'ApiHash')
        self.token: str = conf.get('BotSettings', 'Token')


class TgClient(Config):

    @property
    def instance(self):
        return TelegramClient('bot', self.api_id, self.api_hash)

    @property
    def start(self):
        return self.instance.start(bot_token=self.token)
