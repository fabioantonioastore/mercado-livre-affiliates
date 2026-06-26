from abc import ABC, abstractmethod
from typing_extensions import Self


class BaseOfferCategory(ABC):
    def __new__(cls) -> Self:
        raise RuntimeError("This class cannot be instanciated")

    @classmethod
    @abstractmethod
    def value(cls) -> str:
        pass
