from .base import BaseOfferCategory


class VoIP(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "VoIP"


class SmartwatchesAndAccessories(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Smartwatches and Accessories"


class TwoWayRadios(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Two-Way Radios"


class CellPhoneParts(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Cell Phone Parts"


class MobilePhonesAndSmartphones(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Mobile Phones and Smartphones"


class MobilePhoneAccessories(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Mobile Phone Accessories"


class CellPhonesAndTelephones(BaseOfferCategory):
    MOBILE_PHONE_ACCESSORIES = MobilePhoneAccessories
    MOBILE_PHONE_AND_SMARTPHONES = MobilePhonesAndSmartphones
    CELL_PHONE_PARTS = CellPhoneParts
    TWO_WAY_RADIOS = TwoWayRadios
    SMARTWATCHES_AND_ACCESSORIES = SmartwatchesAndAccessories
    VOIP = VoIP

    @classmethod
    def value(cls) -> str:
        return "Cell Phones and Telephones"
