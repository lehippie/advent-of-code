"""Day 4 script."""

import env
from lib import passwords

# Input
pstart = 153517
pstop = 630395

# Part 1: 1729
pcount = 0
for p in range(pstart, pstop + 1):
    if passwords.validity(p):
        pcount += 1
print(f"They are {pcount} valid passwords within {pstart}-{pstop}.")

# Part 2: 1172
pcount = 0
for p in range(pstart, pstop + 1):
    if passwords.full_validity(p):
        pcount += 1
print(f"They are {pcount} (really) valid passwords within {pstart}-{pstop}.")
