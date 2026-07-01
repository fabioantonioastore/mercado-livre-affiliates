from .base import BaseOfferCategory


class AlbumsAndPhotoFrames(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Albums and Photo Frames"


class LensesAndFilters(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Lenses and Filters"


class OpticalInstruments(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Optical Instruments"


class Camcorders(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Camcorders"


class DronesAndAccessories(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Drones and Accessories"


class Cameras(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Cameras"


class CameraAccessories(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Camera Accessories"


class CamerasAndAccessories(BaseOfferCategory):
    CAMERA_ACCESSORIES = CameraAccessories
    CAMERAS = Cameras
    DRONES_AND_ACCESSORIES = DronesAndAccessories
    CAMCORDERS = Camcorders
    OPTICAL_INSTRUMENTS = OpticalInstruments
    LENSES_AND_FILTERS = LensesAndFilters
    ALBUMS_AND_PHOTO_FRAMES = AlbumsAndPhotoFrames

    @classmethod
    def value(cls) -> str:
        return "Cameras and Accessories"
    