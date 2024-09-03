# Add the src directory to the Python path
from main import add_two_numbers
# import os
# import sys
# sys.path.insert(0, os.path.abspath(
#     os.path.join(os.path.dirname(__file__), '../src')))


def main_test():
    assert add_two_numbers(1, 2) == 3
    assert add_two_numbers(0, -1) == -1
