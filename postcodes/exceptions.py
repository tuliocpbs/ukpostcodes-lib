class InvalidOutward(Exception):
    """Raise when a outward is invalid"""
    def __init__(self):
        Exception.__init__(self,"Invalid Outward")

class InvalidOutwardArea(Exception):
    """Raise when a outward area is invalid"""
    def __init__(self):
        Exception.__init__(self,"Invalid Outward Area")


class InvalidOutwardDistrict(Exception):
    """Raise when a outward district is invalid"""
    def __init__(self):
        Exception.__init__(self,"Invalid Outward District")


class InvalidInwardSector(Exception):
    """Raise when a inward sector is invalid"""
    def __init__(self):
        Exception.__init__(self,"Invalid Inward Sector")


class InvalidInwardUnit(Exception):
    """Raise when a inward unit is invalid"""
    def __init__(self):
        Exception.__init__(self,"Invalid Inward Unit")