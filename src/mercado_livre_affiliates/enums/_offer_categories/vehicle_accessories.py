from .base import BaseOfferCategory
from .commom import Others


class Batteries(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Batteries"


class Horns(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Horns"


class Lighting(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Lighting"


class PortableChargers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Portable Chargers"


class SeatCovers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Seat Covers"


class SeatBeltPads(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Seat Belt Pads"


class InteriorTuningFootpegs(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Footpegs"


class InteriorTuning(BaseOfferCategory):
    footpegs = InteriorTuningFootpegs
    seat_belt_pads = SeatBeltPads

    @classmethod
    def value(cls) -> str:
        return "Interior Tuning"


class ExteriorTuning(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Exterior Tuning"


class SheetMetalPaints(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Sheet Metal Paints"


class Paints(BaseOfferCategory):
    others = Others
    sheet_metal_paints = SheetMetalPaints

    @classmethod
    def value(cls) -> str:
        return "Paints"


class LEDBulbs(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "LED Bulbs"


class XenonBulbs(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Xenon bulbs"


class LightBulbs(BaseOfferCategory):
    xenon_bulbs = XenonBulbs
    led_bulbs = LEDBulbs

    @classmethod
    def value(cls) -> str:
        return "Light bulbs"


class LightingTailLights(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Tail Lights"


class LEDBars(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "LED bars"


class AngelEyes(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Angel Eyes"


class TuningLighting(BaseOfferCategory):
    angel_eyes = AngelEyes
    led_bars = LEDBars
    tail_lights = LightingTailLights
    light_bulbs = LightBulbs
    others = Others

    @classmethod
    def value(cls) -> str:
        return "Lighting"


class ChromePlatedParts(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Chrome-plated parts"


class Stickers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Stickers"


class CarWrapping(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Car Wrapping"


class MatteBlackDecals(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Matte Black Decals"


class DecalsAndStickers(BaseOfferCategory):
    matte_black_decals = MatteBlackDecals
    car_wrapping = CarWrapping
    stickers = Stickers

    @classmethod
    def value(cls) -> str:
        return "Decals and Stickers"


class Tuning(BaseOfferCategory):
    decals_and_stickers = DecalsAndStickers
    chrome_plated_parts = ChromePlatedParts
    tuning_lighting = TuningLighting
    paints = Paints
    exterior_tuning = ExteriorTuning
    interior_tuning = InteriorTuning

    @classmethod
    def value(cls) -> str:
        return "Tuning"


class Screenless(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Screenless"


class WithScreen(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "With Screen"


class Stereos(BaseOfferCategory):
    with_screen = WithScreen
    screenless = Screenless

    @classmethod
    def value(cls) -> str:
        return "Stereos"


class FMTransmitters(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "FM Transmitters"


class RadioWiringHarnesses(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Radio Wiring Harnesses"


class SiresAccessories(BaseOfferCategory):
    radio_wiring_harnesses = RadioWiringHarnesses
    fm_transmitters = FMTransmitters

    @classmethod
    def value(cls) -> str:
        return "Accessories"


class Sires(BaseOfferCategory):
    accessories = SiresAccessories
    stereos = Stereos

    @classmethod
    def value(cls) -> str:
        return "Sires"


class AmplifierModules(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Amplifier Modules"


class Interfaces(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Interfaces"


class Drivers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Drivers"


class CablesAndConnectors(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Cables and Connectors"


class Speakers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Speakers"


class CarAudio(BaseOfferCategory):
    speakers = Speakers
    cables_and_connectors = CablesAndConnectors
    drivers = Drivers
    interfaces = Interfaces
    amplifier_modules = AmplifierModules
    sires = Sires

    @classmethod
    def value(cls) -> str:
        return "Car Audio"


class VehicleSafetySteeringWheelLocks(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Steering Wheel Locks"


class VehicleSafetyLatchesAndElasticBands(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Latches and Elastic Bands"


class WheelNuts(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Wheel Nuts"


class Breathalyzers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Breathalyzers"


class ControllerShells(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Controller Shells"


class CarAlarms(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Car Alarms"


class AlarmsAndAccessories(BaseOfferCategory):
    car_alarms = CarAlarms
    controller_shells = ControllerShells

    @classmethod
    def value(cls) -> str:
        return "Alarms and Accessories"


class VehicleSafety(BaseOfferCategory):
    alarms_and_accessories = AlarmsAndAccessories
    breathalyzers = Breathalyzers
    wheel_nuts = WheelNuts
    latches_and_elastic_bands = VehicleSafetyLatchesAndElasticBands
    steering_wheel_locks = VehicleSafetySteeringWheelLocks

    @classmethod
    def value(cls) -> str:
        return "Vehicle Safety"


class MotorcycleWheels(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Motorcycle Wheels"


class TirePatchStickers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Tire Patch Stickers"


class Wheels(BaseOfferCategory):
    tire_patch_stickers = TirePatchStickers
    motorcycle_wheels = MotorcycleWheels

    @classmethod
    def value(cls) -> str:
        return "Wheels"


class MotorcycleTires(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Motorcycle Tires"


class BicycleTires(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Bicycle Tires"


class CarAndLightTruckTires(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Car and Light Truck Tires"


class TiresAndAccessories(BaseOfferCategory):
    car_and_light_truck_tires = CarAndLightTruckTires
    bicycle_tires = BicycleTires
    motorcycle_tires = MotorcycleTires

    @classmethod
    def value(cls) -> str:
        return "Tires and Accessories"


class GearShiftLever(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Gear Shift Lever"


class DriveKit(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Drive Kit"


class Gears(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Gears"


class ClutchDisc(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Clutch Disc"


class ClutchBell(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Clutch Bell"


class TransmissionClutches(BaseOfferCategory):
    clutch_bell = ClutchBell
    clutch_disc = ClutchDisc

    @classmethod
    def value(cls) -> str:
        return "Clutches"


class GearSelectorShafts(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Gear Selector Shafts"


class Crowns(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Crowns"


class Gearboxes(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Gearboxes"


class MotorcycleAndATVPartsTransmission(BaseOfferCategory):
    gearboxes = Gearboxes
    crowns = Crowns
    gear_selector_shafts = GearSelectorShafts
    clutches = TransmissionClutches
    gears = Gears
    drive_kit = DriveKit
    gear_shift_lever = GearShiftLever

    @classmethod
    def value(cls) -> str:
        return "Transmission"


class Stators(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Stators"


class TransmissionChains(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Transmission Chains"


class Cylinders(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Cylinders"


class Carburetors(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Carburetors"


class MotorcycleAndATVPartsEngine(BaseOfferCategory):
    carburetors = Carburetors
    cylinders = Cylinders
    transmission_chains = TransmissionChains
    stators = Stators

    @classmethod
    def value(cls) -> str:
        return "Engine"


class TurnSignals(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Turn signals"


class Flashlights(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Flashlights"


class LightingHeadlights(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Headlights"


class MotorcycleAndATVPartsLighting(BaseOfferCategory):
    headlights = LightingHeadlights
    flashlights = Flashlights
    turn_signals = TurnSignals

    @classmethod
    def value(cls) -> str:
        return "Lighting"


class MotorcycleAndATVPartsIgnition(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Ignition"


class MotorcycleAndATVPartsFilters(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Filters"


class RearviewMirrors(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Rearview Mirrors"


class Silencers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Silencers"


class ExhaustSystemsAndMufflersExhaustSystems(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Exhaust Systems"


class ExhaustSystemsAndMufflers(BaseOfferCategory):
    exhaust_systems = ExhaustSystemsAndMufflersExhaustSystems
    silencers = Silencers

    @classmethod
    def value(cls) -> str:
        return "Exhaust Systems and Mufflers"


class TankLids(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Tank Lids"


class LicensePlateHolders(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "License Plate Holders"


class FenderBrackets(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Fender Brackets"


class RearWheelOilSeals(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Rear Wheel Oil Seals"


class SkidPlates(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Skid Plates"


class SideCovers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Side Covers"


class Fairing(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Fairing"


class MotorcyclePlastics(BaseOfferCategory):
    fairing = Fairing
    side_covers = SideCovers

    @classmethod
    def value(cls) -> str:
        return "Motorcycle Plastics"


class Footpegs(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Footpegs"


class Panels(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Panels"


class Grips(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Grips"


class HandlebarsAndComponents(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Handlebars and Components"


class ChassisBrakes(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Brakes"


class WheelAxle(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Wheel Axle"


class ChassisKeys(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Keys"


class ChassisSawhorses(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Sawhorses"


class ChassisCables(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Cables"


class ChassisShockAbsorbers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Shock absorbers"


class Chassis(BaseOfferCategory):
    shock_absorbers = ChassisShockAbsorbers
    cables = ChassisCables
    sawhorses = ChassisSawhorses
    keys = ChassisKeys
    wheel_axle = WheelAxle
    brakes = ChassisBrakes
    handlebars_and_components = HandlebarsAndComponents
    grips = Grips
    others = Others
    panels = Panels
    footpegs = Footpegs
    motorcycle_plastics = MotorcyclePlastics
    skid_plates = SkidPlates
    rear_wheel_oil_seals = RearWheelOilSeals
    fender_brackets = FenderBrackets
    license_plate_holders = LicensePlateHolders
    tank_lids = TankLids

    @classmethod
    def value(cls) -> str:
        return "Chassis"


class MotorcycleAndATVParts(BaseOfferCategory):
    batteries = Batteries
    chassis = Chassis
    exhaust_systems_and_mufflers = ExhaustSystemsAndMufflers
    rearview_mirrors = RearviewMirrors
    filters = MotorcycleAndATVPartsFilters
    ignition = MotorcycleAndATVPartsIgnition
    lighting = MotorcycleAndATVPartsLighting
    engine = MotorcycleAndATVPartsEngine
    transmission = MotorcycleAndATVPartsTransmission

    @classmethod
    def value(cls) -> str:
        return "Motorcycle and ATV Parts"


class RefrigerationSystems(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Refrigeration Systems"


class Pictures(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Pictures"


class WindshieldWiperBlades(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Windshield Wiper Blades"


class DoorCylinders(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Door Cylinders"


class HeavyDutyPartsHorns(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Horns"


class HeavyDutyPartsExteriorParts(BaseOfferCategory):
    horns = Horns
    door_cylinders = DoorCylinders
    windshield_wiper_blades = WindshieldWiperBlades

    @classmethod
    def value(cls) -> str:
        return "Exterior Parts"


class Doors(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Doors"


class CabPartsEmblems(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Emblems"


class CabPartsHinges(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Hinges"


class MultifunctionDisplays(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Multifunction Displays"


class CabParts(BaseOfferCategory):
    multifunction_displays = MultifunctionDisplays
    hinges = CabPartsHinges
    emblems = CabPartsEmblems
    doors = Doors

    @classmethod
    def value(cls) -> str:
        return "Cab Parts"


class Lenses(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Lenses"


class HeavyDutyPartsDrivingLights(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Driving Lights"


class HeavyDutyPartsFrontHeadlights(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Front Headlights"


class HeavyDutyPartsLighting(BaseOfferCategory):
    front_headlights = HeavyDutyPartsFrontHeadlights
    driving_lights = HeavyDutyPartsDrivingLights
    lenses = Lenses

    @classmethod
    def value(cls) -> str:
        return "Lighting"


class HeavyDutyPartsFilters(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Filters"


class HeavyDutyPartsLocksAndKeys(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Locks and Keys"


class HeavyDutyParts(BaseOfferCategory):
    locks_and_keys = HeavyDutyPartsLocksAndKeys
    filters = HeavyDutyPartsFilters
    lightning = HeavyDutyPartsLighting
    cab_parts = CabParts
    exterior_parts = HeavyDutyPartsExteriorParts
    pictures = Pictures
    refrigeration_systems = RefrigerationSystems

    @classmethod
    def value(cls) -> str:
        return "Heavy-Duty Parts"


class ManualTransmission(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Manual transmission"


class DifferentialCovers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Differential Covers"


class SelectorsAndCables(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Selectors and Cables"


class BearingsAndHalfShafts(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Bearings and Half-Shafts"


class FastenersAndHardware(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Fasteners and Hardware"


class ClutchMasterCylinders(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Clutch Master Cylinders"


class ClutchActuator(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Clutch Actuator"


class Clutches(BaseOfferCategory):
    clutch_actuator = ClutchActuator
    clutch_master_cylinders = ClutchMasterCylinders

    @classmethod
    def value(cls) -> str:
        return "Clutches"


class Gear(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Gear"


class TransmissionMount(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Transmission Mount"


class ForeignExchange(BaseOfferCategory):
    transmission_mount = TransmissionMount
    gear = Gear

    @classmethod
    def value(cls) -> str:
        return "Foreign Exchange"


class Transmission(BaseOfferCategory):
    foreign_exchange = ForeignExchange
    clutches = Clutches
    fasteners_and_hardware = FastenersAndHardware
    bearings_and_half_shafts = BearingsAndHalfShafts
    selectors_and_cables = SelectorsAndCables
    differential_covers = DifferentialCovers
    manual_transmission = ManualTransmission

    @classmethod
    def value(cls) -> str:
        return "Transmission"


class Bearings(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Bearings"


class AxleStubs(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Axle Stubs"


class HydraulicPumpParts(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Hydraulic Pump Parts"


class Springs(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Springs"


class TorsionBar(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Torsion Bar"


class SpringAndBars(BaseOfferCategory):
    torsion_bar = TorsionBar
    springs = Springs

    @classmethod
    def value(cls) -> str:
        return "Springs and Bars"


class SteeringKnuckles(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Steering Knuckles"


class TurnSignalSwitches(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Turn Signal Switches"


class WheelHub(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Wheel Hub"


class ShockAbsorberMount(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Shock Absorber Mount"


class CVJointBoot(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "CV Joint Boot"


class SteeringRacksAndParts(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Steering Racks and Parts"


class SuspensionBushings(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Suspension Bushings"


class Bushings(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Bushings"


class ControlArms(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Control Arms"


class PitmanArmsAndSuspension(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Pitman Arms and Suspension"


class SwingarmsSwingarms(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Swingarms"


class SuspensionControlArms(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Suspension Control Arms"


class Swingarms(BaseOfferCategory):
    suspension_control_arms = SuspensionControlArms
    swingarms = SwingarmsSwingarms

    @classmethod
    def value(cls) -> str:
        return "Swingarms"


class Doorstops(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Doorstops"


class SwayBarBushings(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Sway Bar Bushings"


class SwayBarLinks(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Sway bar links"


class StabilizerBars(BaseOfferCategory):
    sway_bar_links = SwayBarLinks
    sway_bar_bushings = SwayBarBushings

    @classmethod
    def value(cls) -> str:
        return "Stabilizer bars"


class AxialRods(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Axial Rods"


class ShockAbsorbers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Shock absorbers"


class SuspensionAndSteering(BaseOfferCategory):
    shock_absorbers = ShockAbsorbers
    axial_rods = AxialRods
    stabilizer_bars = StabilizerBars
    doorstops = Doorstops
    swingarms = Swingarms
    pitman_arms_and_suspension = PitmanArmsAndSuspension
    control_arms = ControlArms
    bushings = Bushings
    suspension_bushing = SuspensionBushings
    steering_racks_and_parts = SteeringRacksAndParts
    cv_joint_boot = CVJointBoot
    shcok_absorber_mount = ShockAbsorberMount
    wheel_hub = WheelHub
    turn_signal_switches = TurnSignalSwitches
    steering_knuckles = SteeringKnuckles
    spring_and_bars = SpringAndBars
    hydraulic_pump_parts = HydraulicPumpParts
    axle_stubs = AxleStubs
    bearings = Bearings

    @classmethod
    def value(cls) -> str:
        return "Suspension and Steering"


class ElectricalSystem(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Electrical System"


class Security(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Security"


class SteeringWheels(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Steering Wheels"


class Pedals(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Pedals"


class DoorPanels(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Door Panels"


class GearShiftKnob(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Gear Shift Knob"


class Lighters(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Lighters"


class Glass(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Glass"


class WithHazardLightsOn(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "With Hazard Lights On"


class OfLights(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Of Lights"


class CentralLockingButtons(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Central Locking Buttons"


class InteriorPartsSwitches(BaseOfferCategory):
    central_locking_buttons = CentralLockingButtons
    of_lights = OfLights
    with_hazard_lights_on = WithHazardLightsOn
    glass = Glass

    @classmethod
    def value(cls) -> str:
        return "Switches"


class InteriorRearviewMirrors(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Interior Rearview Mirrors"


class Consoles(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Consoles"


class GearShiftBoots(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Gear Shift Boots"


class Cables(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Cables"


class Armrests(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Armrests"


class InteriorParts(BaseOfferCategory):
    armrests = Armrests
    cables = Cables
    gear_shift_boots = GearShiftBoots
    consoles = Consoles
    interior_rearview_mirrors = InteriorRearviewMirrors
    switches = InteriorPartsSwitches
    lighters = Lighters
    gear_shift_knob = GearShiftKnob
    door_panels = DoorPanels
    pedals = Pedals
    steering_wheels = SteeringWheels

    @classmethod
    def value(cls) -> str:
        return "Interior Parts"


class TireValves(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Tire Valves"


class TPMSSensors(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "TPMS sensors"


class ExteriorPartsWheels(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Wheels"


class SideMirrors(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Side Mirrors"


class BrushesAndRefills(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Brushes and Refills"


class LinksAndTransmissions(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Links and Transmissions"


class WipersAndWashers(BaseOfferCategory):
    links_and_transmissions = LinksAndTransmissions
    brushes_and_refills = BrushesAndRefills

    @classmethod
    def value(cls) -> str:
        return "Wipers and Washers"


class Emblems(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Emblems"


class Erasers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Erasers"


class GasShockAbsorbers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Gas Shock Absorbers"


class ExteriorParts(BaseOfferCategory):
    gas_shock_absorbers = GasShockAbsorbers
    erasers = Erasers
    horns = Horns
    emblems = Emblems
    wipers_and_washers = WipersAndWashers
    side_mirrors = SideMirrors
    wheels = ExteriorPartsWheels
    tpms_sensors = TPMSSensors
    tire_valves = TireValves

    @classmethod
    def value(cls) -> str:
        return "Exterior Parts"


class Crankshaft(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Crankshaft"


class OilDipstick(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Oil Dipstick"


class TurbochargersAndSuperchargers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Turbochargers and Superchargers"


class AirTemperatureSensor(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Air Temperature Sensor"


class TemperatureSensor(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Temperature Sensor"


class EngineSensors(BaseOfferCategory):
    temperature_sensor = TemperatureSensor
    air_temperature_sensor = AirTemperatureSensor

    @classmethod
    def value(cls) -> str:
        return "Sensors"


class OilSensor(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Oil Sensor"


class OilSeals(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Oil seals"


class Refrigeration(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Refrigeration"


class ThermostaticValves(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Thermostatic Valves"


class RadiatorCap(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Radiator Cap"


class Reservoir(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Reservoir"


class OilRadiators(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Oil Radiators"


class WaterRadiators(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Water Radiators"


class Radiators(BaseOfferCategory):
    water_radiators = WaterRadiators
    oil_radiators = OilRadiators
    reservoir = Reservoir
    radiator_cap = RadiatorCap
    thermostatic_valves = ThermostaticValves

    @classmethod
    def value(cls) -> str:
        return "Radiators"


class IntakeHoses(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Intake Hoses"


class IntercoolerHose(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Intercooler Hose"


class BracketsAndHardware(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Brackets and Hardware"


class IntakeManifoldGaskets(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Intake Manifold Gaskets"


class Together(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Together"


class GasketsAndSeals(BaseOfferCategory):
    together = Together
    intake_manifold_gaskets = IntakeManifoldGaskets

    @classmethod
    def value(cls) -> str:
        return "Gaskets and Seals"


class GasketsSealsAndHardware(BaseOfferCategory):
    gaskets_and_seals = GasketsAndSeals
    brackets_and_hardware = BracketsAndHardware

    @classmethod
    def value(cls) -> str:
        return "Gaskets, Seals, and Hardware"


class ChainCovers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Chain Covers"


class TimingBeltKit(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Timing Belt Kit"


class TimingGear(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Timing Gear"


class TimingBelts(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Timing Belts"


class Distribution(BaseOfferCategory):
    timing_belts = TimingBelts
    timing_gear = TimingGear
    timing_belt_kit = TimingBeltKit
    chain_covers = ChainCovers

    @classmethod
    def value(cls) -> str:
        return "Distribution"


class EngineMounts(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Engine Mounts"


class PolyVTensioners(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Poly-V Tensioners"


class TensionerPulleys(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Tensioner Pulleys"


class TensionerKits(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Tensioner Kits"


class RollersAndTensioners(BaseOfferCategory):
    tensioner_kits = TensionerKits
    tensioner_pulleys = TensionerPulleys

    @classmethod
    def value(cls) -> str:
        return "Rollers and Tensioners"


class PolyVBelts(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Poly-V Belts"


class Belts(BaseOfferCategory):
    poly_v_belts = PolyVBelts
    rollers_and_tensioners = RollersAndTensioners
    poly_v_tensioners = PolyVTensioners

    @classmethod
    def value(cls) -> str:
        return "Belts"


class Valves(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Valves"


class LidsLids(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Lids"


class OilCap(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Oil Cap"


class CylinderBolts(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Cylinder Bolts"


class Lids(BaseOfferCategory):
    cylinder_bolts = CylinderBolts
    oil_cap = OilCap
    lids = LidsLids

    @classmethod
    def value(cls) -> str:
        return "Lids"


class Camshafts(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Camshafts"


class SwingStages(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Swing stages"


class EngineCylinderHeads(BaseOfferCategory):
    swing_stages = SwingStages
    camshafts = Camshafts

    @classmethod
    def value(cls) -> str:
        return "Engine Cylinder Heads"


class Tappets(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Tappets"


class EnginePistonRingSet(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Engine Piston Ring Set"


class ConnectingRods(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Connecting rods"


class EngineBlock(BaseOfferCategory):
    connecting_rods = ConnectingRods
    engine_piston_ring_set = EnginePistonRingSet
    tappets = Tappets

    @classmethod
    def value(cls) -> str:
        return "Engine Block"


class EngineComponents(BaseOfferCategory):
    engine_block = EngineBlock
    engine_cylinder_heads = EngineCylinderHeads
    lids = Lids
    valves = Valves

    @classmethod
    def value(cls) -> str:
        return "Engine Components"


class CarburetorsAndParts(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Carburetors and Parts"


class OilPumps(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Oil Pumps"


class VacuumPumps(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Vacuum Pumps"


class FuelPumps(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Fuel Pumps"


class Pumps(BaseOfferCategory):
    fuel_pumps = FuelPumps
    vacuum_pumps = VacuumPumps
    oil_pumps = OilPumps

    @classmethod
    def value(cls) -> str:
        return "Pumps"


class Engine(BaseOfferCategory):
    pumps = Pumps
    carburetors_and_parts = CarburetorsAndParts
    engine_components = EngineComponents
    belts = Belts
    engine_mounts = EngineMounts
    distribution = Distribution
    gaskets_seals_and_hardware = GasketsSealsAndHardware
    intercooler_hose = IntercoolerHose
    intake_hoses = IntakeHoses
    radiators = Radiators
    refrigeration = Refrigeration
    oil_seals = OilSeals
    oil_sensor = OilSensor
    sensors = EngineSensors
    turbochargers_and_superchargers = TurbochargersAndSuperchargers
    oil_dipstick = OilDipstick
    crankshaft = Crankshaft

    @classmethod
    def value(cls) -> str:
        return "Engine"


class LiftingSystems(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Lifting Systems"


class Windows(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Windows"


class WindowsAndSeals(BaseOfferCategory):
    windows = Windows
    lifting_systems = LiftingSystems

    @classmethod
    def value(cls) -> str:
        return "Windows and Seals"


class LambdaSensor(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Lambda sensor"


class RotationSensor(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Rotation Sensor"


class PositionSensor(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Position Sensor"


class TPSSensor(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "TPS sensor"


class Sensors(BaseOfferCategory):
    tps_sensor = TPSSensor
    position_sensor = PositionSensor
    rotation_sensor = RotationSensor

    @classmethod
    def value(cls) -> str:
        return "Sensors"


class Throttle(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Throttle"


class InjectionModule(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Injection Module"


class Injectors(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Injectors"


class FuelRail(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Fuel Rail"


class ThrottleBody(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Throttle Body"


class IdleAirControlValves(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Idle Air Control Valves"


class Injection(BaseOfferCategory):
    idle_air_control_valves = IdleAirControlValves
    throttle_body = ThrottleBody
    fuel_rail = FuelRail
    injectors = Injectors
    injection_module = InjectionModule
    throttle = Throttle
    sensors = Sensors
    lambda_sensor = LambdaSensor

    @classmethod
    def value(cls) -> str:
        return "Injection"


class LightBulbsAndLEDs(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Light Bulbs and LEDs"


class InteriorLights(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Interior Lights"


class ExteriorLights(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Exterior Lights"


class FrontHeadlights(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Front Headlights"


class FairyLights(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Fairy lights"


class ThreeBrakeLightSetup(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Three-brake-light setup"


class DrivingLights(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Driving Lights"


class TailLights(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Tail Lights"


class Headlights(BaseOfferCategory):
    tail_lights = TailLights
    driving_lights = DrivingLights
    three_brake_light_setup = ThreeBrakeLightSetup
    fairy_lights = FairyLights

    @classmethod
    def value(cls) -> str:
        return "Headlights"


class CarLighting(BaseOfferCategory):
    headlights = Headlights
    front_headlights = FrontHeadlights
    exterior_lights = ExteriorLights
    interior_lights = InteriorLights
    light_bulbs_and_leds = LightBulbsAndLEDs

    @classmethod
    def value(cls) -> str:
        return "Lighting"


class SparkPlugs(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Spark Plugs"


class GlowPlugs(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Glow Plugs"


class Candles(BaseOfferCategory):
    glow_plugs = GlowPlugs
    spark_plugs = SparkPlugs

    @classmethod
    def value(cls) -> str:
        return "Candles"


class DistributorsAndParts(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Distributors and Parts"


class StarterMotor(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Starter Motor"


class StarterDrive(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Starter Drive"


class StartingComponents(BaseOfferCategory):
    starter_drive = StarterDrive
    starter_motor = StarterMotor

    @classmethod
    def value(cls) -> str:
        return "Starting Components"


class IgnitionCoilBootsAndWires(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Ignition Coil Boots and Wires"


class IgnitionCoil(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Ignition coil"


class AlternatorsAndDynamos(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Alternators and Dynamos"


class Ignition(BaseOfferCategory):
    alternators_and_dynamos = AlternatorsAndDynamos
    ignition_coil = IgnitionCoil
    ignition_coil_boots_and_wires = IgnitionCoilBootsAndWires
    starting_components = StartingComponents
    distributors_and_parts = DistributorsAndParts
    others = Others
    candles = Candles

    @classmethod
    def value(cls) -> str:
        return "Ignition"


class BrakePads(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Brake Pads"


class BrakeDisc(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Brake Disc"


class BrakeCylinder(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Brake Cylinder"


class CablesConnectorsAndWires(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Cables, Connectors, and Wires"


class Brakes(BaseOfferCategory):
    cables_connectors_and_wires = CablesConnectorsAndWires
    brake_cylinder = BrakeCylinder
    brake_disck = BrakeDisc
    brake_pads = BrakePads

    @classmethod
    def value(cls) -> str:
        return "Brakes"


class FilterKits(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Filter Kits"


class OilFilters(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Oil Filters"


class CabinFilters(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Cabin Filters"


class AirFilters(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Air Filters"


class Filters(BaseOfferCategory):
    air_filters = AirFilters
    cabin_filters = CabinFilters
    oil_filters = OilFilters
    filter_kits = FilterKits

    @classmethod
    def value(cls) -> str:
        return "Filters"


class ForTrunksAndTailgates(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "for Trunks and Tailgates"


class DoorLocks(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Door Locks"


class HoodLatch(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Hood Latch"


class LocksAndKeys(BaseOfferCategory):
    hood_latch = HoodLatch
    door_locks = DoorLocks
    for_trunks_and_tailgates = ForTrunksAndTailgates

    @classmethod
    def value(cls) -> str:
        return "Locks and Keys"


class ExhaustSystems(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Exhaust Systems"


class ElectricCoolingFans(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Electric cooling fans"


class Heating(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Heating"


class Buttons(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Buttons"


class CompressorGaskets(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Compressor Gaskets"


class Switches(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Switches"


class Compressors(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Compressors"


class AirConditioning(BaseOfferCategory):
    compressors = Compressors
    electric_cooling_fans = ElectricCoolingFans
    switches = Switches
    compressor_gaskets = CompressorGaskets
    others = Others

    @classmethod
    def value(cls) -> str:
        return "Air conditioning"


class HVACClimateControl(BaseOfferCategory):
    air_conditioning = AirConditioning
    buttons = Buttons
    heating = Heating

    @classmethod
    def value(cls) -> str:
        return "HVAC / Climate Control"


class SpareTireMounts(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Spare Tire Mounts"


class DoorSills(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Door sills"


class Bumpers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Bumpers"


class DoorHandles(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Door Handles"


class CarDoorHandles(BaseOfferCategory):
    door_handles = DoorHandles
    others = Others

    @classmethod
    def value(cls) -> str:
        return "Car Door Handles"


class Clamps(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Clamps"


class BumperGrilles(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Bumper Grilles"


class SideViewMirrors(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Side-View Mirrors"


class SideMirrorCovers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Side Mirror Covers"


class RearviewMirrorsAndLenses(BaseOfferCategory):
    side_mirror_covers = SideMirrorCovers
    side_view_mirrors = SideViewMirrors

    @classmethod
    def value(cls) -> str:
        return "Rearview Mirrors and Lenses"


class DoorHinges(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Door Hinges"


class Hinges(BaseOfferCategory):
    door_hinges = DoorHinges
    others = Others

    @classmethod
    def value(cls) -> str:
        return "Hinges"


class Bodywork(BaseOfferCategory):
    hinges = Hinges
    rearview_mirrors_and_lenses = RearviewMirrorsAndLenses
    bumper_grilles = BumperGrilles
    clamps = Clamps
    car_door_handles = CarDoorHandles
    bumpers = Bumpers
    door_sills = DoorSills
    spare_tire_mounts = SpareTireMounts

    @classmethod
    def value(cls) -> str:
        return "Bodywork"


class CarAndPickupTruckParts(BaseOfferCategory):
    batteries = Batteries
    bodywork = Bodywork
    hvac_climate_control = HVACClimateControl
    eletric_cooling_fans = ElectricCoolingFans
    exhaust_systems = ExhaustSystems
    locks_and_keys = LocksAndKeys
    filters = Filters
    brakes = Brakes
    ignition = Ignition
    lighting = CarLighting
    injection = Injection
    windows_and_seals = WindowsAndSeals
    engine = Engine
    exterior_parts = ExteriorParts
    interior_parts = InteriorParts
    security = Security
    electrical_system = ElectricalSystem
    suspension_and_steering = SuspensionAndSteering
    trasnmission = Transmission

    @classmethod
    def value(cls) -> str:
        return "Car and Pickup Truck Parts"


class Performance(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Performance"


class GPSDevices(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "GPS devices"


class Accessories(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Accessories"


class GPSNavigatorsForVehicles(BaseOfferCategory):
    accessories = Accessories
    gps_devices = GPSDevices

    @classmethod
    def value(cls) -> str:
        return "GPS Navigators for Vehicles"


class Motorcycles(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Motorcycles"


class Liquids(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Liquids"


class TransmissionOils(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Transmission Oils"


class ForGearboxes(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "For Gearboxes"


class Oils(BaseOfferCategory):
    for_gearboxes = ForGearboxes
    transmission_oils = TransmissionOils

    @classmethod
    def value(cls) -> str:
        return "Oils"


class Additives(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Additives"


class CarsAndPickupTrucks(BaseOfferCategory):
    additives = Additives
    oils = Oils

    @classmethod
    def value(cls) -> str:
        return "Cars and Pickup Trucks"


class LubricantsAndFluids(BaseOfferCategory):
    cars_and_pickup_trucks = CarsAndPickupTrucks
    liquids = Liquids
    motorcycles = Motorcycles

    @classmethod
    def value(cls) -> str:
        return "Lubricants and Fluids"


class Treatments(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Treatments"


class CarShampoo(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Car Shampoo"


class Polisher(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Polisher"


class Cloths(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Cloths"


class Fragrances(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Fragrances"


class Degreasers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Degreasers"


class Waxes(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Waxes"


class VacuumCleaners(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Vacuum Cleaners"


class AntiCorrosives(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Anti-corrosives"


class AutomotiveCleaning(BaseOfferCategory):
    anti_corrosives = AntiCorrosives
    vacuum_cleaners = VacuumCleaners
    waxes = Waxes
    desegreasers = Degreasers
    fragrances = Fragrances
    others = Others
    cloths = Cloths
    polisher = Polisher
    car_shampoo = CarShampoo
    treatments = Treatments

    @classmethod
    def value(cls) -> str:
        return "Automotive Cleaning"


class SocketsAndAccessories(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Sockets and Accessories"


class Measurement(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Measurement"


class Inflators(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Inflators"


class BatteryTesters(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Battery Testers"


class BatteryChargers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Battery Chargers"


class BatteryPoweredTools(BaseOfferCategory):
    battery_charges = BatteryChargers
    battery_testers = BatteryTesters

    @classmethod
    def value(cls) -> str:
        return "Battery-Powered Tools"


class PulleyPullers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Pulley Pullers"


class IScan(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "I scan"


class Monkeys(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Monkeys"


class Sawhorses(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Sawhorses"


class Elevation(BaseOfferCategory):
    sawhorser = Sawhorses
    monkeys = Monkeys

    @classmethod
    def value(cls) -> str:
        return "Elevation"


class Sailing(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Sailing"


class Adjustable(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Adjustable"


class Keys(BaseOfferCategory):
    adjustable = Adjustable
    sailing = Sailing

    @classmethod
    def value(cls) -> str:
        return "Keys"


class VehicleTools(BaseOfferCategory):
    keys = Keys
    elevation = Elevation
    i_scan = IScan
    pulley_pullers = PulleyPullers
    battery_powered_tools = BatteryPoweredTools
    inflators = Inflators
    measurement = Measurement
    others = Others
    sockets_and_accessories = SocketsAndAccessories

    @classmethod
    def value(cls) -> str:
        return "Vehicle Tools"


class SteeringWheelsAndAccessories(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Steering Wheels and Accessories"


class Coasters(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Coasters"


class Refrigerators(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Refrigerators"


class RoofConsoles(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Roof Consoles"


class InteriorAccessories(BaseOfferCategory):
    roof_consoles = RoofConsoles
    refrigerators = Refrigerators
    coasters = Coasters
    steering_wheels_and_accessories = SteeringWheelsAndAccessories

    @classmethod
    def value(cls) -> str:
        return "Interior Accessories"


class Tarps(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Tarps"


class ReflectiveStrips(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Reflective Strips"


class TowStraps(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Tow Straps"


class OutdoorAccessories(BaseOfferCategory):
    portable_charges = PortableChargers
    tow_straps = TowStraps
    reflective_strips = ReflectiveStrips
    tarps = Tarps

    @classmethod
    def value(cls) -> str:
        return "Outdoor Accessories"


class HeavyDutyAccessories(BaseOfferCategory):
    outdoor_accessories = OutdoorAccessories
    interior_accessories = InteriorAccessories
    others = Others

    @classmethod
    def value(cls) -> str:
        return "Heavy-Duty Accessories"


class NavigationSystems(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Navigation Systems"


class SafetyAndRescue(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Safety and Rescue"


class ConnectivityAntennas(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Connectivity Antennas"


class MarineAccessories(BaseOfferCategory):
    connectivity_antennas = ConnectivityAntennas
    lighting = Lighting
    safety_and_rescue = SafetyAndRescue
    navigation_systems = NavigationSystems

    @classmethod
    def value(cls) -> str:
        return "Marine Accessories"


class HelmetVisors(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Helmet Visors"


class Locks(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Locks"


class ElasticBands(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Elastic bands"


class LatchesAndElasticBands(BaseOfferCategory):
    elastic_bands = ElasticBands
    locks = Locks

    @classmethod
    def value(cls) -> str:
        return "Latches and Elastic Bands"


class SpiderBungeeCargoNets(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Spider Bungee Cargo Nets"


class InstrumentClustersAndSpeedometers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Instrument Clusters and Speedometers"


class Intercoms(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Intercoms"


class Raincoats(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Raincoats"


class TShirts(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "T-shirts"


class Boots(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Boots"


class SportsEyewear(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Sports Eyewear"


class Gloves(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Gloves"


class Balaclavas(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Balaclavas"


class ClothingAndFootwearAccessories(BaseOfferCategory):
    balaclavas = Balaclavas
    gloves = Gloves
    sports_eyewear = SportsEyewear

    @classmethod
    def value(cls) -> str:
        return "Accessories"


class ClothingAndFootwear(BaseOfferCategory):
    accessories = ClothingAndFootwearAccessories
    boots = Boots
    t_shirts = TShirts
    raincoats = Raincoats

    @classmethod
    def value(cls) -> str:
        return "Clothing and Footwear"


class Helmets(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Helmets"


class RearTopCases(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Rear Top Cases"


class SideCases(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Side Cases"


class Chests(BaseOfferCategory):
    side_cases = SideCases
    rear_top_cases = RearTopCases

    @classmethod
    def value(cls) -> str:
        return "Chests"


class MotorcycleAndATVAccessories(BaseOfferCategory):
    chests = Chests
    helmets = Helmets
    seat_covers = SeatCovers
    clothing_and_footwear = ClothingAndFootwear
    intercoms = Intercoms
    others = Others
    instrument_clusters_and_speedometers = InstrumentClustersAndSpeedometers
    spider_bungee_cargo_nets = SpiderBungeeCargoNets
    latches_and_elastic_bands = LatchesAndElasticBands
    helmet_visors = HelmetVisors

    @classmethod
    def value(cls) -> str:
        return "Motorcycle and ATV Accessories"


class SteeringWheelLocks(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Steering Wheel Locks"


class Rugs(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Rugs"


class TrashBags(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Trash Bags"


class SunVisor(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Sun Visor"


class Instrumental(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Instrumental"


class DashCam(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Dash Cam"


class DogCoats(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Dog Coats"


class SteeringWheelCovers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Steering Wheel Covers"


class BabyChairs(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Baby Chairs"


class Interior(BaseOfferCategory):
    baby_chairs = BabyChairs
    steering_wheel_covers = SteeringWheelCovers
    seat_covers = SeatCovers
    dog_coats = DogCoats
    dash_cam = DashCam
    instrumental = Instrumental
    others = Others
    sun_visor = SunVisor
    trash_bags = TrashBags
    rugs = Rugs
    steering_wheel_locks = SteeringWheelLocks

    @classmethod
    def value(cls) -> str:
        return "Interior"


class ParkingSensors(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Parking Sensors"


class RoofRacksAndCrossbars(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Roof Racks and Crossbars"


class RacksAndRoofCarriers(BaseOfferCategory):
    others = Others
    roof_racks_and_crossbars = RoofRacksAndCrossbars

    @classmethod
    def value(cls) -> str:
        return "Racks and Roof Carriers"


class AntiTheftBolts(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Anti-theft bolts"


class Hitches(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Hitches"


class TireValveCaps(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Tire Valve Caps"


class SignHolders(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Sign Holders"


class DoorHandleCovers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Door Handle Covers"


class Embellishers(BaseOfferCategory):
    door_handle_covers = DoorHandleCovers
    sign_holders = SignHolders
    tire_valve_caps = TireValveCaps

    @classmethod
    def value(cls) -> str:
        return "Embellishers"


class BackupCameras(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Backup Cameras"


class Covers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Covers"


class Hubcaps(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Hubcaps"


class WheelCenterCaps(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Wheel Center Caps"


class TirePressureGauge(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Tire Pressure Gauge"


class TireRepairKit(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Tire Repair Kit"


class WheelAccessories(BaseOfferCategory):
    tire_repair_kit = TireRepairKit
    tire_pressure_gauge = TirePressureGauge
    wheel_center_caps = WheelCenterCaps

    @classmethod
    def value(cls) -> str:
        return "Wheel Accessories"


class TruckBedAccessories(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Truck Bed Accessories"


class FinishesForRacks(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Finishes for Racks"


class Exterior(BaseOfferCategory):
    finishes_for_racks = FinishesForRacks
    truck_bed_accessories = TruckBedAccessories
    wheel_accessories = WheelAccessories
    hubcaps = Hubcaps
    covers = Covers
    portable_charges = PortableChargers
    backup_cameras = BackupCameras
    embellishers = Embellishers
    hitches = Hitches
    anti_theft_bolts = AntiTheftBolts
    racks_and_roof_carriers = RacksAndRoofCarriers
    parking_sensors = ParkingSensors

    @classmethod
    def value(cls) -> str:
        return "Exterior"


class CarAndPickupTruckAccessories(BaseOfferCategory):
    exterior = Exterior
    interior = Interior
    others = Others

    @classmethod
    def value(cls) -> str:
        return "Car and Pickup Truck Accessories"


class VehicleAccessories(BaseOfferCategory):
    car_and_pickup_truck_accessories = CarAndPickupTruckAccessories
    motorcyle_and_atv_accessories = MotorcycleAndATVAccessories
    marine_accessories = MarineAccessories
    heavy_duty_accessories = HeavyDutyAccessories
    vehicle_tools = VehicleTools
    automotive_cleaning = AutomotiveCleaning
    lubricants_and_fluids = LubricantsAndFluids
    gps_navigators_for_vehicles = GPSNavigatorsForVehicles
    performance = Performance
    car_and_pickup_truck_parts = CarAndPickupTruckParts
    heavy_duty_parts = HeavyDutyParts
    motorcyle_and_atv_parts = MotorcycleAndATVParts
    tires_and_accessories = TiresAndAccessories
    wheels = Wheels
    vehicle_safety = VehicleSafety
    car_audio = CarAudio
    tuning = Tuning

    @classmethod
    def value(cls) -> str:
        return "Vehicle Accessories"
