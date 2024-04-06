from dataclasses import dataclass
from typing import Optional
from date import Date
from src.monarch import Heir, Monarch, Queen
from src.province import Province
from src.enums import Culture, GovType, Religion, Tag, TechGroup, UnitType

@dataclass
class CountryEffect():
    add_prestige: int
    add_treasury: int

class Country:
    def __init__(
        self,
        tag: Tag,
        technology_group: TechGroup,
        gov_type: GovType,
        gov_rank: int,
        primary_culture: Culture,
        religion: Religion,
        mercantilism: int,
        army_profesh: float,
        capital: Province,
        monarch: Monarch,
        heir: Optional[Heir],
        queen: Optional[Queen],
        unit_type: Optional[UnitType],
        accepted_cultures: Optional[list[Culture]],
        removed_cultures: Optional[list[Culture]],
        historical_friends: Optional[list[Tag]],
        historical_rivals: Optional[list[Tag]],
        starting_state: dict[Date, CountryEffect]
        ):
        self.tag: Tag = tag
        self.technology_group: TechGroup = technology_group
        self.gov_type: GovType = gov_type
        self.gov_rank: int = gov_rank
        self.primary_culture: Culture = primary_culture
        self.religion: Religion = religion
        self.mercantilism: int = mercantilism
        self.army_profesh: float = army_profesh
        self.capital: Province = capital
        self.monarch: Monarch = monarch
        self.heir: Optional[Heir] = heir
        self.queen: Optional[Queen] = queen
        self.unit_type: Optional[UnitType] = unit_type
        if accepted_cultures is None:
            accepted_cultures = []
        self.accepted_cultures: Optional[list[Culture]] = accepted_cultures
        if removed_cultures is None:
            removed_cultures = []
        self.removed_cultures: Optional[list[Culture]] = removed_cultures
        if historical_friends is None:
            []
        self.historical_friends: Optional[list[Tag]] = historical_friends
        if historical_rivals is None:
            historical_rivals = []
        self.historical_rivals: Optional[list[Tag]] = historical_rivals
        
        self.starting_state: dict[Date, CountryEffect] = starting_state
        