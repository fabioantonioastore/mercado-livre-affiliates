from dataclasses import dataclass


@dataclass
class Price:
    reais: int
    cents: int
