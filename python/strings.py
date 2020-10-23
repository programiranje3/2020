"""Demonstrates working with strings in Python.
"""

import string

import settings


def demonstrate_formatting():
    """Using classical formatting.
    - \n is the new line char
    - r'...' - raw formatting
    - using \"\"\"...\"\"\" for multi-line formatting
    - string "multiplication"
    - substrings / slicing
    - str() vs. repr() (usually the same, but with whitespace there is a difference)
    """

    # - \n is the new line char
    print('%d %.2f %s' % (34, 56.4, 'eee'))

    print('C:\nobody')

    # - r'...' - raw formatting
    print(r'C:\nobody')

    # - using \"\"\"...\"\"\" for multi-line formatting
    print("""John
Lennon
Paul
McCartney""")

    # - string "multiplication"
    print('Lennon   ' * 3)

    # - substrings / slicing
    print('John Lennon'[0:4])
    print('John Lennon'[-1])
    print('John Lennon'[-6:])

    # - str() vs. repr() (usually the same, but with whitespace there is a difference)
    print(str(12))
    print(repr(12))
    print(str(string.whitespace))
    print(repr(string.whitespace))


def demonstrate_fancy_formatting():
    """Using "fancy" formatting.
    - format strings like '{0}{1} {2}', '{0}{1} {2}, {3}', etc.
    """

    print('{} was born in {}, {}.'.format('John Lennon', 1940, 'Liverpool'))
    print('{0} was born in {1}, {2}.'.format('John Lennon', 1940, 'Liverpool'))
    print('{0} was born in {2}, {1}.'.format('John Lennon', 1940, 'Liverpool'))


def demonstrate_fancy_formatting_with_f_strings():
    """Using f-strings in formatting.
    - format strings like f'Some text {some var}, more text {another var}...', etc.
    """

    year = 1940
    john = 'John Lennon'
    birth_place = 'Liverpool'
    print(f'{john} was born in {year}, in {birth_place}.')


def demonstrate_string_operations():
    """Using different string operations.
    - endswith(), split(), center(), in (aka contains()), == (aka equals(), len(),...), strip() (lstrip(), rstrip())
    """

    john = 'John Lennon'
    print(john.endswith('Lennon'))
    words = john.split()
    for word in words:
        print(word)
    # words = john.split('n')
    # for word in words:
    #     print(word)
    print('nn' in john)
    print(len(john))
    print('      ' + john)
    print(('      ' + john).removeprefix('      '))
    print(john.center(30, '*'))


if __name__ == '__main__':

    # demonstrate_formatting()
    # demonstrate_fancy_formatting()
    # demonstrate_fancy_formatting_with_f_strings()
    demonstrate_string_operations()
