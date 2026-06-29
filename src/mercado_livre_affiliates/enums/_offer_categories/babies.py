from .base import BaseOfferCategory


class BabySafety(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Baby Safety"


class BabysHealth(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Baby's Health"


class BabyClothes(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Baby Clothes"


class BabysRoom(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Baby's Room"


class BabyStroll(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Baby Stroll"


class Maternity(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Maternity"


class BabyHygieneAndCare(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Baby Hygiene and Care"


class PacifiersAndTeethers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Pacifiers and Teethers"


class Playpen(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Playpen"


class BabyToys(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Baby Toys"


class BabysBath(BaseException):
    @classmethod
    def value(cls) -> str:
        return "Baby's Bath"


class WalkersAndRideOnToys(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Walkers and Ride-on Toys"


class NutritionAndBreastfeeding(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Nutrition and Breastfeeding"


class Babies(BaseOfferCategory):
    NUTRITION_AND_BREASTFEEDING = NutritionAndBreastfeeding
    WALKERS_AND_RIDE_ON_TOYS = WalkersAndRideOnToys
    BABYS_BATH = BabysBath
    BABY_TOYS = BabyToys
    PLAYPEN = Playpen
    PACIFIERS_AND_TEETHERS = PacifiersAndTeethers
    BABY_HYGIENE_AND_CARE = BabyHygieneAndCare
    MATERNITY = Maternity
    BABY_STROLL = BabyStroll
    BABYS_ROOM = BabysRoom
    BABY_CLOTHES = BabyClothes
    BABYS_HEALTH = BabysHealth
    BABY_SAFETY = BabySafety

    @classmethod
    def value(cls) -> str:
        return "Babies"
