"""Venus password library."""

import re


def validity(password):
    """Determine validity of Venus fuel depot password."""
    password = [int(d) for d in str(password)]
    if len(password) != 6:
        return False
    if sorted(password) != password:
        return False
    double = False
    for d1, d2 in zip(password[:-1], password[1:]):
        if d1 == d2:
            double = True
    return double


def full_validity(password):
    """Full validity of Venus fuel depot password."""
    if validity(password):
        groups = re.findall(r'((\d)\2+)', str(password))
        glen = [len(g[0]) for g in groups]
        if 2 in glen:
            return True
    return False


if __name__ == "__main__":
    from password_tests import tests
    tests()
