"""
Re-order the characters of a string, so that they are concatenated into a new string in "case-insensitively-alphabetical-order-of-appearance" order. Whitespace and punctuation shall simply be removed!

The input is restricted to contain no numerals and only words containing the english alphabet letters.

Example:

alphabetized("The Holy Bible") # "BbeehHilloTy"
Inspired by Tauba Auerbach
"""

def alphabetized(s):
    char_list = [(char, index, ord(char)) for index, char in enumerate(s) if char.strip() and char.isalpha()]
    sorted_list = sorted(char_list, key = lambda x: (x[0].lower(), x[1]))

    return "".join([item[0] for item in sorted_list])
