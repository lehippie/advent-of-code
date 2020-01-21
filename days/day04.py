"""Day 4 script."""

import env
from lib import passwords

# Input
pstart = 153517
pstop = 630395

# Part 1:
pcount = 0
for p in range(pstart, pstop + 1):
    if passwords.validity(p):
        pcount += 1
print(f"They are {pcount} valid passwords within {pstart}-{pstop}.")
assert pcount == 1729

# Part 2:
pcount = 0
for p in range(pstart, pstop + 1):
    if passwords.full_validity(p):
        pcount += 1
print(f"They are {pcount} (really) valid passwords within {pstart}-{pstop}.")
assert pcount == 1172
