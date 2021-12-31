'''par'''
import unittest
from plesalci import *

test_case = unittest.TestCase()
test_case.assertEqual(par((3, 'Andrej', 4, 'm'), (11, 'Anja', 4, 'ž'), 1), (3, 11))