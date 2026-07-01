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
    HomeFurnitureAndDecor,
    CellPhonesAndTelephones,
    Construction,
    CamerasAndAccessories,
    HomeAppliances,
    ElectronicsAudioAndVideo,
    SportsAndFitness,
    Tools,
    PartiesAndPartyFavors,
    Games,
    IndustryAndCommerce,
    Computing,
    MusicalInstruments,
    JewelryAndWatches,
    BooksMagazinesAndComics,
    MoreCategories,
    PetShop,
    Health
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
    CELL_PHONES_AND_TELEPHONES = CellPhonesAndTelephones
    CONSTRUCTION = Construction
    CAMERAS_AND_ACCESSORIES = CamerasAndAccessories
    HOME_APPLIANCES = HomeAppliances
    ELECTRONICS_AUDIO_AND_VIDEO = ElectronicsAudioAndVideo
    SPORTS_AND_FITNESS = SportsAndFitness
    TOOLS = Tools
    PARTIES_AND_PARTY_FAVORS = PartiesAndPartyFavors
    GAMES = Games
    INDUSTRY_AND_COMMERCE = IndustryAndCommerce
    COMPUTING = Computing
    MUSICAL_INSTRUMENTS = MusicalInstruments
    JEWELRY_AND_WATCHES = JewelryAndWatches
    BOOKS_MAGAZINES_AND_COMICS = BooksMagazinesAndComics
    MORE_CATEGORIES = MoreCategories
    PET_SHOP = PetShop
    HEALTH = Health

    def __new__(cls) -> Self:
        raise RuntimeError("This class cannot be instanciated")
