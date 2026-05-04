"""
Task
Create a function that accepts a string as an argument and validates whether the vowels (a, e, i, o, u) and consonants are in alternate order.

Examples
"amazon" --> true
"apple" --> false
"banana" --> true
Note
Arguments consist of only lowercase letters.
"""

def is_alt(s):
    vowels = set("aeiou")

    for index in range(len(s) - 1):
        if (s[index] in vowels) == (s[index + 1] in vowels):
            return False

    return True
