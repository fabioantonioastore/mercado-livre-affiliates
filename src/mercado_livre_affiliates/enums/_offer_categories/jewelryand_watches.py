from .base import BaseOfferCategory
from .common import Others


class Watches(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Watches"


class JewelryBox(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Jewelry Box"


class Piercings(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Piercings"


class PreciousAndSemiPreciousStones(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Precious and Semi-precious Stones"


class FineJewelryAndCostumeJewelry(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Fine Jewelry and Costume Jewelry"


class JewelryItems(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Jewelry Items"


class WatchAccessories(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Watch Accessories"


class JewelryAndWatches(BaseOfferCategory):
    WATCH_ACCESSORIES = WatchAccessories
    JEWELRY_ITEMS = JewelryItems
    FINE_JEWELRY_AND_COSTUME_JEWELRY = FineJewelryAndCostumeJewelry
    OTHERS = Others
    PRECIOUS_AND_SEMI_PRECIOUS_STONES = PreciousAndSemiPreciousStones
    PIERCINGS = Piercings
    JEWELRY_BOX = JewelryBox
    WATCHES = Watches

    @classmethod
    def value(cls) -> str:
        return "Jewelry and Watches"
    