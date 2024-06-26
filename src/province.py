from __future__ import annotations
from enum import Enum
from pathlib import Path
import re
from src.enums import Building, Culture, CultureGroup, Religion, Tag, TradeGood
from src.country import Country

class Province:
    def __init__(
        self,
        province_id: int,
        owner: Tag,
        capital: str,
        culture: Culture,
        trade_goods: TradeGood,
        religion: Religion,
        tax: int,
        production: int,
        manpower: int,
        discovered_by: list[CultureGroup],
        center_of_trade: int | None = None,
        hre: bool = False,
        add_cores: list[Tag] | None = None,  # type: ignore
        buildings: list[Building] | None = None,  # type: ignore
        is_city: bool = True,
        controller: Tag | None = None,
    ):
        self.province_id: int = province_id
        self.owner: Tag = owner
        self.capital: str = capital
        self.culture: Culture = culture
        self.trade_goods: TradeGood = trade_goods
        self.religion: Religion = religion
        self.tax: int = tax
        self.production: int = production
        self.manpower: int = manpower
        self.discovered_by: list[CultureGroup] = discovered_by

        if center_of_trade is None:
            center_of_trade = 0
        self.center_of_trade: int = center_of_trade
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
    def from_txt(cls, filename: Path) -> Province:
        stem = filename.stem
        province_id = int(re.findall(r'(\d+)[ ]*-[ ]*', stem)[0])
        
        owner = None
        capital = None
        culture = None
        trade_goods = None
        religion = None
        tax = None
        production = None
        manpower = None
        center_of_trade = None
        center_of_trade: int | None = None
        discovered_by: list[CultureGroup] = []
        hre: bool = False
        add_cores: list[Tag] = []
        buildings: list[Building] = []
        is_city: bool = True
        controller: Tag | None = None

        with open(filename, "r") as f:
            lines = f.readlines()

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
                        culture_str = re.findall(r"= ([a-zA-Z_\-\d]+)", line)[0]
                        culture = Culture(culture_str)
                    case line if "trade_goods" in line:
                        # finds grain from trade_goods = grain
                        goods_str = re.findall(r"= ([a-zA-Z_\-\d]+)", line)[0]
                        trade_goods = TradeGood(goods_str)
                    case line if "religion" in line:
                        # finds catholic from "religion = catholic"
                        religion_str = re.findall(r"= ([a-zA-Z_\-\d]+)", line)[0]
                        religion = Religion(religion_str)
                    case line if "base_tax" in line:
                        # finds 4 from base_tax = 4
                        tax = int(re.findall(r"= (\d+)", line)[0])
                    case line if "base_production" in line:
                        # finds 4 from base_production = 4
                        production = int(re.findall(r"= (\d+)", line)[0])
                    case line if "base_manpower" in line:
                        # finds 4 from base_manpower = 4
                        manpower = int(re.findall(r"= (\d+)", line)[0])
                    case line if "center_of_trade" in line:
                        # finds 2 from center_of_trade = 2
                        center_of_trade = int(re.findall(r"= (\d+)", line)[0])
                    case line if "discovered_by" in line:
                        group_str = re.findall(r"= ([a-zA-Z_\-\d]+)", line)[0]
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

        if owner is None:
            raise ValueError("owner not found in province.txt")
        if capital is None:
            raise ValueError("capital not found in province.txt")
        if culture is None:
            raise ValueError("culture not found in province.txt")
        if trade_goods is None:
            raise ValueError("trade_goods not found in province.txt")
        if religion is None:
            raise ValueError("religion not found in province.txt")
        if tax is None:
            raise ValueError("tax not found in province.txt")
        if production is None:
            raise ValueError("production not found in province.txt")
        if manpower is None:
            raise ValueError("manpower not found in province.txt")

        return cls(
            province_id=province_id,
            owner=owner,
            capital=capital,
            culture=culture,
            trade_goods=trade_goods,
            religion=religion,
            tax=tax,
            production=production,
            manpower=manpower,
            discovered_by=discovered_by,
            center_of_trade=center_of_trade,
            hre=hre,
            add_cores=add_cores,
            buildings=buildings,
            is_city=is_city,
            controller=controller,
        )

    def to_txt(self, filename: Path):
        # lets just assert that you're naming it with the ID in front
        stem = filename.stem
        province_id = int(re.findall(r'(\d+)[ ]*-[ ]*', stem)[0])
        assert province_id == self.province_id
        
        with open(filename, "w") as f:
            f.write("owner = {}\n".format(self.owner.value))
            f.write("controller = {}\n".format(self.controller.value))
            f.write('capital = "{}"\n'.format(self.capital))
            f.write(
                "is_city = {}\n".format(
                    "yes" * self.is_city + "no" * (not self.is_city)
                )
            )
            f.write("culture = {}\n".format(self.culture.value))
            f.write("religion = {}\n".format(self.religion.value))
            f.write("trade_goods = {}\n".format(self.trade_goods.value))
            if Building.LVL2_FORT in self.buildings:
                f.write("{} = yes\n".format(Building.LVL2_FORT.value))
            f.write("base_tax = {}\n".format(str(self.tax)))
            f.write("base_production = {}\n".format(str(self.production)))
            f.write("base_manpower = {}\n".format(str(self.manpower)))
            if self.center_of_trade > 0:
                f.write("center_of_trade = {}\n".format(str(self.center_of_trade)))
            for tag in self.add_cores:
                f.write("add_core = {}\n".format(tag.value))
            for group in self.discovered_by:
                f.write("discovered_by = {}\n".format(group.value))
            if self.hre:
                f.write("hre = yes")
