'''zmage_na_plesalca'''
import unittest
from plesalci import *

test_case = unittest.TestCase()
zmage = {(0, 1): 0, (2, 7): 3, (4, 7): 0, (1, 3): 0, (4, 6): 0, (5, 6): 0, (7, 8): 2, (5, 7): 4, (3, 5): 0, (1, 7): 0, (3, 8): 0, (2, 6): 0, (0, 5): 0, (0, 4): 1, (2, 3): 3, (1, 6): 3, (0, 8): 4, (3, 4): 1, (0, 2): 4, (6, 8): 3}

test_case.assertEqual({0: 9, 1: 3, 2: 10, 3: 4, 4: 2, 5: 4, 6: 6, 7: 9, 8: 9}, zmage_na_plesalca(zmage))