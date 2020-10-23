"""Demonstrates how operators and expressions work in Python.
"""

# from settings import *


def demonstrate_arithmetic_operators():
    """Working with arithmetic operators.
    Arithmetic operators in Python are pretty much the same as in other programming languages.
    The integer division operator: //
    """

    print((13 // 4) % 2 - 12)


def demonstrate_relational_operators():
    """Working with relational operators.
    - simple comparisons
    - comparing dates (== vs. is)
    - comparing dates (>, <, etc. with dates)
    - None in comparisons, type(None)
    """

    # - simple comparisons
    if 13 > 19:
        print(True)
    else:
        print(False)
    print()

    # - comparing dates (== vs. is)
    from datetime import date
    d1 = date(1940, 10, 9)
    d2 = date.today()
    if d1 > d2:
        print(True)
    else:
        print(False)
    print()

    if id(d1) == id(d2):
        print(True)
    else:
        print(False)
    print()

    print(id(d1))
    print(id(d2))
    print()

    # - comparing dates (>, <, etc. with dates)
    # - None in comparisons, type(None)

    print(type(None))
    # print(d1 > None)


def demonstrate_logical_operators():
    """Working with logical operators.
    - logical operations with True, False and None
    - logical operations with dates
    - logical operations with None (incl. None and int, None and date, etc.)
    - None and date vs. None > date
    """

    # - logical operations with True, False and None
    from datetime import date
    d1 = date(1940, 10, 9)
    d2 = date.today()

    if True or False:
        print(True)
    else:
        print(False)
    print()
    if None and d1:
        print(True)
    else:
        print(False)
    print()
    if d2 and d1:
        print(True)
    else:
        print(False)
    print()
    print(d1 or d2)
    print()

    # - logical operations with dates
    # - logical operations with None (incl. None and int, None and date, etc.)
    # - None and date vs. None > date
    if None or d1:
        print(True)
    else:
        print(False)


if __name__ == '__main__':

    # demonstrate_arithmetic_operators()
    # demonstrate_relational_operators()
    demonstrate_logical_operators()

