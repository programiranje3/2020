"""The class representing the concept of a music/recording studio.
"""

from datetime import date
import sys
from pathlib import Path
from pickle import dump, load

from music.musician import *
from music.band import *
# from util.utility import *

import json


class Studio:
    """The class describing the concept of a music/recording studio.
    It includes the studio name, a list of Band objects (bands recording in that studio over a certain period of time),
    location and the start and end dates for the scheduled recording sessions.
    """

    def __init__(self, name, location, *bands, start_date=date(1961, 1, 1), end_date=date(1970, 12, 31)):
        if start_date > end_date:
            raise RecordingDateError(start_date, end_date)
        elif not all([band.formed < end_date for band in bands]):
            raise BandStartDateError(bands[[band.formed < end_date for band in bands].index(False)], end_date)
        else:
            self.name = name
            self.location = location
            self.start_date = start_date
            self.end_date = end_date
            self.bands = bands

    def __str__(self):
        studio = f'"{self.name}" studio, {self.location}'
        sessions = f'Recording sessions: {self.start_date} - {self.end_date}'
        bands = f'Bands: {", ".join([band.name for band in list(self.bands)])}'
        return f'{studio}\n{sessions}\n{bands}'


class StudioError(Exception):
    """Base class for exceptions in this module.
    """

    pass


class RecordingDateError(StudioError):
    """Exception raised when the start date of the recording sessions is not before the end date.
    """

    def __init__(self, start, end):
        self.message = f'session start date ({start}) after session end date ({end})'


class BandStartDateError(StudioError):
    """Exception raised when a the date when a band started performing together is not between the start and end dates
    of the recording sessions.
    """

    def __init__(self, band, end):
        self.message = f'band formed on {band.formed}, after recording session end {end}'


class StudioEncoder(json.JSONEncoder):
    """JSON encoder for Studio objects.
    """

    def default(self, o):
        # recommendation: always use double quotes with JSON

        pass


def studio_json_to_py(studio_json):
    """JSON decoder for Studio objects (object_hook parameter in json.loads()).
    """


if __name__ == "__main__":

    from testdata.musicians import *

    # Demonstrate exceptions - user-defined exceptions (wrong recording date(s), wrong band start date)
    # the_beatles = Band('The Beatles', *[johnLennon, paulMcCartney, georgeHarrison, ringoStarr],
    #                    formed=date(1962, 8, 18), split=date(1970, 4, 10))
    # pink_floyd = Band('Pink Floyd', rogerWaters, nickMason, rickWright, davidGilmour,
    #                   formed=date(1965, 2, 12), split=date(1995, 3, 14))

    # # Create a Studio object
    # abbey_road = Studio('Abbey Road', 'London', the_beatles, pink_floyd,
    #                     start_date=date(1967, 1, 1), end_date=date(1967, 12, 31))
    # print(abbey_road)
    # print()

    # Demonstrate exceptions
    # Here's the hierarchy of built-in exceptions: https://docs.python.org/3/library/exceptions.html#exception-hierarchy

    # Demonstrate exceptions - the general structure of try-except statements, possibly including else and finally
    print()

    # Demonstrate exceptions - except: Exception as <e> (and then type(<e>), <e>.__class__.__name__, <e>.args,...)
    print()

    # Demonstrate exceptions - user-defined exceptions (wrong recording date(s), wrong band start date)
    the_beatles = Band('The Beatles', *[johnLennon, paulMcCartney, georgeHarrison, ringoStarr],
                       formed=date(1972, 8, 18), split=date(1970, 4, 10))
    pink_floyd = Band('Pink Floyd', rogerWaters, nickMason, rickWright, davidGilmour,
                      formed=date(1965, 2, 12), split=date(1995, 3, 14))
    try:
        abbey_road = Studio('Abbey Road', 'London', the_beatles, pink_floyd,
                            start_date=date(1967, 1, 1), end_date=date(1967, 12, 31))
        # print(4/0)
    except RecordingDateError as e:
        # print(f'Caught {e.__class__.__name__} exception: {e.message}')
        sys.stderr.write(f'Caught {e.__class__.__name__} exception: {e.message}\n')
        raise
    except BandStartDateError as e:
        # print(f'Caught {e.__class__.__name__} exception: {e.message}')
        # sys.stderr.write(f'Caught {e.__class__.__name__} exception: {e.message}\n')
        sys.stderr.write(f'Caught {e.__class__.__name__} exception: {e.args[0]}\n')
        raise
    except Exception as e:
        # print(f'Caught {e.__class__.__name__} exception')
        sys.stderr.write(f'Caught {e.__class__.__name__} exception')
        raise
    else:
        print("It's OK.")
    finally:
        print("That's it.")

    # Demonstrate writing to a text file - <outfile>.write(), <outfile>.writelines()

    print()

    # Demonstrate reading from a text file - <infile>.read(), <infile>.readline()
    print()

    # Demonstrate writing to a binary file - pickle.dump() and <f>.write()/<f>.writelines() with str.encode(<obj>)
    print()

    # Demonstrate reading from a binary file - pickle.load() and <f>.read().decode()/<f>.readlines().decode()
    print()

    # Demonstrate get_project_dir(), get_data_dir() and writing/reading to/from files in data dir
    print()

    # Demonstrate JSON encoding/decoding of Studio objects
    # Single object
    print()

    # List of objects
    print()

