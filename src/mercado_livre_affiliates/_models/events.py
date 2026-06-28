from typing import TypeVar
from datetime import datetime
from dataclasses import dataclass

from . import BaseModel
from . import Price


class EventResponse(BaseModel):
    pass


EventResponseT = TypeVar("EventResponseT", bound=EventResponse)


@dataclass
class DealOfTheDayProduct(EventResponse):
    title: str
    url: str
    image_url: str
    rating: float
    total_reviews: int
    categories: list[str]
    old_price: Price
    current_price: Price


@dataclass
class LightningDealProduct(EventResponse):
    title: str
    url: str
    image_url: str
    rating: float
    total_reviews: int
    categories: list[str]
    old_price: Price
    current_price: Price
    expires_in: datetime
