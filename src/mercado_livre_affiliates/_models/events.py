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
    old_price: Price
    current_price: Price
    discount_factor: float


@dataclass
class LightningDealProduct(EventResponse):
    title: str
    url: str
    image_url: str
    rating: float
    total_reviews: int
    old_price: Price
    current_price: Price
    discount_factor: float
    expires_in: datetime
