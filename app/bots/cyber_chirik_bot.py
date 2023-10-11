from dataclasses import dataclass

from app.bots.base_bot import BaseBot, BaseEvent


class CyberChirikBotEvents(BaseEvent):
    pass


@dataclass
class CyberChirikBot(BaseBot):

    def process(self):
        pass
