def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    result = 1
    min = n - k

    while n > min:
        result = n * result
        n = n - 1

    return result



def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    result = 0
    while y > 0:
        quotient = y // 10
        remainder = y % 10
        y = quotient
        result = result + remainder
    return result


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"

# WWPD Exercises (What Would Python Display)
def xk(c, d):
    """
    Fill in the output
    >>> xk(10, 10)
    23
    >>> xk(10, 6)
    23
    >>> xk(4, 6)
    17
    >>> xk(0, 0)
    25
    """
    if c == 3:
        return 6
    elif d >= 4:
        return 6 + 7 + c
    else:
        return 25

def how_big(x):
    """
    Fill in the output
    >>> how_big(7)
    'big'
    >>> how_big(12)
    huge
    >>> how_big(1)
    small
    >>> how_big(-1)
    nothin
    """
    if x > 10:
        print('huge')
    elif x > 5:
        return 'big'
    elif x > 0:
        print('small')
    else:
        print('nothin')
