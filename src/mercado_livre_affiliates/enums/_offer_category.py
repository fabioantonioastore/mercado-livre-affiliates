from typing_extensions import Self

from ._offer_categories import Games
from ._offer_categories import AntiquesAndCollectibles




class OfferCategory:
    antiques_and_collectibles = AntiquesAndCollectibles
    games = Games

    def __new__(cls) -> Self:
        raise RuntimeError("This class cannot be instanciated")
