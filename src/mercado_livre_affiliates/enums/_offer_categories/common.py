from .base import BaseOfferCategory


class Others(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Others"
    