"""
Create a function which takes a string as input and returns an array containing the characters in the string whose binary representation of their ASCII code has more zeroes than ones.

The returned array must not contain duplicate characters. Only the first occurrence of each character in the input should be included, keeping the order of appearance.

All input will be valid strings of length > 0. Leading zeroes in binary should not be counted.

Examples
input = 'abcdea'

characters = [
     'a',     'b',        'c',       'd',       'e',       'a'
]
ascii codes = [
    97,       98,         99,        100,       101,       97
]

binary = [
  0b1100001, 0b1100010, 0b1100011, 0b1100100, 0b1100101, 0b1100001
]

has more zeroes than ones = [
    true,      true,      false,     true,      false,      true
]

result = [
    'a',        'b',                 'd'                  // duplicate character
]

'DIGEST'--> ['D','I','E','T']
"""
from collections import Counter

def more_zeros(s):
    seen = set()
    result = []

    for char in s:
        binary = format(ord(char), "b")
        if Counter(binary)["0"] > Counter(binary)["1"]:
            if char not in seen:
                seen.add(char)
                result.append(char)

    return result
