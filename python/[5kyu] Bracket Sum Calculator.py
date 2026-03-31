"""
Given a string expression, calculate the total sum where numbers inside brackets are multiplied by the number following the closing bracket.
"2(3)2"        -->  8    # 2 + (3)*2 = 8
"1(2 3)2"      -->  11   # 1 + (2+3)*2 = 11
"(1 2)(3)2"    -->  9    # (1+2) + (3)*2 = 9
"2((1 2)2)3"   -->  20   # 2 + ((1+2)*2)*3 = 20

Rules
- Numbers are single digits only
- If no number follows a closing bracket, treat it as multiplier 1
- Brackets can be nested
- A space between numbers means addition
"""

def check_digit(idx, str, top):
    if idx + 1 < len(str) and str[idx + 1].isdigit():
        idx += 1
        return idx, sum(top) * int(str[idx])

    return idx, sum(top)

def bracket_sum_cal(str):
    copied = str[:].replace(" ", "")
    stack = [[]]
    index = 0

    while index < len(copied):
        current = copied[index]

        if current in ")":
            top = stack.pop()
            index, result = check_digit(index, copied, top)
            stack[-1].append(result)

        if current.isdigit():
            stack[-1].append(int(current))

        if current in "(":
            stack.append([])

        index += 1

    return sum(stack[0])
