"""
Task
Given a list of positive integers, determine the minimum non-negative integer that needs to be inserted so that the sum of all elements becomes a prime number.

Notes
The list will always have at least 2 elements.
All elements will be positive integers (n > 0).
The list may contain duplicate values.
The new sum must be the closest prime number that is greater than or equal to the current sum.
Examples
[3, 1, 2] ==> Should return 1
Explanation: The sum is 6
The closest prime greater than or equal to 6 is 7
We need to add 1 to make the sum 7 (a prime)

[2, 12, 8, 4, 6] ==> Should return 5
Explanation: The sum is 32
The closest prime greater than or equal to 32 is 37
We need to add 5 to make the sum 37 (a prime)

[50, 39, 49, 6, 17, 28] ==> Should return 2
Explanation: The sum is 189
The closest prime greater than or equal to 189 is 191
We need to add 2 to make the sum 191 (a prime)
For more challenges, check out Playing with Numbers Series.

Enjoy coding!
"""

def is_prime(n):
    if n < 2:
        return False

    if n < 4:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5

    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False

        i += 6

    return True

def minimum_number(numbers):
    num_sum = sum(numbers)
    min_prime = num_sum

    while not is_prime(min_prime):
        min_prime += 1

    return min_prime - num_sum
