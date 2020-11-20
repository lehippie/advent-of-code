"""Tests of Venus password library."""

import password


def tests():
    assert password.validity(122345) == True
    assert password.validity(111123) == True
    assert password.validity(111111) == True
    assert password.validity(123) == False
    assert password.validity(1234567) == False
    assert password.validity(134679) == False
    assert password.validity(223450) == False
    assert password.validity(123789) == False
    assert password.validity(123789) == False
    assert password.full_validity(112233) == True
    assert password.full_validity(123444) == False
    assert password.full_validity(111122) == True

if __name__ == "__main__":
    tests()
