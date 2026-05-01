"""
Find the sum of the digits of all the numbers from 1 to N (both ends included).

Examples
# N = 4
1 + 2 + 3 + 4 = 10

# N = 10
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) = 46

# N = 12
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) + (1 + 1) + (1 + 2) = 51
"""

def compute_sum(n):
    total = 0

    for number in range(1, n + 1):
        if len(str(number)) == 1:
            total += number
        else:
            total += sum(int(operator) for operator in str(number))

    return total
