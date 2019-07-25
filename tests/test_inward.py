import unittest

from postcodes.exceptions import InvalidInwardSector, InvalidInwardUnit
from postcodes.inward import Inward


class TestInward(unittest.TestCase):

    def test_valids_inwards(self):
        valids = ["7HF", "0KK", "9JP", "9NL", "1AE"]

        for inward in valids:
            assert str(Inward(inward)) in valids

    def test_invalids_inwards_sectors(self):
        invalids = ["KLK", "?LK", " Lk"] 

        for inward in invalids:
            self.assertRaises(InvalidInwardSector, Inward, inward)

    def test_invalids_inwards_units(self):
        invalids = ["99F", "8J0", "0?P", "9NLK"] 

        for inward in invalids:
            self.assertRaises(InvalidInwardUnit, Inward, inward)
