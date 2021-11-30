'''dolga_imena'''
import unittest
from IMDb import *

test_case = unittest.TestCase()
serije = [
    ('Friends', 9.0, 1994),
    ('The Big Bang Theory', 8.4, 2007),
    ('Game of Thrones', 9.5, 2011),
    ('Mr. Robot', 8.7, 2015),
    ('Humans', 8.1, 2015),
]
expected = ['The Big Bang Theory', 'Game of Thrones']
result = dolga_imena(serije)

test_case.assertEqual(expected, result)