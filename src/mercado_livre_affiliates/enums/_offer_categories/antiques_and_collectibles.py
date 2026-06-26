from .base import BaseOfferCategory


class TacticalGear(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Tactical Gear"


class KnifeSheaths(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Knife Sheaths"


class MilitariaAndRelatedItems(BaseOfferCategory):
    knife_sheaths = KnifeSheaths
    tactical_gear = TacticalGear

    @classmethod
    def value(cls) -> str:
        return "Militaria and Related Items"


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


class Trophy(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Trophy"


class MedalHolder(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Medal Holder"


class Antiques(BaseOfferCategory):
    medal_holder = MedalHolder
    trophy = Trophy

    @classmethod
    def value(cls) -> str:
        return "Antiques"


class AntiquesAndCollectibles(BaseOfferCategory):
    antiques = Antiques
    flags = Flags
    banknotes_and_coins = BanknotesAndCoins
    sculptures = Sculptures
    militaria_and_related_items = MilitariaAndRelatedItems

    @classmethod
    def value(cls) -> str:
        return "Antiques and Collectibles"
