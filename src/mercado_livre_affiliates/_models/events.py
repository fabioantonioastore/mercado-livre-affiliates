from typing import TypeVar
from datetime import datetime
from dataclasses import dataclass

from . import BaseModel
from . import Price


@dataclass
class EventResponse(BaseModel):
    title: str
    url: str
    image_url: str
    rating: float
    total_reviews: int
    categories: set[str]
    old_price: Price
    current_price: Price


EventResponseT = TypeVar("EventResponseT", bound=EventResponse)


@dataclass
class DealOfTheDayProduct(EventResponse):
    pass


@dataclass
class LightningDealProduct(EventResponse):
    expires_in: datetime
