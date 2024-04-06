from dataclasses import dataclass

from src.leader import Leader
from src.enums import Culture, Religion
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
    
    leader: Leader