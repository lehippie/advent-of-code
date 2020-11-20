"""Day 4: Secure Container."""

import password

# Input
pstart = 153517
pstop = 630395

# Part 1:
pcount = 0
for p in range(pstart, pstop + 1):
    if password.validity(p):
        pcount += 1
print(f"They are {pcount} valid passwords within {pstart}-{pstop}.")
assert pcount == 1729

# Part 2:
pcount = 0
for p in range(pstart, pstop + 1):
    if password.full_validity(p):
        pcount += 1
print(f"They are {pcount} (really) valid passwords within {pstart}-{pstop}.")
assert pcount == 1172
