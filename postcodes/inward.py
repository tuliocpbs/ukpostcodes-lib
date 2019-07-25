import re

from .exceptions import InvalidInwardSector, InvalidInwardUnit

REGEX_INWARD_SECTOR = r"^([0-9])$"
REGEX_INWARD_UNIT = r"^([A-Za-z]{2}|[Gg][Ii][Rr] [Aa]{2})$"

class Inward():

    def __init__(self, inward):
        self.sector = inward[0]
        self.unit = inward[1:]

        self.__validate_sector()
        self.__validate_unit()

    def __validate_sector(self):
        if not bool(re.match(REGEX_INWARD_SECTOR, self.sector)):
            raise InvalidInwardSector()

    def __validate_unit(self):
        if not bool(re.match(REGEX_INWARD_UNIT, self.unit)):
            raise InvalidInwardUnit()

    def __repr__(self):
        return (self.sector + self.unit).upper()
