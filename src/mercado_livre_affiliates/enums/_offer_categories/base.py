from abc import ABC, abstractmethod


class BaseOfferCategory(ABC):
    @classmethod
    @abstractmethod
    def value(cls) -> str:
        pass
