from .base import BaseOfferCategory
from .common import Others


class PhysicalBooks(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Physical Books"


class BooksMagazinesAndComics(BaseOfferCategory):
    PHYSICAL_BOOKS = PhysicalBooks
    OTHERS = Others

    @classmethod
    def value(cls) -> str:
        return "Books, Magazines, and Comics"
