from enum import Enum
from pathlib import Path
from country import Country


class Tag(Enum):
    SWE = "SWE"


class Culture(Enum):
    SWEDISH = "swedish"

class CultureGroup(Enum):
    EAST_AFRICAN = "east_african"

class TradeGood(Enum):
    GRAIN = "grain"


class Religion(Enum):
    CATHOLIC = "catholic"

class Building(Enum):
    LVL2_FORT = "fort_15th"

class Province:
    def __init__(
        self,
        owner: Tag,
        capital: str,
        culture: Culture,
        trade_goods: TradeGood,
        religion: Religion,
        tax: int,
        production: int,
        manpower: int,
        centre_of_trade: int,
        discovered_by: list[CultureGroup],
        hre: bool = False,
        add_cores: list[Tag] = None,
        buildings: list[Building] = None,
        is_city: bool = True,
        controller: Tag | None = None,
    ):
        self.owner: Tag = owner
        self.capital: str = capital
        self.culture: Culture = culture
        self.trade_goods: TradeGood = trade_goods
        self.religion: Religion = religion
        self.tax: int = tax
        self.production: int = production
        self.manpower: int = manpower
        self.centre_of_trade: int = centre_of_trade
        self.discovered_by: list[CultureGroup] = discovered_by
        
        self.hre: bool = hre
        if add_cores is None:
            add_cores: list[Tag] = []
        self.add_cores: list[Tag] = add_cores
        if buildings is None:
            buildings: list[Building] = []
        self.buildings = buildings
        self.is_city: bool = is_city
        if controller is None:
            controller = owner
        self.controller: Tag = controller

    @classmethod
    def from_txt(cls, filename: Path):
        with open(filename, 'r') as f:
            lines = f.readlines()
                        
            owner: Tag
            capital: str
            culture: Culture
            trade_goods: TradeGood
            religion: Religion
            tax: int
            production: int
            manpower: int
            centre_of_trade: int
            discovered_by: list[CultureGroup]
            hre: bool = False
            add_cores: list[Tag] = None
            buildings: list[Building] = None
            is_city: bool = True
            controller: Tag | None = None
            

class Map:
    def __init__(self, provinces: list[Province], countries: list[Country]):
        self.provinces = provinces
        self.countries = countries
