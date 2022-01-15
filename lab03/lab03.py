HW_SOURCE_FILE = __file__
from functools import reduce


def summation(n, term):
    """Return the sum of numbers 1 through n (including n) wíth term applied to each number.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    "*** YOUR CODE HERE ***"
    if (n == 1):
        return term(n)
    else:
        return summation(n - 1, term) + term(n)




def generate_pascal_triangle(n):
    triangle = []

    for j in range(n + 1):
        row = []
        for i in range(j + 1):
            has_row_above = j > 0

            if has_row_above:
                row_above = triangle[j - 1]

                has_value_above_left = i > 0
                has_value_directly_above = i < j

                value_above_left = row_above[i -
                                             1] if has_value_above_left else 0
                value_directly_above = triangle[j -
                                                1][i] if has_value_directly_above else 0

                value = value_directly_above + value_above_left
            else:
                value = 1

            row.append(value)
        triangle.append(row)

    return triangle

def pretty_print_pascal_triangle(triangle):
    for row in triangle:
        pretty_row = reduce(lambda acc, val:  acc + str(val), row, '')
        print(pretty_row)


def pascal(j, i):
    """Returns the value of the item in Pascal's Triangle 
    whose position is specified by row and column.
    >>> pascal(0, 0)
    1
    >>> pascal(0, 5)	# Empty entry; outside of Pascal's Triangle
    0
    >>> pascal(3, 2)	# Row 3 (1 3 3 1), Column 2
    3
    >>> pascal(4, 2)     # Row 4 (1 4 6 4 1), Column 2
    6
    """
    "*** YOUR CODE HERE ***"
    if (i > j or i < 0):
        return 0
    elif (j == 0):
        return 1
    else:
        return pascal(j - 1, i) + pascal(j - 1, i - 1)

def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
