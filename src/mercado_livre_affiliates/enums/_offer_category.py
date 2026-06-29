from typing import Self

from ._offer_categories import (
    VehicleAccessories,
    Agribusiness,
    FoodAndBeverage,
    AntiquesAndCollectibles,
    ArtSuppliesStationeryAndHaberdashery,
    Babies,
    BeautyAndPersonalCare,
    ToysAndHobbies
)


class OfferCategory:
    VEHICLE_ACCESSORIES = VehicleAccessories
    AGRIBUSINESS = Agribusiness
    FOOD_AND_BEVERAGE = FoodAndBeverage
    ANTIQUES_AND_COLLECTIBLES = AntiquesAndCollectibles
    ART_SUPPLIES_STATIONERY_AND_HABERDASHERY = ArtSuppliesStationeryAndHaberdashery
    BABIES = Babies
    BEAUTY_AND_PERSONAL_CARE = BeautyAndPersonalCare
    TOYS_AND_HOBBIES = ToysAndHobbies

    def __new__(cls) -> Self:
        raise RuntimeError("This class cannot be instanciated")
