"""Demonstrates working with lists.
"""


def demonstrate_lists():
    """Using just the simplest operations with lists.
    - create a non-empty list with different kinds of elements
    - accessing/slicing a list
    - comparing 2 lists (== vs. is)
    - concatenating 2 lists (the + operator)
    - looping through a list
    """

    john = ['John Lennon', 1940, True]
    print(john)
    print(john[0])
    print(john[-2:])
    print(john + ['Paul McCartney', 'Liverpool'])
    for e in john:
        print(e)


def demonstrate_list_methods():
    """Using
    append()
    insert()
    remove()
    pop()
    extend()
    count()
    index()
    reverse()
    len()
    ...
    Also, "in" and "not in" operators can be used to search lists
    for the occurrence of a given element.
    """

    john = ['John Lennon', 1940, True]
    # john.append('Liverpool')
    # print(john)
    print(john.append('Liverpool'))
    print(john)
    john.insert(2, 'The Beatles')
    print(john)
    john.remove(1940)
    print(john)
    del john[True]
    print(john)
    john.extend(['Paul McCartney', 'The Beatles'])
    print(john)
    john.append('Liverpool')
    print(john)
    print(john.count('Liverpool'))
    print(john.index('Liverpool'))
    john.reverse()
    print(john)


def demonstrate_arrays():
    """Using array.array() to build list-based numeric arrays.
    Demonstrating that lists and arrays are different types.
    """

    from array import array
    a = array('i', [4, 2, 8, 9])
    print(a)
    print(type(a))
    l = [4, 2, 8, 9]
    print(l)
    print(type(l))


def populate_empty_list():
    """Creating an empty list and populating it with random values
    using random.seed() and random.randint()
    """

    from random import randint, seed
    seed(56)
    l = []
    for i in range(100):
        l.append(randint(0, 100))
    print(l[34:56])


def duplicate_list():
    """Duplicating lists (carefully :)).
    Don't use l2 = l1, but either of the following:
    - l2 = l1.copy()
    - l2 = l1 + []
    - l2 = l1[:]
    """

    l1 = ['John', 'Paul', 'George', 'Ringo']
    l2 = l1                                     # just copying addresses, not creating another object
    print(str(id(l1)) + '\n' + str(id(l2)))     # the addresses are the same


def demonstrate_list_comprehension():
    """Showing examples of list comprehension.
    - list comprehension over an array.array()
    - list comprehension over a list of strings
    - list comprehension with enumerate(), to find indices of all occurrences of an element in a list
    Using str() and join() in printing results.
    """

    from array import array
    a = array('i', [4, 2, 8, 9])
    l = [i for i in a]
    print(l)
    l = [str(i) for i in a]
    print(l)
    print()

    john = ['John', 'Lennon', 'Liverpool']
    l = [s for s in john]
    print(l)
    print(', '.join(s for s in john))
    print(', '.join(john))
    print()

    songs = ['Imagine a Man', 'There\'s a Place', 'No Expectations', 'Heaven is a Place on Earth']

    first_words = [words[0] for words in [title.split() for title in songs]]
    print(first_words)
    print(' '.join(first_words))
    lyric = [first_words[0]] + [word.lower() for word in first_words[1:]]
    print(' '.join(lyric))
    print()

    songs = ['No Expectations', 'Imagine a Man', 'There\'s a Place', 'No Expectations', 'Heaven is a Place on Earth',
             'No Expectations', 'No Expectations', ]
    print([i for i, k in enumerate(songs) if k == 'No Expectations'])


if __name__ == '__main__':

    # demonstrate_lists()
    # demonstrate_list_methods()
    # demonstrate_arrays()
    # populate_empty_list()
    # duplicate_list()
    demonstrate_list_comprehension()
