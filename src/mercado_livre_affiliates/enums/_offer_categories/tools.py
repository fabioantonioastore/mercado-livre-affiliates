from .base import BaseOfferCategory
from .common import Others


class MeasurementsAndInstrumentation(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Measurements and Instrumentation"


class GardenTools(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Garden Tools"


class PneumaticTools(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Pneumatic Tools"


class HandTools(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Hand Tools"


class IndustrialTools(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Industrial Tools"


class PowerTools(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Power Tools"


class BoxesAndOrganizers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Boxes and Organizers"


class ToolAccessories(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Tool Accessories"


class Tools(BaseOfferCategory):
    TOOL_ACCESSORIES = ToolAccessories
    BOXES_AND_ORGANIZERS = BoxesAndOrganizers
    POWER_TOOLS = PowerTools
    INDUSTRIAL_TOOLS = IndustrialTools
    HAND_TOOLS = HandTools
    PNEUMATIC_TOOLS = PneumaticTools
    GARDEN_TOOLS = GardenTools
    MEASUREMENTS_AND_INSTRUMENTATION = MeasurementsAndInstrumentation
    OTHERS = Others

    @classmethod
    def value(cls) -> str:
        return "Tools"
    