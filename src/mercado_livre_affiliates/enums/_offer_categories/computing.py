from .base import BaseOfferCategory


class TabletsAndAccessories(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Tablets and Accessories"


class Software(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Software"


class ProjectorsAndScreens(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Projectors and Screens"


class LaptopsAndAccessories(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Laptops and Accessories"


class PCPeripherals(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "PC Peripherals"


class PalmDevicesAndHandhelds(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Palm Devices and Handhelds"


class DesktopPC(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Desktop PC"


class MonitorsAndAccessories(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Monitors and Accessories"


class PCCleaning(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "PC Cleaning"


class ReadersAndScanners(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Readers and Scanners"


class Print(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Print"


class VoltageStabilizersAndUPSUnits:
    @classmethod
    def value(cls) -> str:
        return "Voltage Stabilizers and UPS Units"


class ConnectivityAndNetworking(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Connectivity and Networking"


class PCComponents(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "PC Components"


class USBCablesAndHubs(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "USB Cables and Hubs"


class Storage(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Storage"


class PCGamingAccessories(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "PC Gaming Accessories"


class Computing(BaseOfferCategory):
    PC_GAMING_ACCESSORIES = PCGamingAccessories
    STORAGE = Storage
    USB_CABLES_AND_HUBS = USBCablesAndHubs
    PC_COMPONENTS = PCComponents
    CONNECTIVITY_AND_NETWORKING = ConnectivityAndNetworking
    VOLTAGE_STABILIZERS_AND_UPS_UNITS = VoltageStabilizersAndUPSUnits
    PRINT = Print
    READERS_AND_SCANNERS = ReadersAndScanners
    PC_CLEANING = PCCleaning
    MONITORS_AND_ACCESSORIES = MonitorsAndAccessories
    DESKTOP_PC = DesktopPC
    PALM_DEVICES_AND_HANDLEHELDS = PalmDevicesAndHandhelds
    PC_PERIPHERALS = PCPeripherals
    LAPTOPS_AND_ACCESSORIES = LaptopsAndAccessories
    PROJECTORS_AND_SCREENS = ProjectorsAndScreens
    SOFTWARE = Software
    TABLETS_AND_ACCESSORIES = TabletsAndAccessories

    @classmethod
    def value(cls) -> str:
        return "Computing"
