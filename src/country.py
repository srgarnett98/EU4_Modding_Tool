from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import re
from typing import Optional
from date import START_DATE, Date
from src.monarch import Heir, Monarch, Queen
from src.province import Province
from src.enums import Culture, GovType, Religion, Tag, TechGroup


@dataclass
class CountryEffect:
    add_prestige: int
    add_treasury: int

    @classmethod
    def from_list_of_lines(cls, lines: list[str])->CountryEffect:
        ...

class Country:
    def __init__(
        self,
        tag: Tag,
        technology_group: TechGroup,
        gov_type: GovType,
        gov_rank: int,
        primary_culture: Culture,
        religion: Religion,
        capital: int,
        monarch: Optional[Monarch],
        heir: Optional[Heir],
        queen: Optional[Queen],
        unit_type: Optional[TechGroup],
        mercantilism: Optional[int],
        army_profesh: Optional[float],
        accepted_cultures: Optional[list[Culture]],
        removed_cultures: Optional[list[Culture]],
        historical_friends: Optional[list[Tag]],
        historical_rivals: Optional[list[Tag]],
        starting_state: dict[Date, CountryEffect],
    ):
        self.tag: Tag = tag
        self.technology_group: TechGroup = technology_group
        self.gov_type: GovType = gov_type
        self.gov_rank: int = gov_rank
        self.primary_culture: Culture = primary_culture
        self.religion: Religion = religion
        self.capital: int = capital
        self.monarch: Optional[Monarch] = monarch
        self.heir: Optional[Heir] = heir
        self.queen: Optional[Queen] = queen
        self.unit_type: Optional[TechGroup] = unit_type
        self.mercantilism: Optional[int] = mercantilism
        self.army_profesh: Optional[float] = army_profesh
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

    @classmethod
    def from_txt(cls, filename: Path) -> Country:
        stem = filename.stem
        tag = Tag(re.findall(r"(...)[ ]*-[ ]*", stem)[0])

        technology_group = None
        gov_type = None
        gov_rank = None
        primary_culture = None
        religion = None
        capital = None
        monarch: Optional[Monarch] = None
        heir: Optional[Heir] = None
        queen: Optional[Queen] = None
        unit_type: Optional[TechGroup] = None
        mercantilism: Optional[int] = None
        army_profesh: Optional[float] = None
        accepted_cultures: Optional[list[Culture]] = []
        removed_cultures: Optional[list[Culture]] = []
        historical_friends: Optional[list[Tag]] = []
        historical_rivals: Optional[list[Tag]] = []
        starting_state: dict[Date, CountryEffect] = {}

        with open(filename, "r") as f:
            lines = f.readlines()

            for i, line in enumerate(lines):
                match line:
                    case line if line.startswith("	"):
                        pass
                    case line if "technology_group" in line:
                        # finds SWE or F19 from "owner = SWE" or "owner = F19"
                        tech_group_str = re.findall(r"= ([a-zA-Z_-\d]+)", line)[0]
                        technology_group = TechGroup(tech_group_str)
                    case line if "government = " in line:
                        gov_type_str = re.findall(r"= ([a-zA-Z_-\d]+)", line)[0]
                        gov_type = GovType(gov_type_str)
                    case line if "government_rank = " in line:
                        gov_rank = int(re.findall(r"= (\d)", line)[0])
                    case line if "primary_culture" in line:
                        culture_str = re.findall(r"= ([a-zA-Z_-\d]+)", line)[0]
                        primary_culture = Culture(culture_str)
                    case line if "religion" in line:
                        religion_str = re.findall(r"= ([a-zA-Z_-\d]+)", line)[0]
                        religion = Religion(religion_str)
                    case line if "capital" in line:
                        capital = int(re.findall(r"= (\d+)", line)[0])
                    case line if "monarch" in line:
                        monarch_lines = []
                        j = i
                        while not lines[j].startswith("}"):
                            monarch_lines.append(lines[j])
                            j += 1
                        monarch = Monarch.from_list_of_lines(monarch_lines)
                    case line if "heir" in line:
                        heir_lines = []
                        j = i
                        while not lines[j].startswith("}"):
                            heir_lines.append(lines[j])
                            j += 1
                        heir = Heir.from_list_of_lines(heir_lines)
                    case line if "queen" in line:
                        queen_lines = []
                        j = i
                        while not lines[j].startswith("}"):
                            queen_lines.append(lines[j])
                            j += 1
                        queen = Queen.from_list_of_lines(queen_lines)
                    case line if "mercantilism" in line:
                        mercantilism = int(re.findall(r"= (\d+)", line)[0])
                    case line if "army_professionalism" in line:
                        army_profesh = float(re.findall(r"= (\d*.*\d*)", line)[0])
                    case line if "add_accepted_culture" in line:
                        # finds swedish from "culture = swedish"
                        culture_str = re.findall(r"= ([a-zA-Z_-\d]+)", line)[0]
                        accepted_cultures.append(Culture(culture_str))
                    case line if "remove_accepted_culture" in line:
                        # finds swedish from "culture = swedish"
                        culture_str = re.findall(r"= ([a-zA-Z_-\d]+)", line)[0]
                        removed_cultures.append(Culture(culture_str))
                    case line if "historical_friend" in line:
                        tag_str = re.findall(r"= (...)", line)[0]
                        historical_friends.append(Tag(tag_str))
                    case line if "historical_rival" in line:
                        tag_str = re.findall(r"= (...)", line)[0]
                        historical_rivals.append(Tag(tag_str))
                    case line if re.search(r"1\d\d\d\.\d+\.\d+", line):
                        state_lines =[]
                        j = i
                        while not lines[j].startswith("}"):
                            state_lines.append(lines[j])
                            j += 1
                        starting_state[START_DATE] = CountryEffect.from_list_of_lines(state_lines)

        if technology_group is None:
            raise ValueError("technology_group not found in province.txt")
        if gov_type is None:
            raise ValueError("gov_type not found in province.txt")
        if gov_rank is None:
            raise ValueError("gov_rank not found in province.txt")
        if primary_culture is None:
            raise ValueError("primary_culture not found in province.txt")
        if religion is None:
            raise ValueError("religion not found in province.txt")
        if capital is None:
            raise ValueError("capital not found in province.txt")

        return cls(
            tag=tag,
            technology_group=technology_group,
            gov_type=gov_type,
            gov_rank=gov_rank,
            primary_culture=primary_culture,
            religion=religion,
            capital=capital,
            monarch=monarch,
            heir=heir,
            queen=queen,
            unit_type=unit_type,
            mercantilism=mercantilism,
            army_profesh=army_profesh,
            accepted_cultures=accepted_cultures,
            removed_cultures=removed_cultures,
            historical_friends=historical_friends,
            historical_rivals=historical_rivals,
            starting_state=starting_state,
        )
