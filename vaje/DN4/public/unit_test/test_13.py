import unittest
from plesalci import *

test_case = unittest.TestCase()
plesalci = {0: ('Erik', 12, 'm'), 1: ('Teja', 11, 'ž'), 2: ('Urška', 6, 'ž'), 3: ('Gašper', 9, 'm'), 4: ('Sabina', 1, 'ž'), 5: ('Lucija', 3, 'ž'), 6: ('David', 3, 'm'), 7: ('Blaž', 1, 'm'), 8: ('Kaja', 3, 'ž')}
zmage = {(0, 1): 0, (2, 7): 3, (4, 7): 0, (1, 3): 0, (4, 6): 0, (5, 6): 0, (7, 8): 2, (5, 7): 4, (3, 5): 0, (1, 7): 0, (3, 8): 0, (2, 6): 0, (0, 5): 0, (0, 4): 1, (2, 3): 3, (1, 6): 3, (0, 8): 4, (3, 4): 1, (0, 2): 4, (6, 8): 3}

test_case.assertEqual({0,7}, najvec_zmag(plesalci, zmage, spol='m'))