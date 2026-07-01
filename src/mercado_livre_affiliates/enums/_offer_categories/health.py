from .base import BaseOfferCategory
from .common import Others


class AlternativeTherapies(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Alternative Therapies"


class DietarySupplements(BaseOfferCategory):
    @classmethod
    def valeu(cls) -> str:
        return "Dietary Supplements"


class Orthopedics(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Orthopedics"


class Mobility(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Mobility"


class Massage(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Massage"


class MedicalEquipment(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Medical Equipment"


class Healthcare(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Healthcare"


class Health(BaseOfferCategory):
    HEALTHCARE = Healthcare
    MEDICAL_EQUIPMENT = MedicalEquipment
    MASSAGE = Massage
    MOBILITY = Mobility
    ORTHOPEDICS = Orthopedics
    OTHERS = Others
    DIETARY_SUPPLEMENTS = DietarySupplements
    ALTERNATIVE_THERAPIES = AlternativeTherapies

    @classmethod
    def value(cls) -> str:
        return "Health"
