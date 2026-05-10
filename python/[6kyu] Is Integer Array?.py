"""
Write a function that:

returns true  / True if every element in an array is an integer or a float with no decimals.
returns true  / True if array is empty.
returns false / False for every other input.
"""

def check_item(item):
    if isinstance(item, bool):
        return False
    if not isinstance(item, (int, float)):
        return False
    if isinstance(item, float) and not item.is_integer():
        return False

    return True

def is_int_array(arr):
    if not isinstance(arr, list):
        return False

    return all(check_item(item) for item in arr)
