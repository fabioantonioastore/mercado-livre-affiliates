from .base import BaseOfferCategory
from .common import Others


class UniformsAndWorkwear(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Uniforms and Workwear"


class TextilesAndFootwear(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Textiles and Footwear"


class WorkplaceSafety(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Workplace Safety"


class AdvertisingAndPromotion(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Advertising and Promotion"


class PrintingServices(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Printing Services"


class GastronomyAndHospitality(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Gastronomy and Hospitality"


class IndustrialTools(BaseOfferCategory):
    @classmethod
    def valeu(cls) -> str:
        return "Industrial Tools"


class OfficeEquipment(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Office Equipment"


class CommercialEquipment(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Commercial Equipment"


class MedicalEquipment(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Medical Equipment"


class PackagingAndLogistics(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Packaging and Logistics"


class ArchitectureAndDesign(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Architecture and Design"


class IndustryAndCommerce(BaseOfferCategory):
    ARCHITECTURE_AND_DESIGN = ArchitectureAndDesign
    PACKAGING_AND_LOGISTICS = PackagingAndLogistics
    MEDICAL_EQUIPMENT = MedicalEquipment
    COMMERCIAL_EQUIPMENT = CommercialEquipment
    OFFICE_EQUIPMENT = OfficeEquipment
    INDUSTRIAL_TOOLS = IndustrialTools
    GASTRONOMY_AND_HOSPITALITY = GastronomyAndHospitality
    PRINTING_SERVICES = PrintingServices
    OTHERS = Others
    ADVERTISING_AND_PROMOTION = AdvertisingAndPromotion
    WORKPLACE_SAFETY = WorkplaceSafety
    TEXTILES_AND_FOOTWEAR = TextilesAndFootwear
    UNIFORMS_AND_WORKWEAR = UniformsAndWorkwear

    @classmethod
    def value(cls) -> str:
        return "Industry and Commerce"
