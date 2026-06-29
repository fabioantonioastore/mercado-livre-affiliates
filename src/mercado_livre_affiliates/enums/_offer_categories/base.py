from typing import Self
from abc import ABC, abstractmethod


class BaseOfferCategory(ABC):
    def __new__(cls) -> Self:
        raise RuntimeError("This class cannot be instanciated")

    @classmethod
    @abstractmethod
    def value(cls) -> str:
        pass
