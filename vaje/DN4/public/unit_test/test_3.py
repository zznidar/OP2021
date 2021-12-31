import unittest
from plesalci import *

test_case = unittest.TestCase()
test_case.assertIsNone(par((11, 'Anja', 4, 'ž'), (53, 'Janja', 5, 'ž'), 2))