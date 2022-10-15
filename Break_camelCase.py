"""
Complete the solution so that the function will break up camel casing,
using a space between words.
"camelCasing"  =>  "camel Casing"
"""


def break_camel_case(s):
    return "".join((" " + char) if char.isupper() else char for char in s).strip()


#test
print(break_camel_case("breakCamelCase"))       # expected result: break Camel Case
print(break_camel_case("Camel"))                # expected result: Camel
print(break_camel_case("camel"))                # expected result: camel
