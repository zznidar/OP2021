import unittest
from razcep import *

test_case = unittest.TestCase()
test_case.assertEqual(prastevila(42), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41])