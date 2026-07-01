from .base import BaseOfferCategory
from .common import Others


class AlbumsAndStickers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Albums and Stickers"


class ToyVehicles(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Toy Vehicles"


class PlushToys(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Plush Toys"


class MiniVehiclesAndBicycles(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Mini Vehicles and Bicycles"


class TablesAndChairs(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Tables and Chairs"


class ToyLaunchers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Toy Launchers"


class BoardAndCardGames(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Board and Card Games"


class ParlorGames(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Parlor Games"


class MusicalInstruments(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Musical Instruments"


class Hobbies(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Hobbies"


class HandPuppetsAndMarionettes(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Hand Puppets and Marionettes"


class PlayhousesAndPlayTents(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Playhouses and Play Tents"


class BabyToys(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Baby Toys"


class BeachAndPoolToys(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Beach and Pool Toys"


class BuildingToys(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Building Toys"


class PretendPlayToys(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Pretend Play Toys"


class ElectronicToys(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Electronic Toys"


class Dolls(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Dolls"


class ArtsAndActivities(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Arts and Activities"


class OutdoorsAndPlayground(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Outdoors and Playground"


class AntiStressAndIngenuity(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Anti-stress and Ingenuity"


class ToysAndHobbies(BaseOfferCategory):
    ANTI_STRESS_AND_INGENUITY = AntiStressAndIngenuity
    OUTDOORS_AND_PLAYGROUND = OutdoorsAndPlayground
    ARTS_AND_ACTIVITIES = ArtsAndActivities
    DOLLS = Dolls
    ELECTRONIC_TOYS = ElectronicToys
    PRETEND_PLAY_TOYS = PretendPlayToys
    BUILDING_TOYS = BuildingToys
    BEACH_AND_POOL_TOYS = BeachAndPoolToys
    BABY_TOYS = BabyToys
    PLAYHOUSES_AND_PLAY_TENTS = PlayhousesAndPlayTents
    HAND_PUPPETS_AND_MARIONETTES = HandPuppetsAndMarionettes
    HOBBIES = Hobbies
    MUSICAL_INSTRUMENTS = MusicalInstruments
    PARLOR_GAMES = ParlorGames
    BOARD_AND_CARD_GAMES = BoardAndCardGames
    TOY_LAUNCHERS = ToyLaunchers
    TABLES_AND_CHAIRS = TablesAndChairs
    MINI_VEHICLES_AND_BICYCLES = MiniVehiclesAndBicycles
    OTHERS = Others
    PLUSH_TOYS = PlushToys
    TOY_VEHICLES = ToyVehicles
    ALBUMS_AND_STICKERS = AlbumsAndStickers

    @classmethod
    def value(cls) -> str:
        return "Toys and Hobbies"
