from .base import BaseOfferCategory


class ParlorGames(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Parlor Games" \
        ""


class Volleyball(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Volleyball"


class TennisPadelAndSquash(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Tennis, Padel, and Squash"


class Tennis(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Tennis"


class ShootingSports(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Shooting Sports"


class SupplementsAndShakers(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Supplements and Shakers"


class RappellingMountaineeringAndRockClimbing(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Rappelling, Mountaineering, and Rock Climbing"


class RollerSkatingAndSkateboarding(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Roller Skating and Skateboarding"


class KickScootersAndMotorScooters(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Kick Scooters and Motor Scooters"


class Swimming(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Swimming"


class SportsInstructors(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Sports Instructors"


class Activewear(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Activewear"


class Dive(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Dive"


class Handball(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Handball"


class Golf(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Golf"


class Soccer(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Soccer"


class FitnessAndWeightTraining(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Fitness and Weight Training"


class SkiingAndSnowboarding(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Skiing and Snowboarding"


class HorsebackRiding(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Horseback Riding"


class Cycling(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Cycling"


class CanoesKayaksAndInflatables(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Canoes, Kayaks, and Inflatables"


class CampingHuntingAndFishing(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Camping, Hunting, and Fishing"


class Basketball(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Basketball"


class MartialArtsAndBoxing(BaseOfferCategory):
    @classmethod
    def value(cls) -> str:
        return "Martial Arts and Boxing"


class SportsAndFitness(BaseOfferCategory):
    MARTIAL_ARTS_AND_BOXING = MartialArtsAndBoxing
    BASKETBALL = Basketball
    CAMPING_HUNTING_AND_FISHING = CampingHuntingAndFishing
    CANOES_KAYAKS_AND_INFLATABLES = CanoesKayaksAndInflatables
    CYCLING = Cycling
    HORSEBACK_RIDING = HorsebackRiding
    SKIING_AND_SNOWBOARDING = SkiingAndSnowboarding
    FITNESS_AND_WEIGHT_TRAINING = FitnessAndWeightTraining
    SOCCER = Soccer
    GOLF = Golf
    HANDBALL = Handball
    DIVE = Dive
    ACTIVEWEAR = Activewear
    SPORTS_INSTRUCTORS = SportsInstructors
    SWIMMING = Swimming
    KICK_SCOOTERS_AND_MOTOR_SCOOTERS = KickScootersAndMotorScooters
    ROLLER_SKATING_AND_SKATEBOARDING = RollerSkatingAndSkateboarding
    RAPPELING_MOUNTAINEERING_AND_ROCK_CLIMBING = RappellingMountaineeringAndRockClimbing
    SUPPLEMENTS_AND_SHAKERS = SupplementsAndShakers
    SHOOTING_SPORTS = ShootingSports
    TENNIS = Tennis
    TENNIS_PADEL_AND_SQUASH = TennisPadelAndSquash
    VOLLEYBALL = Volleyball
    PARLOR_GAMES = ParlorGames

    @classmethod
    def value(cls) -> str:
        return "Sports and Fitness"
    