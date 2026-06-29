from .base import BaseOfferCategory


class Sculptures(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Sculptures"


class BanknotesAndCoins(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Banknotes and Coins"


class Flags(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Flags"


class Antiques(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Antiques"


class AntiquesAndCollectibles(BaseOfferCategory):
    ANTIQUES = Antiques
    FLAGS = Flags
    BANKNOTES_AND_COINS = BanknotesAndCoins
    SCULPTURES = Sculptures

    @classmethod
    def value(cls) -> str:
        return "Antiques and Collectibles"
