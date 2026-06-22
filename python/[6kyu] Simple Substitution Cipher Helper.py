"""
A simple substitution cipher replaces one character from an alphabet with a character from an alternate alphabet, where each character's position in an alphabet is mapped to the alternate alphabet for encoding or decoding.

E.g.

map1 = "abcdefghijklmnopqrstuvwxyz";
map2 = "etaoinshrdlucmfwypvbgkjqxz";

cipher = Cipher(map1, map2);
cipher.encode("abc") # => "eta"
cipher.encode("xyz") # => "qxz"
cipher.encode("aeiou") # => "eirfg"

cipher.decode("eta") # => "abc"
cipher.decode("qxz") # => "xyz"
cipher.decode("eirfg") # => "aeiou"
If a character provided is not in the opposing alphabet, simply leave it as be.
"""

class Cipher:
    def __init__(self, map1, map2):
        self.map1 = map1
        self.map2 = map2
        self.result = ""

    def encode(self, string):
        return transformer(string, self.map1, self.map2)

    def decode(self, string):
        return transformer(string, self.map2, self.map1)

    def transformer(self, string, source, target):
        result = ""

        for char in string:
            if char not in source:
                result += char
                continue

            index = source.find(char)
            result += target[index]

        return result
