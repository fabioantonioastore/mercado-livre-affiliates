from .base import BaseOfferCategory


class Microphones(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Microphones"


class AudioAndVideoForGaming(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Audio and Video for Gaming"


class GamepadsAndJoysticks(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Gamepads and Joysticks"


class Consoles(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Consoles"


class VRHeadset(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "VR Headset"


class Headphones(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Headphones"


class ControllersAndJoysticks(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Controllers and Joysticks"


class GamingChairs(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Gaming Chairs"


class PCGamingAccessories(BaseOfferCategory):
    gaming_chairs = GamingChairs
    controllers_and_joysticks = ControllersAndJoysticks
    headphones = Headphones
    microphones = Microphones
    vr_headset = VRHeadset

    @classmethod
    def value(cls) -> str:
        return "PC Gaming Accessories"


class MemoryCards(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Memory Cards"


class PlayStation2(BaseOfferCategory):
    memory_cards = MemoryCards
    microphones = Microphones

    @classmethod
    def value(cls) -> str:
        return "PlayStation 2"


class ControllerCases(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Controller Cases"


class ControllerChargers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Controller Chargers"


class PlayStation5(BaseOfferCategory):
    controller_cases = ControllerCases
    gamepads_and_joysticks = GamepadsAndJoysticks
    audio_and_video_for_gaming = AudioAndVideoForGaming
    controller_charges = ControllerChargers

    @classmethod
    def value(cls) -> str:
        return "PlayStation 5"


class BasesAndSupports(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Bases and Supports"


class PlayStation4(BaseOfferCategory):
    bases_and_supports = BasesAndSupports
    gamepads_and_joysticks = GamepadsAndJoysticks
    audio_and_video_for_gaming = AudioAndVideoForGaming

    @classmethod
    def value(cls) -> str:
        return "PlayStation 4"


class PlayStation3(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "PlayStation 3"


class ForPlayStation(BaseOfferCategory):
    playstation_3 = PlayStation3
    playstation_4 = PlayStation4
    playstation_5 = PlayStation5

    @classmethod
    def value(cls) -> str:
        return "For PlayStation"


class CasesAndSleeves(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Cases and Sleeves"


class NintendoSwitch(BaseOfferCategory):
    cases_and_sleeves = CasesAndSleeves
    gamepads_and_joysticks = GamepadsAndJoysticks

    @classmethod
    def value(cls) -> str:
        return "Nintendo Switch"


class Nintendo64(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Nintendo 64"


class ForNintendo(BaseOfferCategory):
    nintendo_64 = Nintendo64
    nintendo_switch = NintendoSwitch

    @classmethod
    def value(cls) -> str:
        return "For Nintendo"


class ConsoleAccessories(BaseOfferCategory):
    for_nintendo = ForNintendo
    for_playstation = ForPlayStation
    playstation_2 = PlayStation2

    @classmethod
    def value(cls) -> str:
        return "Console Accessories"


class ForXbox(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "For Xbox"


class ConsoleParts(BaseOfferCategory):
    for_playstation = ForPlayStation
    for_xbox = ForXbox

    @classmethod
    def value(cls) -> str:
        return "Console Parts"


class Games(BaseOfferCategory):
    console_accessories = ConsoleAccessories
    pc_gaming_accessories = PCGamingAccessories
    consoles = Consoles
    console_parts = ConsoleParts

    @classmethod
    def value(cls) -> str:
        return "Games"
