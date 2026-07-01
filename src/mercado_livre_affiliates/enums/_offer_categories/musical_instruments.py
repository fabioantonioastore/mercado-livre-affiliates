from .base import BaseOfferCategory


class PianosAndKeyboards(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Pianos and Keyboards"


class PedalsAndAccessories(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Pedals and Accessories"


class SheetMusicAndLyrics(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Sheet Music and Lyrics"


class MicrophonesAndAmplifiers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Microphones and Amplifiers"


class Metronomes(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Metronomes"


class WindInstruments(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Wind Instruments"


class StringInstruments(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "String Instruments"


class RecordingStudio(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Recording Studio"


class DJEquipment(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "DJ Equipment"


class Speakers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Speakers"


class DrumsAndPercussion(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Drums and Percussion"


class MusicalInstruments(BaseOfferCategory):
    DRUMS_AND_PERCUSSION = DrumsAndPercussion
    SPEAKERS = Speakers
    DJ_EQUIPMENT = DJEquipment
    RECORDING_STUDIO = RecordingStudio
    STRING_INSTRUMENTS = StringInstruments
    WIND_INSTRUMENTS = WindInstruments
    METRONOMES = Metronomes
    MICROPHONES_AND_AMPLIFIERS = MicrophonesAndAmplifiers
    SHEET_MUSIC_AND_LYRICS = SheetMusicAndLyrics
    PEDALS_AND_ACCESSORIES = PedalsAndAccessories
    PIANOS_AND_KEYBOARDS = PianosAndKeyboards

    @classmethod
    def value(cls) -> str:
        return "Musical Instruments"
