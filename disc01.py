def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    isCold = temp < 60

    if (isCold or raining):
        return True
    else:
        return False

def special_case():
    """
    >>> special_case()
    12
    """

    x = 10
    if x > 0:
        x += 2
    elif x < 13:
        x += 3
    elif x % 2 == 1:
        x += 4
    return x

def just_in_case():
    """
    >>> just_in_case()
    19
    """

    x = 10
    if x > 0:
        x +=2
    if x < 13:
        x +=3
    if x % 2 == 1:
        x += 4
    return x

def case_in_point():
    """
    >>> case_in_point()
    12
    """
    x = 10

    if x > 0:
        return x + 2
    if x < 13:
        return x + 3
    if x % 2 == 1:
        return x + 4
    return x

def so_slow(num):
    """
    causes an infinite loop
    """

    x = num
    while x > 0:
        print(x)
        x = x + 1
    return x / 0

def square(x):

    print("here!")
    return x * x

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """

    x = 2

    while x < n:
        if n % x == 0:
            return False
        x += 1

    return True

def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result == None
    True
    """
    x = 1

    while x <= n:
        if x % 5 == 0 and x % 3 == 0:
            print("fizzbuzz")
        elif x % 3 == 0:
            print("fizz")
        elif x % 5 == 0:
            print("buzz")
        else:
            print(x)

        x += 1
