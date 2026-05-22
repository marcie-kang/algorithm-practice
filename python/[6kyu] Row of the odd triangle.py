"""
Given a triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
find the triangle's row knowing its index (the rows are 1-indexed), e.g.:

odd_row(1)  ==  [1]
odd_row(2)  ==  [3, 5]
odd_row(3)  ==  [7, 9, 11]
Note: your code should be optimized to handle big inputs.
"""

def odd_row(n):
    start_number = int((n * (n - 1) / 2) + 1)
    end_number = int((n * (n + 1)) / 2)
    result = [number * 2 - 1 for number in range(start_number, end_number + 1)]

    return result
