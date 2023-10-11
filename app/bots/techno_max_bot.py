from dataclasses import dataclass


from app.bots.base_bot import BaseBot, BaseEvent


class TechnoMaxEvents(BaseEvent):
    pass


@dataclass
class TechnoMaxBot(BaseBot):

    def process(self):
        pass
