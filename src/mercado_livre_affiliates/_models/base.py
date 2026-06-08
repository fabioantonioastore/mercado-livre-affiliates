from typing import Iterator, Any
from dataclasses import dataclass, fields


@dataclass
class BaseModel:
    def __iter__(self) -> Iterator[tuple[str, Any]]:
        for field in fields(self):
            yield field.name, getattr(self, field.name)
