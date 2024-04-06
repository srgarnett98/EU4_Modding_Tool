class Date:
    def __init__(self, yr: int, mo: int, day:int):
        self.yr:int = yr
        self.mo:int = mo
        self.day:int = day
    
    def to_str(self):
        return str(self.yr) +"." + str(self.mo) + "." + str(self.day)
    
START_DATE = Date(1444, 11, 11)