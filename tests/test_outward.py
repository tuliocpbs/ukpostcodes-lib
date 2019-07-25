import unittest

from postcodes.exceptions import InvalidOutwardArea, InvalidOutwardDistrict, InvalidOutward
from postcodes.outward import Outward


class TestOutward(unittest.TestCase):

    def test_valids_outwards(self):
        valids = ["EC1A", "SL5", "B92", "M1", "L1"]

        for outward in valids:
            assert str(Outward(outward)) in valids

    def test_invalids_outwards(self):
        invalids = ["MMM", "K", "ECAA"] 

        for outward in invalids:
            self.assertRaises(InvalidOutward, Outward, outward)

    def test_invalids_outwards_areas(self):
        invalids = ["99", "?C1A", " 1", "9NLK"]

        for outward in invalids:
            self.assertRaises(InvalidOutwardArea, Outward, outward)

    def test_invalids_outwards_districts(self):
        invalids = ["SL555", "L99K"]

        for outward in invalids:
            self.assertRaises(InvalidOutwardDistrict, Outward, outward)
