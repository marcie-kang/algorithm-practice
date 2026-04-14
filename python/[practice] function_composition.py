"""
apply_twice(f, x)  →  f(f(x))

# 예시
apply_twice(lambda x: x + 3, 7)  →  13
"""

def apply_twice(f, x):
    return f(f(x))

"""
double = make_multiplier(2)
double(5)   →  10
double(8)   →  16

triple = make_multiplier(3)
triple(5)   →  15
"""

def make_multiplier(input):
    def multiplier(arg):
        return arg * input

    return multiplier

"""
add3 = lambda x: x + 3

apply_n_times(add3, 4)(10)  →  22
# 10 → 13 → 16 → 19 → 22

apply_n_times(add3, 0)(10)  →  10  # 0번이면 그대로
"""

def apply_n_times(func, times):
    def apply(input):
        result = input

        for time in range(times):
            result = func(result)
        return result

    return apply

"""
chained([a, b, c, d])(10)
"""

def chained(functions):
    def func(input):
        result = input

        for function in functions:
            result = function(result)

        return result
    return func

"""
add5 = make_adder(5)
add5(3)   →  8
add5(10)  →  15

add100 = make_adder(100)
add100(1)  →  101
"""

def make_adder(input):
    def adder(arg):
        return arg + input
    return adder

"""
counter = make_counter()
counter()  →  1
counter()  →  2
counter()  →  3

# if new function is made, it starts from 0 again
counter2 = make_counter()
counter2()  →  1
"""

def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

def make_counter_from(arg):
    count = arg

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

"""
acc = make_accumulator()
acc(5)   →  5
acc(3)   →  8
acc(10)  →  18
acc(2)   →  20
"""

def make_accumulator():
    total = 0

    def accumulator(input):
        nonlocal total
        total += input

        return total

    return accumulator

"""
logger = make_logger()
logger(5)        →  [5]
logger("hello")  →  [5, "hello"]
logger(True)     →  [5, "hello", True]
"""

def make_logger():
    inputs = []

    def logger(input):
        inputs.append(input)
        return inputs

    return logger

"""
add5 = make_once(lambda x: x + 5)

add5(10)  →  15
add5(20)  →  15  # 두 번째부터는 처음 결과 그대로
add5(99)  →  15
"""

def make_once(function):
    result = None
    called = False

    def inner_function(input):
        nonlocal result, called

        if not called:
            result = function(input)
            called = True

        return result

"""
slow_double = make_memoize(lambda x: x * 2)

slow_double(5)   →  10  # 처음 계산
slow_double(3)   →  6   # 처음 계산
slow_double(5)   →  10  # 저장된 값 반환 (다시 계산 안 함)
slow_double(3)   →  6   # 저장된 값 반환
"""

def make_memoize(function):
    cache = {}

    def memoize(input):
        if input not in cache:
            cache[input] = function(input)

        return cache[input]

    return memoize
