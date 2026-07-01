from .base import BaseOfferCategory


class Rodents(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Rodents"


class PetFoodContainer(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Pet Food Container"


class Fish(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Fish"


class PetLeashes(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Pet Leashes"


class Cats(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Cats"


class Dogs(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Dogs"


class Horses(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Horses"


class BirdsAndAccessories(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Birds and Accessories"


class PetShop(BaseOfferCategory):
    BIRDS_AND_ACCESSORIES = BirdsAndAccessories
    HORSES = Horses
    DOGS = Dogs
    CATS = Cats
    PET_LEASHES = PetLeashes
    FISH = Fish
    PET_FOOD_CONTAINER = PetFoodContainer
    RODENTS = Rodents

    @classmethod
    def value(cls) -> str:
        return "Pet Shop"
    