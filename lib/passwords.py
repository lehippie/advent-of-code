"""Venus passwords validity functions."""

import re


def validity(pw):
    """Determine validity of Venus fuel depot password."""
    pw = [int(d) for d in str(pw)]
    if len(pw) != 6:
        return False
    if sorted(pw) != pw:
        return False
    double = False
    for d1, d2 in zip(pw[:-1], pw[1:]):
        if d1 == d2:
            double = True
    return double


def full_validity(pw):
    """Full validity of Venus fuel depot password."""
    if validity(pw):
        groups = re.findall(r'((\d)\2+)', str(pw))
        glen = [len(g[0]) for g in groups]
        if 2 in glen:
            return True
    return False


if __name__ == "__main__":
    import env
    from tests import tests_passwords
    tests_passwords.tests()
