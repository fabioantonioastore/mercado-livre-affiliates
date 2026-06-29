from .base import BaseOfferCategory


class CropProtection(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Crop Protection"


class AnimalProduction(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Animal Production"


class AgriculturalMachineryParts(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Agricultural Machinery Parts"


class AgriculturalMachinery(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Agricultural Machinery"


class LivestockSupplies(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Livestock Supplies"


class AgriculturalInputs(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Agricultural Inputs"


class RuralInfrastructure(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Rural Infrastructure"


class WorkTools(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Work Tools"


class RenewableEnergy(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Renewable Energy"


class Storage(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Storage"


class Beekeeping(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Beekeeping"


class Agribusiness(BaseOfferCategory):
    BEEKEEPING = Beekeeping
    STORAGE = Storage
    RENEWABLE_ENERGY = RenewableEnergy
    WORK_TOOLS = WorkTools
    RURAL_INFRASTRUCTURE = RuralInfrastructure
    AGRICULTURAL_INPUTS = AgriculturalInputs
    LIVESTOCK_SUPPLIES = LivestockSupplies
    AGRICULTURAL_MACHINERY = AgriculturalMachinery
    AGRICULTURAL_MACHINERY_PARTS = AgriculturalMachineryParts
    ANIMAL_PRODUCTION = AnimalProduction
    CROP_PROTECTION = CropProtection

    @classmethod
    def value(cls) -> str:
        return "Agribusiness"
