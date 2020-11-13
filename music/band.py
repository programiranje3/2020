"""The class representing the concept of a music group/band.
It includes a list of Musician objects (band members) and the date when the band started performing together.
"""

from datetime import date, datetime, time
import json

from music.musician import Musician
# from util.utility import format_date


class Band():
    """The class describing the concept of a music group/band.
    It includes a list of Musician objects (band members) and the date when the band started performing together.
    """

    # Class variables: like static fields in Java; typically defined and initialized before __init__()
    # Insert a class variable (static field), such as definition, date_pattern,...

    formed_phrase_approx = 'the band was formed in '
    formed_phrase_date = 'the band was formed on '
    formed_phrase_approx_still_together = 'the band has been formed in '
    formed_phrase_date_still_together = 'the band has been formed on '
    formed_phrase_unknown = 'It is unknown when the band has been formed.'
    split_phrase_approx = 'the band split up in '
    split_phrase_date = 'the band split up on '
    split_phrase_negative = 'the band is still together.'
    split_phrase_unknown = 'It is unknown if he band is still together.'
    expected_keywords = ['formed', 'split']

    # def __init__(self, name, *members, formed=date.today(), split=date.today()):
    def __init__(self, name, *members, formed=1960, split=date.today().year):
        self.name = name
        self.members = members
        self.formed = formed
        self.split = split
        pass                                            # introduce and initialize iterator counter, self.__i

    def __str__(self):
        tab = '\t'
        nl = '\n'
        name = self.name + (nl+tab)
        members = f'{(nl+tab).join([str(member) for member in self.members])}' + nl if self.members else ''
        formed = Band.formed_phrase_approx.capitalize() + str(self.formed) + '.' + nl
        split = Band.split_phrase_approx.capitalize() + str(self.split) + '.'
        return name + members + formed + split

    def __eq__(self, other):
        return isinstance(other, Band) and self.name == other.name and self.members == other.members

    @staticmethod
    def parse_band_str(band_str):
        """Splits a band string in its typical segments.
        """
        name, *members_str, rest1 = band_str.split('\n\t')
        last_member, formed_str, split_str = rest1.split('\n')
        members_str.append(last_member)
        members = [Musician.from_str(member) for member in members_str]
        formed = int(formed_str[-5:-1])
        split = int(split_str[-5:-1])

        return name, members, formed, split

    # # Alternative constructor 1
    @classmethod
    def from_band_str_year(cls, band_str):
        name, members, formed, split = Band.parse_band_str(band_str)
        return cls(name, *members, formed=formed, split=split)

    # Alternative constructor 2
    @classmethod
    def from_band_str_date(cls, band_str):
        pass

    @staticmethod
    def is_date_valid(d):
        """It is assumed that a band does not perform together since more than ~60 years ago.
        So, the valid date to denote the start of a band's career is between Jan 01, 1960, and today.
        """

        return date(1960, 1, 1) < d < date.today()

    def __iter__(self):
        """Once __iter__() and __next__() are implemented in a class,
        we can create an iterator object by calling the iter() built-in function on an object of the class,
        and then call the next() built-in function on that object.
        It is often sufficient to just return self in __iter__(),
        if the iterator counter such as self.__i is introduced and initialized in __init__().
        Alternatively, the iterator counter (self.__i) is introduced and initialized  here.
        """

        self.__i = 0
        return self               # sufficient if the iterator counter is introduced and initialized in __init__()

    def __next__(self):
        if self.__i < len(self.members):
            member = self.members[self.__i]
            self.__i += 1
            return member
        else:
            raise StopIteration


def next_member(band):
    """Generator that shows members of a band, one at a time.
    yield produces a generator object, on which we call the next() built-in function.
    A great tutorial on generators: https://realpython.com/introduction-to-python-generators/.
    """


class BandEncoder(json.JSONEncoder):
    """JSON encoder for Band objects.
    """

    def default(self, o):
        # recommendation: always use double quotes with JSON

        pass


def band_json_to_py(members_json):
    """JSON decoder for Band objects (object_hook parameter in json.loads()).
    """


if __name__ == "__main__":

    # from testdata.musicians import *

    # class variables (like static fields in Java; typically defined and initialized before __init__())
    # object class (like the Object class in Java; all classes inherit from object
    #   try, e.g., list.__mro__ in the console)
    #   object class defines object.__eq__(self, other) etc.
    #   object.__ne__(self, other), the inverse of object.__eq__(self, other),
    #   is provided by Python automatically once object.__eq__(self, other) is implemented

    # Check the basic methods (__init__(), __str__(),...)
    johnLennon = Musician('John Lennon', is_band_member=True)
    paulMcCartney = Musician('Paul McCartney', is_band_member=True)
    georgeHarrison = Musician('George Harrison', is_band_member=True)
    ringoStarr = Musician('Ringo Starr', is_band_member=True)
    theBeatlesList = [johnLennon, paulMcCartney, georgeHarrison, ringoStarr]

    theBeatles = Band('The Beatles', *theBeatlesList, formed=1962, split=1970)
    print(theBeatles)
    print()
    Band.parse_band_str(str(theBeatles))
    print()

    # Check the alternative constructor 1 (@classmethod from_band_str_year(<band_str>))
    print(Band.from_band_str_year(str(theBeatles)))
    print()

    # Check the alternative constructor 2 (@classmethod from_band_str_date(<band_str>))
    print()

    # Check date validator (@staticmethod is_date_valid(<date>))
    print(Band.is_date_valid(date(1980, 1, 23)))
    print()

    # Check the iterator
    m_iterator = iter(theBeatles)
    while True:
        try:
            print(next(m_iterator))
        except StopIteration:
            break
    print()

    # Repeated attempt to run the iterator fails, because the iterator is exhausted
    # print(next(m_iterator))

    # Demonstrate generators
    print()

    # Demonstrate generator expressions
    print()

    # Demonstrate JSON encoding/decoding of Band objects
    # Single object
    print()

    # List of objects
    print()


