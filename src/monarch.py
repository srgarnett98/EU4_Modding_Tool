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
    
class Heir(Monarch):
    claim: int
    monarch_name: str

class Queen(Monarch):
    country_of_origin: Tag