from typing import Self

from ._offer_categories import (
    VehicleAccessories,
    Agribusiness,
    FoodAndBeverage,
    AntiquesAndCollectibles,
    ArtSuppliesStationeryAndHaberdashery,
    Babies,
    BeautyAndPersonalCare,
    ToysAndHobbies,
    FootwearClothingAndBags,
    HomeFurnitureAndDecor
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
    FOOTWEAR_CLOTHING_AND_BAGS = FootwearClothingAndBags
    HOME_FURNITURE_AND_DECOR = HomeFurnitureAndDecor

    def __new__(cls) -> Self:
        raise RuntimeError("This class cannot be instanciated")
