"""
Task: Roman Numerals Encoder
Create a function taking a positive integer as its parameter
and returning a string containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately
starting with the left most digit and skipping any digit with a value of zero.

In Roman numerals is rendered:
1990      --->     1000=M, 900=CM, 90=XC;      --->     resulting in MCMXC.
2008      --->     2000=MM, 8=VIII;     --->     MMVIII.
1666      --->      MDCLXVI.
"""


def roman(n):
    units = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thousands = ["", "M", "MM", "MMM", "MMMM"]
    return thousands[n // 1000] + hundreds[n // 100 % 10] + tens[n // 10 % 10] + units[n % 10]


print(roman(246))     # expected result: CCXLVI
print(roman(2421))    # expected result: MMCDXXI
print(roman(984))     # expected result: CMLXXXIV
print(roman(21))     # expected result: XXI