from os import path, getcwd
from asyncio import gather, create_task, get_event_loop
from configparser import ConfigParser
from dataclasses import dataclass
from telethon import TelegramClient

from app.lib.formate import camel_to_snake
from app.bots.cyber_chirik_bot.cyber_chirik_bot import CyberChirikBot
from app.bots.techno_max_bot.techno_max_bot import TechnoMaxBot
from app.bots.giga_brain_bot.giga_brain_bot import GigaBrainBot


@dataclass
class Config:
    """Configuration class."""
    CONFIG_PATH: str = path.join(getcwd(), 'app', 'config.ini')

    def _init_main_config(self) -> None:
        """Commence the establishment of fundamental parameter nomenclature."""
        self.__main_section = 'Application'
        self.__api_id_option = 'ApiId'
        self.__api_hash_option = 'ApiHash'

    def _init_custom_params(self, conf: ConfigParser) -> None:
        """Initialization of custom confidential parameters."""
        for section in conf.sections():
            if section != self.__main_section:
                for param, value in conf.items(section):
                    setattr(self, f'{section}_{param}', value)

    def __post_init__(self) -> None:
        """Initialization of sensitive data."""
        self._init_main_config()

        conf: ConfigParser = ConfigParser()
        conf.read(self.CONFIG_PATH)

        if not conf.has_section(self.__main_section):
            raise Exception
        if not conf.has_option(self.__main_section, self.__api_id_option):
            raise Exception
        if not conf.has_option(self.__main_section, self.__api_hash_option):
            raise Exception

        self.api_id: int = int(conf.get(self.__main_section, self.__api_id_option))
        self.api_hash: str = conf.get(self.__main_section, self.__api_hash_option)

        self._init_custom_params(conf)


class Client(Config):
    BOTS_PATH = path.join(getcwd(), 'app', 'bots')

    def _init_bot(self, instance):
        bot_name: str = instance.__name__
        token_var: str = f'{bot_name}_token'
        if hasattr(self, token_var):
            return instance(
                self.start_client(bot_name, token=getattr(self, token_var)),
                self.get_bot_path(bot_name)
            )

    def __init__(self):
        super().__post_init__()

        self.bots = (
            self._init_bot(CyberChirikBot),
            # self._init_bot(TechnoMaxBot),
            self._init_bot(GigaBrainBot)
        )
        get_event_loop().run_until_complete(self.run_bots())

    async def run_bots(self):
        await gather(*[create_task(bot.process()) for bot in self.bots])

    def start_client(self, bot_name: str, token: str):
        return self.get_client(bot_name).start(bot_token=token)

    def get_client(self, bot_name: str) -> TelegramClient:
        bot_session_path = path.join(self.get_bot_path(bot_name), 'session', bot_name)
        return TelegramClient(bot_session_path, self.api_id, self.api_hash)

    def get_bot_path(self, bot_name: str) -> str:
        return path.join(self.BOTS_PATH, camel_to_snake(bot_name))
