from .base import BaseOfferCategory


class VideoGames(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Video Games"


class ConsoleParts(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Console Parts"


class Consoles(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Consoles"


class PCGamingAccessories(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "PC Gaming Accessories"


class ConsoleAccessories(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Console Accessories"


class Games(BaseOfferCategory):
    CONSOLE_ACCESSORIES = ConsoleAccessories
    PC_GAMING_ACCESSORIES = PCGamingAccessories
    CONSOLES = Consoles
    CONSOLE_PARTS = ConsoleParts
    VIDEO_GAMES = VideoGames

    @classmethod
    def value(cls) -> str:
        return "Games"
