"""
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""

def solution(s):
    copied = list(s)
    answer = []

    while len(copied):
        if ord(copied[0]) >= 65 and ord(copied[0]) <= 90:
            answer.append(" " + copied[0])
        else:
            answer.append(copied[0])
        del copied[0]

    return "".join(answer)
