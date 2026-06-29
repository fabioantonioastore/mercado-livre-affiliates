from .base import BaseOfferCategory


class GroceryStore(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Grocery Store"


class Kefir(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Kefir"


class Fresh(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Fresh"


class PreparedFood(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Prepared Food"


class Beverages(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Beverages"


class FoodAndBeverage(BaseOfferCategory):
    BEVERAGES = Beverages
    PREPARED_FOOD = PreparedFood
    FRESH = Fresh
    KEFIR = Kefir
    GROCERY_STORE = GroceryStore

    @classmethod
    def value(cls) -> str:
        return "Food and Beverage"
