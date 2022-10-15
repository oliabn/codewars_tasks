"""
Task: Estimating Amounts of Subsets
Given a set of elements (integers or string characters, characters only in RISC-V),
where any element may occur more than once, return the number of subsets
that do not contain a repeated element.

Let's see with an example: set numbers = {1, 2, 3, 4}
{{1}, {2}, {3}, {4}, {1,2}, {1,3}, {1,4}, {2,3}, {2,4}, {3,4}, {1,2,3}, {1,2,4}, {1,3,4}, {2,3,4}, {1,2,3,4}}
est_subsets([1, 2, 3, 4]) = 15
"""

from math import comb


# comb(n, k) - Find the total number of possibilities to choose k things from n items


def est_subsets(arr):
    arr = set(arr)
    n = len(arr)
    nCk = 0                     # Combinations k things from n items
    for k in range(1, n + 1):
        nCk += comb(n, k)
    return nCk


# test
print(est_subsets([1, 2, 3, 4]))  # expected result: 15
