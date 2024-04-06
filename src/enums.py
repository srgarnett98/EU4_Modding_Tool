from enum import Enum

class TechGroup(Enum):
    EAST_AFRICAN = 'east_african'

class GovType(Enum):
    MONARCHY = "monarchy"
    REPUBLIC = "republic"
    THEOCRACY = "theocracy"
    
class Tag(Enum):
    SWE = "SWE"
    AKS = "AKS"


class Culture(Enum):
    SWEDISH = "swedish"
    CUSTOM1 = "dynamic-beja-somali-sidamo-culture-num1"


class CultureGroup(Enum):
    EAST_AFRICAN = "east_african"
    EASTERN = "eastern"
    INDIAN = "indian"
    MUSLIM = "muslim"
    NOMAD_GROUP = "nomad_group"
    OTTOMAN = "ottoman"
    SUB_SAHARAN = "sub_saharan"
    WESTERN = "western"


class TradeGood(Enum):
    GRAIN = "grain"


class Religion(Enum):
    CATHOLIC = "catholic"
    COPTIC = "coptic"


class Building(Enum):
    LVL2_FORT = "fort_15th"
