from __future__ import annotations
from typing import Any


class Date:
    def __init__(self, yr: int, mo: int, day: int):
        self.yr: int = yr
        self.mo: int = mo
        self.day: int = day

    def to_str(self) -> str:
        return str(self.yr) + "." + str(self.mo) + "." + str(self.day)

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other: Date | Any) -> bool:
        if not isinstance(other, Date):
            raise NotImplementedError("Can't compare date and not a date")
        return self.yr == other.yr and self.mo == other.mo and self.day == other.day


START_DATE = Date(1444, 11, 11)
