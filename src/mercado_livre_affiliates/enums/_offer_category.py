from typing import Self

from ._offer_categories import Games, AntiquesAndCollectibles, VehicleAccessories


class OfferCategory:
    vehicle_accessories = VehicleAccessories
    antiques_and_collectibles = AntiquesAndCollectibles
    games = Games

    def __new__(cls) -> Self:
        raise RuntimeError("This class cannot be instanciated")
