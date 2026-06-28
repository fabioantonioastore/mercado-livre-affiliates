from typing import Self

from ._offer_categories import VehicleAccessories


class OfferCategory:
    vehicle_accessories = VehicleAccessories

    def __new__(cls) -> Self:
        raise RuntimeError("This class cannot be instanciated")
