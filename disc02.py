def make_keeper(n):
    def keeper(cond):
        i = 1
        while i <= n:
            cond(i) and print(i)
    return keeper

def referential_make_keep(n):
    def keeper(cond):
        i = 1
        while i<= n:
            cond(i) and print(i)
            return keeper
    return keeper

def print_delayed(x):
    """ Return a new function.
        This new function, when called, will print out x
        and return another function with the same behavior.
    >>> f = print_delayed(1)
    >>> f = f(2)
    1
    >>> f = f(3)
    2
    >>> f = f(4)(5)
    3
    4
    >>> f("hi") # a function is returned
    5
    <function delay_print>
    """
    def delay_print(y):
        print(x)
        return print_delayed(y)
    return delay_print

def print_n(n):
    def inner_print(x):
        if  n == 0:
            print("done")
        else:
            print(x)
        return print_n(n - 1)
    return inner_print
