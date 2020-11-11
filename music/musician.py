"""Domain classes and functions related to the concept of musician
"""


# from util import utility
# from music.enums import Vocals, Instrument
import json


class Musician:
    """The class describing the concept of musician.
    It is assumed that a musician is sufficiently described by their
    name and whether they are a solo musician or a member of a band.

    This class illustrates some of the important concepts of Python classes:
    - self
    - __init__()
    - __str__()
    - __eq__(self, other) is the equivalent of Java equals() and should be overridden in classes
    - __dict__ attribute of all objects ()
    - data fields (instance variables)
    - methods - calling them by self.<method>(...) from the same class where they are defined
    """

    def __init__(self, name, is_band_member=True):
        self.name = name
        self.is_band_member = is_band_member
        # self.__n = 'lll'                                    # 'private' field

    # Properties: 'private' fields; run setters and getters in the debugger.
    # Make name a property (after setting up __init__(), __str__(), __eq__(), methods,...).

    # Add an immutable property (no setter for it)

    def __str__(self):
        return self.name + ', ' + ('band member' if self.is_band_member else 'solo musician')

    def __eq__(self, other):
        return isinstance(other, Musician) and other.name == self.name and other.is_band_member == self.is_band_member

    def play(self, song_title, *args, **kwargs):
        """Assumes that song_title, *args (expressions of gratitude) and kwargs.values() (messages) are strings.
        Prints song_title, rhythm counts, expressions of gratitude and messages. A call example:
            <musician>.play(song_title, *['Thank you!', 'You're wonderful!], love='We love you!')
        """

        # print(self.name + ' plays:', song_title)
        rhythm_count = kwargs['rhythm_count'] if 'rhythm_count' in kwargs.keys() else ''
        messages = ' '.join([v for k, v in kwargs.items() if not k == 'rhythm_count']) if kwargs else ''
        return f'{self.name} playing: {rhythm_count}! - {song_title} - {" ".join(arg for arg in args)} {messages}'

    def play_song(self, song_title, *args, **kwargs):
        """Demonstrates calling another method from the same class (self.<method>(...) as a mandatory syntax).
        """

        return self.play(song_title, *args, **kwargs)

    # Alternative constructor
    @classmethod
    def from_str(cls, musician_string):
        """Inverted __str__() method.
        Assumes that musician_string is in the format generated by __str__().
        """

        pass


class MusicianEncoder(json.JSONEncoder):
    """JSON encoder for musician objects.
    """

    def default(self, o):
        # recommendation: always use double quotes with JSON

        pass


def musician_json_to_py(musician_json):
    """JSON decoder for Musician objects (object_hook parameter in json.loads()).
    """


class Singer(Musician):
    """The class describing the concept of singer.
    It is assumed that a singer is sufficiently described as a Musician,
    with the addition of whether they are a lead or a background singer.

    Useful link (related to inheritance in Python):
    https://stackoverflow.com/questions/3394835/use-of-args-and-kwargs/3394902#3394902 (calling super() in constructors)
    """

    # Version 1 - no multiple inheritance

    # Version 2 - with multiple inheritance

    def play(self, song_title, *args, **kwargs):
        """Overrides the play() method from superclass.
        Assumes that song_title, *args (expressions of gratitude) and kwargs.values() (messages) are strings.
        Prints song_title, expressions of gratitude and messages. A call example:
            <singer>.play(song_title, *['Thank you!', 'You're wonderful!], love='We love you!')
        """


class Songwriter(Musician):
    """The class describing the concept of songwriter.
    It is assumed that a songwriter is sufficiently described as a musician
    who writes songs and plays an instrument.
    """

    # Version 1 - no multiple inheritance

    # Version 2 - with multiple inheritance

    def what_do_you_do(self):
        """Just a simple method to describe the concept of songwriter.
        """


class SingerSongwriter(Singer, Songwriter):
    """The class describing the concept of singer-songwriter.
    It is assumed that a singer-songwriter is sufficiently described as a Singer who is simultaneously a Songwriter.

    Useful links :
    https://stackoverflow.com/a/50465583/1899061 (designing classes (i.e. their __init__() methods) for multiple inh.)
    https://stackoverflow.com/a/533675/1899061 (mixins explained, and what good they are in multiple inheritance)
    """


if __name__ == "__main__":

    # from testdata.musicians import *
    johnLennon = Musician('John Lennon', is_band_member=True)

    # Print objects
    john = Musician('John Lennon', is_band_member=True)
    print(john.name)
    print(john)
    print()

    # Compare objects
    print(john == johnLennon)
    print(john.__eq__(johnLennon))
    print(john.__ne__(johnLennon))
    print()

    # Access data fields (instance variables), including 'private' fields
    print()

    # Add new data fields (instance variables)
    #   1. <object>.<new_attr> = <value>
    #   2. <object>.__setattr__('<new_attr>', <value>)      # counterpart: <object>.__getattribute__('<attr>')
    #   3. setattr(<object>, '<new_attr>', <value>))        # counterpart: getattr(<object>, '<attr>')
    print()

    # Calling methods
    # john.play('Nobody Told Me')
    # john.play_song('Nobody Told Me')
    print(johnLennon.play('I Saw Her Standing There', 'Thank you!',
                          rhythm_count='One, two, three, four',
                          end='Good night!'))
    print(johnLennon.play_song('I Saw Her Standing There', 'Thank you!',
                               rhythm_count='One, two, three, four',
                               end='Good night!'))
    print()

    # Demonstrate object data fields and methods in Python Console for some built-in classes (boolean, int, object,...)
    # - True + 1
    # - True.__int__()
    # - (1).__class__.__name__
    # - (1).__class__
    # - o.__dir__()
    # - o.__dir__
    # - o.__dict__

    # Demonstrate object data fields and methods for Musician objects
    print()

    # Demonstrate @classmethod (from_str())
    print()

    # Demonstrate inheritance
    # object class (like the Object class in Java; all classes inherit from object
    #   try, e.g., list.__mro__ in the console)
    #   object class defines object.__eq__(self, other) etc.
    #   object.__ne__(self, other), the inverse of object.__eq__(self, other),
    #   is provided by Python automatically once object.__eq__(self, other) is implemented
    print()

    # Demonstrate method overriding
    print()

    # Demonstrate multiple inheritance and MRO.
    # Make sure to read this first: https://stackoverflow.com/a/50465583/1899061 (especially Scenario 3).
    print()

    # Demonstrate JSON encoding/decoding of Performer objects
    # Single object
    print()

    # List of objects
    print()

