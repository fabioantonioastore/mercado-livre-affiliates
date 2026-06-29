from .base import BaseOfferCategory


class BeautyTreatments(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Beauty Treatments"


class Perfumes(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Perfumes"


class Makeup(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Makeup"


class ManicureAndPedicure(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Manicure and Pedicure"


class PersonalHygiene(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Personal Hygiene"


class Pharmacy(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Pharmacy"


class HairRemoval(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Hair Removal"


class HairCare(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Hair Care"


class Skincare(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Skincare"


class Barbershop(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Barbershop"


class HairdressingSupplies(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Hairdressing Supplies"


class HairAccessories(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Hair Accessories"


class BeautyAndPersonalCare(BaseOfferCategory):
    HAIR_ACCESSORIES = HairAccessories
    HAIRDRESSING_SUPPLIES = HairdressingSupplies
    BARBERSHOP = Barbershop
    SKINCARE = Skincare
    HAIR_CARE = HairCare
    HAIR_REMOVAL = HairRemoval
    PHARMACY = Pharmacy
    PERSONAL_HYGIENE = PersonalHygiene
    MANICURE_AND_PEDICURE = ManicureAndPedicure
    MAKEUP = Makeup
    PERFUMES = Perfumes
    BEAUTY_TREATMENTS = BeautyTreatments

    @classmethod
    def value(cls) -> str:
        return "Beauty and Personal Care"
