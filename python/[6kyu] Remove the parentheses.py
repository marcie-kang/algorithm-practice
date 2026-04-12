"""
Remove the parentheses
In this kata you are given a string for example:

"example(unwanted thing)example"
Your task is to remove everything inside the parentheses as well as the parentheses themselves.

The example above would return:

"exampleexample"
Notes
Other than parentheses only letters and spaces can occur in the string. Don't worry about other brackets like "[]" and "{}" as these will never appear.
There can be multiple parentheses.
The parentheses can be nested.
"""

def remove_parentheses(st):
    result = []
    stack = []

    for current in st:
        if current == "(":
            stack.append("(")
        elif current == ")" and stack:
            stack.pop()
        elif len(stack) == 0:
            result.append(current)

    return "".join(result)

print(remove_parentheses("example(unwanted thing)example"))
