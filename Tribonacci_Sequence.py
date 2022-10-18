"""
Task: Tribonacci Sequence
Fibonacci bigger brother, AKA Tribonacci)

As the name may already reveal, it works basically like a Fibonacci,
but summing the last 3 (instead of 2) numbers of the sequence to generate the next.
You need to create a fibonacci function that given a signature list,
returns the first n elements - signature included of the so-seeded sequence.

- signature will always contain 3 numbers;
- n will always be a non-negative number;
- if n == 0, then return an empty array.
"""


def tribonacci(trib_list, n):
    for i in range(2, n - 1):
        trib_list.append(sum(trib_list[-3:]))
    return trib_list[:n]


# Test
print(f"Expected res: {[1, 1, 1, 3, 5, 9, 17, 31, 57, 105]}. Current res: {tribonacci([1, 1, 1], 10)}")
print(f"Expected res: {[1]}. Current res: {tribonacci([1, 1, 1], 1)}")
print(f"Expected res: {[]}. Current res: {tribonacci([1, 1, 1], 0)}")