from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from src.leader import Leader
from src.enums import Culture, Religion, Tag
from src.date import Date


@dataclass
class Monarch():
    name: str
    dynasty: str
    adm: int
    dip: int
    mil: int
    birth_date: Date
    female: bool
    regent: bool
    religion: Religion
    culture: Culture
    
    leader: Optional[Leader]
    
    @classmethod
    def from_list_of_lines(cls, lines: list[str])->Monarch:
        ...
    
class Heir(Monarch):
    claim: int
    monarch_name: str

    @classmethod
    def from_list_of_lines(cls, lines: list[str])->Heir:
        ...

class Queen(Monarch):
    country_of_origin: Tag
    
    @classmethod
    def from_list_of_lines(cls, lines: list[str])->Queen:
        ...