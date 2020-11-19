"""Project configuration settings (PROJECT_DIR, format strings, etc.)
"""

from pathlib import Path

PREFERRED_STRING_FORMAT = '%b %d, %Y'
PROJECT_DIR = Path(__file__).parent

# print(PROJECT_DIR)
# print(type(PROJECT_DIR))

# import os
#
# print(__file__)
# print(os.path.abspath(__file__))
# print(os.path.dirname(__file__))
#
# PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
# print(PROJECT_DIR)
# print(type(PROJECT_DIR))

