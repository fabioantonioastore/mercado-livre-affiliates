from .base import BaseOfferCategory


class FlooringAndGrout(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Flooring and Grout"


class ConstructionMachinery(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Construction Machinery"


class KitchenFurniture(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Kitchen Furniture"


class BathroomFurniture(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Bathroom Furniture"


class ConstructionMaterials(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Construction Materials"


class PaintShop(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Paint Shop"


class Energy(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Energy"


class Plumbing(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Plumbing"


class ConstructionAccessories(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Construction Accessories"


class Openings(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Openings"


class Construction(BaseOfferCategory):
    OPENINGS = Openings
    CONSTRUCTION_ACCESSORIES = ConstructionAccessories
    PLUMBING = Plumbing
    ENERGY = Energy
    PAINT_SHOP = PaintShop
    CONSTRUCTION_MATERIALS = ConstructionMaterials
    BATHROOM_FURNITURE = BathroomFurniture
    KITCHEN_FURNITURE = KitchenFurniture
    CONSTRUCTION_MACHINERY = ConstructionMachinery
    FLOORING_AND_GROUT = FlooringAndGrout

    @classmethod
    def value(cls) -> str:
        return "Construction"
    