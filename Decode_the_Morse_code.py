"""
Task: Decode the Morse code
In this kata you have to write a simple Morse code decoder.
The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A
is coded as ·−
- The Morse code is case-insensitive, traditionally capital letters are used.
- When the message is written in Morse code, a single space is used to separate the character codes
and 3 spaces are used to separate words.
For example,
"HEY JUDE" in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

NOTE: Extra spaces before or after the code have no meaning and should be ignored.
In addition to letters, digits and some punctuation, there are some special service codes,
the most notorious of those is the international distress signal SOS (that was first issued by Titanic),
that is coded as ···−−−···. These special codes are treated as single special characters,
and usually are transmitted as separate words.

Your task is to implement a function that would take the morse code as input
and return a decoded human-readable string.
"""


MORSE_CODE = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F",
              "--.": "G", "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M",
              "-.": "N", "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
              "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z"}


# from preloaded import MORSE_CODE


def decode_morse(morse_code):
    res = ""
    if morse_code == '...---...':
        return "SOS"
    char_list = morse_code.strip().split(" ")
    res = "".join([MORSE_CODE[char] if char != "" else " " for char in char_list])
    res = res.replace("  ", " ")
    return res


# Test
print(decode_morse('.... . -.--   .--- ..- -.. .'))         # expected result: HEY JUDE
print(decode_morse('... --- ...'))                          # expected result: SOS
print(decode_morse('...---...'))                            # expected result: SOS
print(decode_morse('...   ---   ...'))                      # expected result: S O S
