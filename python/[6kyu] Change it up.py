"""
Create a function that takes a string as a parameter and does the following, in this order:

Replaces every letter with the letter following it in the alphabet (see note below)
Makes any vowels capital
Makes any consonants lower case
Note:

the alphabet should wrap around, so Z becomes A
in this kata, y isn't considered as a vowel.
So, for example the string "Cat30" would return "dbU30" (Cat30 --> Dbu30 --> dbU30)
"""

def changer(s):
    result = ""
    vowels = "aeiou"

    for char in s:
        if char == '{':
            result += 'A'
            continue

        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')

            shifted_char = chr((ord(char) - start + 1) % 26 + start)

            if shifted_char.lower() in vowels:
                result += shifted_char.upper()
            else:
                result += shifted_char.lower()
        else:
            result += char

    return result
