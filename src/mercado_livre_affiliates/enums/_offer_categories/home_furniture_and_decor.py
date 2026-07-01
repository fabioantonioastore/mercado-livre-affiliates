from .base import BaseOfferCategory


class HomeTextilesAndDecor(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Home Textiles and Decor"


class HomeSecurity(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Home Security"


class HomeOrganization(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Home Organization"


class HomeFurniture(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Home Furniture"


class GardenAndOutdoors(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Garden and Outdoors"


class ResidentialLighting(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Residential Lighting"


class OrnamentsAndHomeDecor(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Ornaments and Home Decor"


class HomeCareAndLaundry(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Home Care and Laundry"


class Kitchen(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Kitchen"


class BedsMattressesAndAccessories(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Beds, Mattresses, and Accessories"


class Restrooms(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Restrooms"


class HomeFurnitureAndDecor(BaseOfferCategory):
    RESTROOMS = Restrooms
    BEDS_MATTRESSES_AND_ACCESSORIES = BedsMattressesAndAccessories
    KITCHEN = Kitchen
    HOME_CARE_AND_LAUNDRY = HomeCareAndLaundry
    ORNAMENTS_AND_HOME_DECOR = OrnamentsAndHomeDecor
    RESIDENTIAL_LIGHTING = ResidentialLighting
    GARDEN_AND_OUTDOORS = GardenAndOutdoors
    HOME_FURNITURE = HomeFurniture
    HOME_ORGANIZATION = HomeOrganization
    HOME_SECURITY = HomeSecurity
    HOME_TEXTILES_AND_DECOR = HomeTextilesAndDecor

    @classmethod
    def value(cls) -> str:
        return "Home, Furniture And Decor"
