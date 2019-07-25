import re

from .inward import Inward
from .outward import Outward


class UKPostcode():

    def __init__(self, postcode):
        self.postcode = postcode.replace(" ", "")
        self.outward = Outward(self.postcode[:-3])
        self.inward = Inward(self.postcode[-3:])

    def __repr__(self):
        return str(self.outward) + " " + str(self.inward)

    @classmethod
    def validate_postcode(cls, postcode):
        try:
            UKPostcode(postcode)
            return True
        except:
            return False
    