"""
Given a string, remove any characters that are unique from the string.

Example:

input: "abccdefee"

output: "cceee"
"""

def only_duplicates(st):
    return "".join([char for char in st if st.count(char) > 1])
