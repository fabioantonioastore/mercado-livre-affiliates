from .base import BaseOfferCategory
from .common import Others


class Refrigeration(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Refrigeration"


class SmallAppliances(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Small Appliances"


class Washers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Washers"


class OvensAndStoves(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Ovens and Stoves"


class PersonalCare(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Personal Care"


class WaterCoolersAndPurifiers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Water Coolers and Purifiers"


class AirAndVentilation(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Air and Ventilation"


class HomeAppliances(BaseOfferCategory):
    AIR_AND_VENTILATION = AirAndVentilation
    WATER_COOLERS_AND_PURIFIERS = WaterCoolersAndPurifiers
    PERSONAL_CARE = PersonalCare
    OVENS_AND_STOVES = OvensAndStoves
    WASHERS = Washers
    OTHERS = Others
    SMALL_APPLIANCES = SmallAppliances
    REFRIGERATION = Refrigeration

    @classmethod
    def value(cls) -> str:
        return "Home Appliances"
