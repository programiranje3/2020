"""Demonstrates details of writing Python functions: annotations, default args, kwargs
"""


def demonstrate_annotations(musician: str, year: int) -> str:

    """Demonstrates how to use annotations of
    function parameters/arguments (<arg>: <type>) and of function return type (def f(...) -> <type>:).
    - print the function parameters/arguments
    - print the value of the __annotations__ attribute of this function
    - print the name and the docstring of this function
    - return a formatted string (including function parameters/arguments)
    """

    # print(f'musician: {musician}, year: {year}')
    # print(locals())
    # a = 4
    # print(locals())
    # print()

    print(demonstrate_annotations.__annotations__)
    print(demonstrate_annotations.__doc__)
    return f'Function {demonstrate_annotations.__name__}, parameters: {musician}, {year}'


def show_musician(name, year=1940, city='Liverpool'):
    """Demonstrates default arguments/parameters.
    - print the function arguments/parameters in one line
    """

    print(f'{name}, {year}, {city}')


def use_flexible_arg_list(band_name: str, *members):
    """Demonstrates flexible number of arguments/parameters.
    - print the band name and the list of band members in one line
    """

    # print(members)
    m_str = ', '.join(members) if members else ''
    print(f'{band_name}: {m_str}' if members else f'{band_name}')


def use_all_categories_of_args(band, *members, year=1962, **music_details):
    """Demonstrates positional args, flexible args, keyword args, and kwargs (flexible keyword args).
    - print all arguments/parameters, including the keyword arguments/parameters, in one line
    """

    print(music_details)
    print()

    m_str = ', '.join(members) if members else ''
    kw_arg = [str(i) + ': ' + str(j) for i, j in music_details.items()]
    print(f'{band}: {m_str}' if members else f'{band}', end='')
    print(f' ({", ".join(kw_arg)})')


if __name__ == "__main__":

    john = 'John Lennon'
    paul = 'Paul McCartney'
    george = 'George Harrison'
    ringo = 'Ringo Starr'
    the_beatles = [john, paul, george, ringo]

    # demonstrate_annotations(john, 1940)
    # print(demonstrate_annotations(23, 1940))

    # show_musician(john)
    # show_musician(john, 1940)
    # show_musician(john, city='New York')
    # show_musician(john, city='New York', year=1971)
    # show_musician(city='New York', year=1971, john, )

    # use_flexible_arg_list('The Beatles', *the_beatles)
    # use_flexible_arg_list(ringo, 'The Beatles', john, paul)
    # use_flexible_arg_list('The Beatles')

    # use_all_categories_of_args('The Beatles', start=1962, end=1970)
    use_all_categories_of_args('The Beatles', *the_beatles, start=1962, end=1970, year=1970)


