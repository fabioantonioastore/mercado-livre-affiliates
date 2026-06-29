from .base import BaseOfferCategory


class SchoolSupplies(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "School Supplies"


class HaberdasherySupplies(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Haberdashery Supplies"


class ArtAndCrafts(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Art and Crafts"


class ArtSuppliesStationeryAndHaberdashery(BaseOfferCategory):
    ART_AND_CRAFTS = ArtAndCrafts
    HABERDASHERY_SUPPLIES = HaberdasherySupplies
    SCHOOL_SUPPLIES = SchoolSupplies

    @classmethod
    def value(cls) -> str:
        return "Art Supplies, Stationery, and Haberdashery"
