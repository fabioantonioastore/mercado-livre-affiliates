from .base import BaseOfferCategory
from .common import Others


class PartyFavorsForParties(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Party Favors for Parties"


class PartyFavors(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Party Favors"


class CostumesAndCosplay(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Costumes and Cosplay"


class FoamStreamersAndConfetti(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Foam, Streamers, and Confetti"


class PartyEquipment(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Party Equipment"


class PartyDisposables(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Party Disposables"


class PartyDecoration(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Party Decoration"


class PartySupplies(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Party Supplies"


class PartiesAndPartyFavors(BaseOfferCategory):
    PARTY_SUPPLIES = PartySupplies
    PARTY_DECORATION = PartyDecoration
    PARTY_DISPOSABLES = PartyDisposables
    PARTY_EQUIPMENT = PartyEquipment
    FOAM_STREAMERS_AND_CONFETTI = FoamStreamersAndConfetti
    COSTUMES_AND_COSPLAY = CostumesAndCosplay
    PARTY_FAVORS = PartyFavors
    PARTY_FAVORS_FOR_PARTIES = PartyFavorsForParties
    OTHERS = Others

    @classmethod
    def value(cls) -> str:
        return "Parties and Party Favors"
