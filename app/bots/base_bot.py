from abc import ABC, abstractmethod
from dataclasses import dataclass


class BaseEvent(ABC):
    pass


@dataclass
class BaseBot(ABC):
    pass
