"""
Description:
Complete the method so that it formats the words into a single comma separated value. The last word should be separated by the word 'and' instead of a comma. The method takes in an array of strings and returns a single formatted string.

Note:

Empty string values should be ignored.
Empty arrays or null/nil/None values being passed into the method should result in an empty string being returned.
Example: (Input --> output)

['ninja', 'samurai', 'ronin'] --> "ninja, samurai and ronin"
['ninja', '', 'ronin'] --> "ninja and ronin"
[] -->""
"""

def format_words(words):
    if len(words) == 0: return ""

    final_words = list(filter(None, words))
    result = final_words[0]

    for idx, word in enumerate(final_words[1:], start = 1):
        if idx != (len(final_words) - 1):
            result += ", " + word
        elif idx == (len(final_words) - 1):
            result += " and " + word

    return result

print(format_words(['ninja', 'samurai', 'ronin']))
print(format_words(['ninja', '', 'ronin']))
print(format_words(['', '', 'three']))
print(format_words([]))
