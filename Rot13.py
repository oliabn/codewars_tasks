"""
Task: Rot13
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters
after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13.
If there are numbers or special characters included in the string,
they should be returned as they are.
Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""


def rot13(message):
    encode_list = str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM")
    return message.translate(encode_list)


# test
print(rot13('test'))                        # expected result 'grfg'
print(rot13('aA bB zZ 1234 *!?%'))          # expected result 'nN oO mM 1234 *!?%'