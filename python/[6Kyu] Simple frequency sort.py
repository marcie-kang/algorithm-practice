"""
In this kata, you will sort elements in an array by decreasing frequency of elements. If two elements have the same frequency, sort them by increasing value.

solve([2,3,5,3,7,9,5,3,7]) = [3,3,3,5,5,7,7,2,9]
-- We sort by highest frequency to lowest frequency.
-- If two elements have same frequency, we sort by increasing value.
More examples in test cases.

Good luck!
"""

def solve(arr):
    unique_numbers = set(arr)
    number_count = [[number, arr.count(number)] for number in unique_numbers]
    sorted_count = sorted(number_count, key = lambda x: ([-x[1], x[0]]))

    return sum([[number] * count for number, count in sorted_count], [])
