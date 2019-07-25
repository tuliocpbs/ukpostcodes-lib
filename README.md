# United Kingdom API Postcodes Validation and Formatting - [Wikipedia Link](https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom)
![Test Coverage](ukpostcode-coverage.svg)

This UK postcode validation and formatting library provides 3 classes that you can work with, UK Postcode, Outward and Inward. Bellow you can see some examples how to use and what this classes can provide.

### Outward

Example:
```python
In [1]: outward = Outward('EC1A') # Raises InvalidOutward, InvalidOutwardArea or InvalidOutwardDistrict exceptions
In [2]: outward
Out[3]: 'EC1A'
In [4]: outward.area
Out[5]: 'EC'
In [6]: outward.district
Out[7]: '1A'
```

### Inward

Example:
```python
In [1]: inward = Inward('1BB') # Raises InvalidInwardSector or InvalidInwardUnit exceptions
In [2]: inward
Out[3]: '1BB'
In [4]: inward.sector
Out[5]: '1'
In [6]: inward.unit
Out[7]: 'BB'
```

### UKPostcode

Example 1:
```python
In [1]: ukpc = UKPostcode('ec1A1bb') # Raises InvalidOutward, InvalidOutwardArea, InvalidOutwardDistrict, InvalidInwardSector or InvalidInwardUnit exceptions
In [2]: ukpc
Out[3]: 'EC1A 1BB'
In [4]: ukpc.outward
Out[5]: 'EC1A'
In [6]: ukpc.inward
Out[7]: '1BB'
```

OR

Example 2:
```python
In [1]: UKPostcode.validate_postcode('ec1A1bb')
Out[2]: True
In [4]: UKPostcode.validate_postcode('ec1A1b0')
Out[5]: False
```