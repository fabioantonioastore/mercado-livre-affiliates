from .base import BaseOfferCategory
from .common import Others


class Dresses(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Dresses"


class Suits(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Suits"


class Skirts(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Skirts"


class BabyClothes(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Baby Clothes"


class IntimateApparelAndLingerie(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Intimate Apparel and Lingerie"


class Beachwear(BaseOfferCategory):
    @classmethod
    def valeu(cls) -> str:
        return "Beachwear"


class Activewear(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Activewear"


class SuitcasesAndBags(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Suitcases and Bags"


class Overalls(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Overalls"


class Leggings(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Leggings"


class ClothingSetKits(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Clothing Set Kits"


class WorkAndSchoolAttire(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Work and School Attire"


class TShirtsAndTankTops(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "T-shirts and Tank Tops"


class Shirts(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Shirts"


class Pants(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Pants"


class Footwear(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Footwear"


class Blouses(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Blouses"


class BermudaShortsAndShorts(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Bermuda Shorts and Shorts"


class Outerwear(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Outerwear"


class FashionAccessories(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Fashion Accessories"


class FootwearClothingAndBags(BaseOfferCategory):
    FASHION_ACCESSORIES = FashionAccessories
    OUTERWEAR = Outerwear
    BERMUDA_SHORTS_AND_SHORTS = BermudaShortsAndShorts
    BLOUSES = Blouses
    FOOTWEAR = Footwear
    PANTS = Pants
    SHIRTS = Shirts
    T_SHIRTS_AND_TANK_TOPS = TShirtsAndTankTops
    WORK_AND_SCHOOL_ATTIRE = WorkAndSchoolAttire
    CLOTHING_SET_KITS = ClothingSetKits
    LEGGINGS = Leggings
    OVERALLS = Overalls
    SUITCASES_AND_BAGS = SuitcasesAndBags
    ACTIVEWEAR = Activewear
    BEACHWEAR = Beachwear
    INTIMATE_APPARE_AND_LINGERIE = IntimateApparelAndLingerie
    OTHERS = Others
    BABY_CLOTHES = BabyClothes
    SKIRTS = Skirts
    SUITS = Suits
    DRESSES = Dresses

    @classmethod
    def value(cls) -> str:
        return "Footwear, Clothing, and Bags"
