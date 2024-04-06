from enum import Enum
from pathlib import Path
import re
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
        discovered_by: list[CultureGroup],
        centre_of_trade: int | None = None,
        hre: bool = False,
        add_cores: list[Tag] | None = None, # type: ignore
        buildings: list[Building] | None = None, # type: ignore
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
        self.discovered_by: list[CultureGroup] = discovered_by

        if centre_of_trade is None:
            centre_of_trade = 0
        self.centre_of_trade: int = centre_of_trade
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
        with open(filename, "r") as f:
            owner = None
            capital = None
            culture = None
            trade_goods = None
            religion = None
            tax = None
            production = None
            manpower = None
            centre_of_trade = None
            lines = f.readlines()
            centre_of_trade: int | None
            discovered_by: list[CultureGroup] = []
            hre: bool = False
            add_cores: list[Tag] = []
            buildings: list[Building] = []
            is_city: bool = True
            controller: Tag | None = None
            
            for line in lines:
                match line:
                    case line if "owner" in line:
                        # finds SWE or F19 from "owner = SWE" or "owner = F19"
                        owner_str = re.findall(r"= (...)", line)[0]
                        owner = Tag(owner_str)
                    case line if "capital" in line:
                        # finds Stockholm from "capital = "Stockholm""
                        capital = re.findall(r'= "([a-zA-Z\d ]+)"', line)[0]
                    case line if "culture" in line:
                        # finds swedish from "culture = swedish"
                        culture_str = re.findall(r'= ([a-zA-Z_]+)', line)[0]
                        culture = Culture(culture_str)
                    case line if "trade_goods" in line:
                        # finds grain from trade_goods = grain
                        goods_str = re.findall(r'= ([a-zA-Z_]+)', line)[0]
                        trade_goods = TradeGood(goods_str)
                    case line if "religion" in line:
                        # finds catholic from "religion = catholic"
                        religion_str = re.findall(r'= ([a-zA-Z_]+)', line)[0]
                        religion = Religion(religion_str)
                    case line if "base_tax" in line:
                        # finds 4 from base_tax = 4
                        tax = int(re.findall(r'= (\d+)', line)[0])
                    case line if "base_production" in line:
                        # finds 4 from base_production = 4
                        production = int(re.findall(r'= (\d+)', line)[0])
                    case line if "base_manpower" in line:
                        # finds 4 from base_manpower = 4
                        manpower = int(re.findall(r'= (\d+)', line)[0])
                    case line if "centre_of_trade" in line:
                        # finds 2 from centre_of_trade = 2
                        centre_of_trade = int(re.findall(r'= (\d+)', line)[0])
                    case line if "discovered_by" in line:
                        group_str = re.findall(r'= ([a-zA-Z_]+)', line)
                        discovered_by.append(CultureGroup(group_str))
                    case line if "hre" in line:
                        hre = "yes" in line
                    case line if "add_core" in line:
                        core_tag = re.findall(r"= (...)", line)[0]
                        add_cores.append(Tag(core_tag))
                    case line if "fort_15th" in line:
                        buildings.append(Building("fort_15th"))
                    case line if "is_city" in line:
                        is_city = "yes" in line
                    case line if "controller" in line:
                        controller_str = owner_str = re.findall(r"= (...)", line)[0]
                        controller = Tag(controller_str)
                        
        if owner is None: raise ValueError("owner not found in province.txt")
        if capital is None: raise ValueError("capital not found in province.txt")
        if culture is None: raise ValueError("culture not found in province.txt")
        if trade_goods is None: raise ValueError("trade_goods not found in province.txt")
        if religion is None: raise ValueError("religion not found in province.txt")
        if tax is None: raise ValueError("tax not found in province.txt")
        if production is None: raise ValueError("production not found in province.txt")
        if manpower is None: raise ValueError("manpower not found in province.txt")
        
        return cls(
            owner,
            capital,
            culture,
            trade_goods,
            religion,
            tax,
            production,
            manpower,
            discovered_by,
            centre_of_trade,
            hre,
            add_cores,
            buildings,
            is_city,
            controller,
        )


class Map:
    def __init__(self, provinces: list[Province], countries: list[Country]):
        self.provinces = provinces
        self.countries = countries
