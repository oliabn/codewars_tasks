"""
Task: Counting Valleys
- Count how many valleys you will pass
- Start is always from zero level0
- Input: s='FUFFDDFDUDFUFUF'     U=UP, F=FORWARD, D=DOWN
(level 1)  __
(level 0)_/  \         _(exit we are again on level 0)
(entry-1)     \_     _/
(level-2)       \/\_/

- Valley: every time you go down below level0 counts as an entry of a valley,
and as you go up to level0 from valley counts as an exit of a valley
- One passed valley is equal one entry and one exit of a valley.
"""


def counting_valleys(s):
    valleys = 0
    level = 0
    for go in s:
        if go == "U" and level == -1:
            valleys += 1
        if go == "U":
            level += 1
        elif go == "D":
            level -= 1
    return valleys


# Test
print(f"Expected: {0}, Current: {counting_valleys('UFFFD')}")
print(f"Expected: {2}, Current: {counting_valleys('DDUUDDUU')}")
print(f"Expected: {4}, Current: {counting_valleys('UFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFU')}")