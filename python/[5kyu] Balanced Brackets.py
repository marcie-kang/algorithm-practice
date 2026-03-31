"""
Balanced Brackets
Given a string containing only brackets (), [], {}, return True if the brackets are balanced, False otherwise.
"([]{})"     -->  True
"([)]"       -->  False
"((("        -->  False
""           -->  True
"{[]}"       -->  True
"(]"         -->  False
Rules

Every opening bracket must have a matching closing bracket
Brackets must be closed in the correct order
Empty string is considered balanced
"""

def bracket_matcher(brackets):
    stack = []
    matching = {"]": "[", ")": "(", "}": "{"}

    for bracket in brackets:
        if bracket in matching:
            if stack and matching[bracket] == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            stack.append(bracket)

    return len(stack) == 0
