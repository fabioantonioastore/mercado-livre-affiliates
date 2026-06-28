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
    car_and_pickup_truck_accessories = CarAndPickupTruckAccessories
    motorcycle_and_atv_accessories = MotorcycleAndATVAccessories
    marine_accessories = MarineAccessories
    heavy_duty_accessories = HeavyDutyAccessories
    vehicle_tools = VehicleTools
    automotive_cleaning = AutomotiveCleaning
    lubricants_and_fluids = LubricantsAndFluids
    gps_navigators_for_vehicles = GPSNavigatorsForVehicles
    performance = Performance
    marine_parts = MarineParts
    car_and_pickup_truck_parts = CarAndPickupTruckParts
    heavy_duty_parts = HeavyDutyParts
    motorcycle_and_atv_parts = MotorcycleAndATVParts
    tires_and_accessories = TiresAndAccessories
    wheels = Wheels
    vehicle_safety = VehicleSafety
    car_audio = CarAudio
    tuning = Tuning

    @classmethod
    def value(cls) -> str:
        return "Vehicle Accessories"