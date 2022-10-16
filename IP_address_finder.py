"""
Task: IP address finder [Code-golf]

- !Code length <= 59 characters
- !import is forbidden as a part of anti-cheat

You are given a string representing a website's address.
To calculate the IP4 address you must convert all the characters into ASCII code,
then calculate the sum of the values.
- 1 part of the IP number will be the result mod 256
- 2 part of the IP number will be the double of the sum mod 256
- 3 will be the triple of the sum mod 256
- 4 will be the quadruple of the sum mod 256

"www.codewars.com"  --->  [88, 176, 8, 96]
"""

f = lambda u: [i*sum(map(ord, u)) % 256 for i in (1,2,3,4)]

print(f("www.codewars.com"))    # expected result: [88, 176, 8, 96]
print(f('www.starwiki.com'))    # expected result: [110, 220, 74, 184]
print(f('www.winnerss.win'))    # expected result: [136, 16, 152, 32]