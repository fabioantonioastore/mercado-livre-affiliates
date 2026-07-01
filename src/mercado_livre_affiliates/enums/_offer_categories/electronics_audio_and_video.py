from .base import BaseOfferCategory


class Audio(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Audio"


class Televisions(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Televisions"


class ProjectorsAndScreens(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Projectors and Screens"


class BatteriesAndChargers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Batteries and Chargers"


class MediaStreaming(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Media Streaming"


class DronesAndAccessories(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Drones and Accessories"


class RemoteControls(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Remote Controls"


class ElectronicComponents(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Electronic Components"


class Cables(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Cables"


class DVDAndBluRayPlayers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "DVD and Blu-ray players"


class AudioAndVideoAccessories(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Audio and Video Accessories"


class TVAccessories(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "TV Accessories"


class ElectronicsAudioAndVideo(BaseOfferCategory):
    TV_ACCESSORIES = TVAccessories
    AUDIO_AND_VIDEO_ACCESSORIES = AudioAndVideoAccessories
    DVD_AND_BLU_RAY_PLAYERS = DVDAndBluRayPlayers
    CABLES = Cables
    ELECTRONIC_COMPONENTS = ElectronicComponents
    REMOTE_CONTROLS = RemoteControls
    DRONES_AND_ACCESSORIES = DronesAndAccessories
    MEDIA_STREAMING = MediaStreaming
    BATTERIES_AND_CHARGERS = BatteriesAndChargers
    PROJECTORS_AND_SCREENS = ProjectorsAndScreens
    TELEVISIONS = Televisions
    AUDIO = Audio

    @classmethod
    def value(cls) -> str:
        return "Electronics, Audio and Video"
