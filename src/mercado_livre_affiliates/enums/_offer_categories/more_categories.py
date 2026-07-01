from .base import BaseOfferCategory


class EsotericismAndOccultism(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Esotericism and Occultism"


class TattooEquipment(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Tattoo Equipment"


class MoreCategories(BaseOfferCategory):
    TATTOO_EQUIPMENT = TattooEquipment
    ESOTERICISM_AND_OCCULTISM = EsotericismAndOccultism

    @classmethod
    def value(cls) -> str:
        return "More Categories"
    