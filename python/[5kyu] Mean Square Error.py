"""
Complete the function that

accepts two integer arrays of equal length
compares the value each member in one array to the corresponding member in the other
squares the absolute value difference between those two values
and returns the average of those squared absolute value difference between each member pair.
Examples
[1, 2, 3], [4, 5, 6]              -->   9   because (9 + 9 + 9) / 3
[10, 20, 10, 2], [10, 25, 5, -2]  -->  16.5 because (0 + 25 + 25 + 16) / 4
[-1, 0], [0, -1]                  -->   1   because (1 + 1) / 2
"""

#solution1
def solution1(a, b):
    value_differences = []

    for i in range(len(a)):
        difference = (b[i]-a[i]) ** 2
        value_differences.append(difference)

    return sum(value_differences) / len(a)

#solution2
def solution2(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b)) / len(a)