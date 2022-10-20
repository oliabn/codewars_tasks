"""
Task: Positions Average
________________________
Suppose you have 4 numbers: '0', '9', '6', '4' and 3 strings composed with them:
s1 = "6900690040"
s2 = "4690606946"
s3 = "9990494604"

1) Compare s1-s2 -> to see how many positions they have in common: 0 at index 3,
 6 at index 4, 4 at index 8 ie 3 common positions out of 10.
2) Compare s1-s3 -> to see how many positions they have in common: 9 at index 1, 0 at index 3,
9 at index 5 ie 3 common positions out of 10.
3) Compare s2-s3 -> We find 2 common positions out of 10.
4) So for the 3 strings we have 8 common positions out of 30 ie 0.2666... or 26.666...%

Given n substrings (n >= 2) in a string s our function pos_average will calculate
the average percentage of positions that are the same between the (n * (n-1)) / 2 sets of substrings
taken amongst the given n substrings. It can happen that some substrings are duplicate but since their
ranks are not the same in s they are considered as different substrings.
________________________
Example:
Given string s = "444996, 699990, 666690, 096904, 600644, 640646, 606469, 409694, 666094, 606490"
composing a set of n = 10 substrings (hence 45 combinations), pos_average -> return 29.2592592593.
"""


def count_coincidences(elem1, elem2):
    return sum(1 for char1, char2 in zip(elem1, elem2)
               if char1 == char2)


def coincid_with_remaining_arr_elem(arr_elem, idx, arr):
    coincidences = 0
    for i in range(idx, len(arr)):
        coincidences += count_coincidences(arr_elem, arr[i])
    return coincidences


def pos_average(s):
    arr = s.split(", ")
    coincidences = 0
    combos = (len(arr) * (len(arr)-1)) / 2
    positions = combos * len(arr[0])
    for idx, arr_elem in enumerate(arr):
        coincidences += coincid_with_remaining_arr_elem(arr_elem, idx + 1, arr)
    return coincidences / positions * 100


# Test
print(f"Expected: {26.6666666667}, "
      f"Current: {pos_average('466960, 069060, 494940, 060069, 060090, 640009, 496464, 606900, 004000, 944096')}")
print(f"Expected: {29.2592592593}, "
      f"Current: {pos_average('444996, 699990, 666690, 096904, 600644, 640646, 606469, 409694, 666094, 606490')}")