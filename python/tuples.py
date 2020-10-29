"""Demonstrates tuples
"""


def demonstrate_tuples():
    """Creating and using tuples.
    - create and print 1-tuple, 2-tuple, mixed-type n-tuple
    - accessing elements of a tuple using []
    - demonstrate that tuples are immutable
    """

    # t0 = ()
    # print(type(t0))
    # print(t0)
    # t1 = (3, )
    # print(type(t1))
    # print(t1)
    # t2 = 'John', 1940
    # print(type(t2))
    # print(t2)
    # t4 = 'John', 1940, 'Liverpool', 'UK'
    # print(type(t4))
    # print(t4)
    # print()

    t4 = 'John', 1940, 'Liverpool', 'UK'
    print(t4[0:3])
    # t4[0] = 'Lennon'
    print()


def demonstrate_zip():
    """Using the built-in zip() function with tuples and double-counter for-loop.
    """

    john = ('John Lennon', 1940, 'Liverpool')
    paul = ('Paul McCartney', 1942, 'Liverpool')
    george = ('George Harrison', 1944, 'Liverpool')
    ringo = ('Ringo Starr', 1940, 'Liverpool')

    the_beatles_zip = zip(john, paul, george, ringo)
    print(the_beatles_zip)
    print()

    for j, p, g, r in the_beatles_zip:
        print(j, p, g, r)
    print()

    the_beatles_zip = zip(john, paul, george, ringo)
    for i in the_beatles_zip:
        print(i)


def demonstrate_packing():
    """Packing and unpacking tuples.
    """

    john = ('John Lennon', 1940, 'Liverpool')
    paul = ('Paul McCartney', 1942, 'Liverpool')
    george = ('George Harrison', 1944, 'Liverpool')
    ringo = ('Ringo Starr', 1940, 'Liverpool')

    the_beatles = john, paul, george, ringo
    print(the_beatles)
    print()

    j, p, g, r = the_beatles
    print(r)


if __name__ == '__main__':

    # demonstrate_tuples()
    # demonstrate_zip()
    demonstrate_packing()
