"""
Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'
"""

def solution(string):
    result = ""

    for i in range(len(string) - 1, -1, -1):
        result += string[i]

    return result

print(solution("world"))
