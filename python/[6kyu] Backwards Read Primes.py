"""
Backwards-read-primes are primes that when read backwards in base 10 (from right to left) are a different prime. (This rules out primes which are palindromes.)

Examples:

13 17 31 37 71 73
13 is such because it's prime and read from right to left writes 31 which is prime too. Same for the others.

Task
Find all Backwards-read-primes between two positive given numbers (both inclusive), the second one always being greater than or equal to the first one. The resulting array or the resulting string will be ordered following the natural order of the prime numbers.

Examples (in general form):
(start = 2, end = 100) => [13, 17, 31, 37, 71, 73, 79, 97]
(start = 9900, end = 10000) => [9923, 9931, 9941, 9967]
(start = 501, end = 599) => []
See "Sample Tests" for your language.

Notes
Forth: Return only the first backwards-read prime between start and end or 0 if you don't find any
Ruby: Don't use the Prime class, it's disabled.
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

def cached_is_prime(n, prime_cache):
    if n not in prime_cache:
        prime_cache[n] = is_prime(n)

    return prime_cache[n]

def backwardsPrime(start, end):
    result = []
    prime_cache = {}

    for n in range(start, end + 1):
        if cached_is_prime(n, prime_cache):
            reversed_n = int(str(n)[::-1])

            if n != reversed_n and cached_is_prime(reversed_n, prime_cache):
                result.append(n)

    return result
