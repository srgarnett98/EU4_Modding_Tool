from dataclasses import dataclass
from enum import Enum

class LeaderTypes(Enum):
    GENERAL = 'general'
    ADMIRAL = 'admiral'
    EXPLORER = 'explorer'
    CONQUISTADOR = 'conquistador'

@dataclass
class Leader:
    name: str
    variant: LeaderTypes
    fire: int
    shock: int
    manuever: int
    siege: int