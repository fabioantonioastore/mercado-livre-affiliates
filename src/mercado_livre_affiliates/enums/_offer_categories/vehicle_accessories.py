from .base import BaseOfferCategory


class Tuning(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Tuning"


class CarAudio(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Car Audio"


class VehicleSafety(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Vehicle Safety"


class Wheels(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Wheels"


class TiresAndAccessories(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Tires and Accessories"


class MotorcycleAndATVParts(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Motorcycle and ATV Parts"


class HeavyDutyParts(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Heavy-Duty Parts"


class CarAndPickupTruckParts(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Car and Pickup Truck Parts"


class MarineParts(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Marine Parts"


class Performance(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Performance"


class GPSNavigatorsForVehicles(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "GPS Navigators for Vehicles"


class LubricantsAndFluids(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Lubricants and Fluids"


class AutomotiveCleaning(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Automotive Cleaning"


class VehicleTools(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Vehicle Tools"


class HeavyDutyAccessories(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Heavy-Duty Accessories"


class MarineAccessories(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Marine Accessories"


class MotorcycleAndATVAccessories(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Motorcycle and ATV Accessories"


class CarAndPickupTruckAccessories(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Car and Pickup Truck Accessories"


class VehicleAccessories(BaseOfferCategory):
    CAR_AND_PICKUP_TRUCK_ACCESSORIES = CarAndPickupTruckAccessories
    MOTORCYCLE_AND_ATV_ACCESSORIES = MotorcycleAndATVAccessories
    MARINE_ACCESSORIES = MarineAccessories
    HEAVY_DUTY_ACCESSORIES = HeavyDutyAccessories
    VEHICLE_TOOLS = VehicleTools
    AUTOMOTIVE_CLEANING = AutomotiveCleaning
    LUBRICANTS_AND_FLUIDS = LubricantsAndFluids
    GPS_NAVIGATORS_FOR_VEHICLES = GPSNavigatorsForVehicles
    PERFORMANCE = Performance
    MARINE_PARTS = MarineParts
    CAR_AND_PICKUP_TRUCK_PARTS = CarAndPickupTruckParts
    HEAVY_DUTY_PARTS = HeavyDutyParts
    MOTORCYCLE_AND_ATV_PARTS = MotorcycleAndATVParts
    TIRES_AND_ACCESSORIES = TiresAndAccessories
    WHEELS = Wheels
    VEHICLE_SAFETY = VehicleSafety
    CAR_AUDIO = CarAudio
    TUNING = Tuning

    @classmethod
    def value(cls) -> str:
        return "Vehicle Accessories"
