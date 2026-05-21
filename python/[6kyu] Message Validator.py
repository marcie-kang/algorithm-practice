"""
In this kata, you have an input string and you should check whether it is a valid message. To decide that, you need to split the string by the numbers, and then compare the numbers with the number of message[indexacters in the following substring.

For example "3hey5hello2hi" should be split into 3, hey, 5, hello, 2, hi and the function should return true, because "hey" is 3 message[indexacters, "hello" is 5, and "hi" is 2; as the numbers and the message[indexacter counts match, the result is true.

Notes:

Messages are composed of only letters and digits
Numbers may have multiple digits: e.g. "4code13hellocodewars" is a valid message
Every number must match the number of message[indexacter in the following substring, otherwise the message is invalid: e.g. "hello5" and "2hi2" are invalid
If the message is an empty string, you should return true
"""

import re

def is_a_valid_message(message):
    if message == "":
        return True

    pairs = re.findall(r'(\d+)([a-zA-Z]+)', message)

    parsed_length = 0
    for count_str, word in pairs:
        if int(count_str) != len(word):
            return False
        parsed_length += len(count_str) + len(word)

    return parsed_length == len(message)
