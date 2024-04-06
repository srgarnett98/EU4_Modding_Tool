from src.country import Country
from src.province import Province

class Map:
    def __init__(self, provinces: list[Province], countries: list[Country]):
        self.provinces = provinces
        self.countries = countries
