"""The very first module in a more structured version of the project.
"""


# Moving code from main.py
def print_year():
    """Prints the year of John Lennon's birth.
    """
    print(1940)


# Taking care of the module __name__
if __name__ == '__main__':

    # Printing with ' ' and printing without '\n'
    print('John Lennon', '\nwas born in', str(1940) + '.')
    print('John Lennon ', end='')
    print('was born in 1940.')
    print()

    # Printing with classical formatting (%)
    print('An int: %4d, a float: %6.2f, a string: %s.' % (23, 45.5, 'John'))
    print()

    # Keyboard input
    year = input('Read the year when John was born: ')
    print(year)
    print()

    # break and continue
    for i in range(5):
        if i == 3:
            # continue
            break
        print(i)
    print()

    # Printing docstrings
    print(__doc__)
    print(__name__)
    print(print_year.__doc__)
    print()

    # Importing from Standard Library
    from datetime import date
    date_of_birth = date(1940, 10, 9)
    print(date_of_birth)
    preferred_date_format = '%b %d, %Y'
    print(date_of_birth.strftime(preferred_date_format))
