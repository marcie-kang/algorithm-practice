"""
Task
You will receive an array as parameter that contains 1 or more integers and a number n.

Here is a little visualization of the process:

Step 1: Split the array in two:

[1, 2, 5, 7, 2, 3, 5, 7, 8]
      /            \
[1, 2, 5, 7]    [2, 3, 5, 7, 8]
Step 2: Put the arrays on top of each other:

   [1, 2, 5, 7]
[2, 3, 5, 7, 8]
Step 3: Add them together:

[2, 4, 7, 12, 15]
Repeat the above steps n times or until there is only one number left, and then return the array.

Example
Input: arr=[4, 2, 5, 3, 2, 5, 7], n=2


Round 1
-------
step 1: [4, 2, 5]  [3, 2, 5, 7]

step 2:    [4, 2, 5]
        [3, 2, 5, 7]

step 3: [3, 6, 7, 12]


Round 2
-------
step 1: [3, 6]  [7, 12]

step 2:  [3,  6]
         [7, 12]

step 3: [10, 18]


Result: [10, 18]

[1, 2, 3, 4, 5]
[1] [2] [3, 4, 5]
[3, 4, 8]
[15]
"""

def split_and_add(numbers, n):
    if len(numbers) <= 1 or n == 0:
        return numbers

    mid = len(numbers) // 2
    left = numbers[:mid]
    right = numbers[mid:]

    left = [0] * (len(right) - len(left)) + left
    tokens_sum = [a + b for a, b in zip(left, right)]

    return split_and_add(tokens_sum, n - 1)
