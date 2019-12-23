"""Tests of fuel calculation functions."""

import env
from lib import passwords


def tests():
    assert passwords.validity(122345) == True
    assert passwords.validity(111123) == True
    assert passwords.validity(111111) == True
    assert passwords.validity(123) == False
    assert passwords.validity(1234567) == False
    assert passwords.validity(134679) == False
    assert passwords.validity(223450) == False
    assert passwords.validity(123789) == False
    assert passwords.validity(123789) == False
    assert passwords.full_validity(112233) == True
    assert passwords.full_validity(123444) == False
    assert passwords.full_validity(111122) == True

if __name__ == "__main__":
    tests()
