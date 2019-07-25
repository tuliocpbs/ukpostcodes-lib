import re

from .exceptions import InvalidOutwardArea, InvalidOutwardDistrict, InvalidOutward

REGEX_OUTWARD_AREA = r"^([A-Za-z][A-Ha-hK-Yk-y]?)$"
REGEX_OUTWARD_DISTRICT = r"^([0-9][A-Za-z0-9]?)$"

class Outward():

    def __init__(self, outward):
        try:
            sep = re.search(r"\d",outward).start() # Separator between area and district
        except:
            raise InvalidOutward()

        self.area = outward[:sep]
        self.district = outward[sep:]

        self.__validate_area()
        self.__validate_district()

    def __validate_area(self):
        if not bool(re.match(REGEX_OUTWARD_AREA, self.area)):
            raise InvalidOutwardArea()

    def __validate_district(self):
        if not bool(re.match(REGEX_OUTWARD_DISTRICT, self.district)):
            raise InvalidOutwardDistrict

    def __repr__(self):
        return (self.area + self.district).upper()
