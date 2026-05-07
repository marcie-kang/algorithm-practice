"""
Write a function that outputs the transpose of a matrix - a new matrix where the columns and rows of the original are swapped.

For example, the transpose of:

| 1 2 3 |
| 4 5 6 |
is

| 1 4 |
| 2 5 |
| 3 6 |
The input to your function will be an array of matrix rows. You can assume that each row has the same length, and that the height and width of the matrix are both positive.
"""

#first solution
def transpose1(matrix):
    if not matrix:
        return []

    result = []

    for outer_idx in range(len(matrix[0])):
        new_value = []

        for inner_idx in range(len(matrix)):
            new_value.append(matrix[inner_idx][outer_idx])

        result.append(new_value)

    return result

#second solution
def transpose2(matrix):
    return list(map(list, zip(*matrix)))
