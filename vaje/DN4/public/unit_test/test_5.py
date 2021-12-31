'''vsi_pari'''
import unittest
from plesalci import *

test_case = unittest.TestCase()
plesalci = {2: ('Urška', 2, 'ž'), 10: ('Blaž', 3, 'm'), 3: ('Andrej', 4, 'm'), 4: ('Simon', 2, 'm'), 15: ('Laura', 5, 'ž'), 1: ('Teja', 4, 'ž'), 8: ('Karmen', 2, 'ž'), 13: ('Domen', 4, 'm'), 11: ('Anja', 4, 'ž'), 12: ('Urška', 3, 'ž'), 0: ('Erik', 6, 'm'), 5: ('Anja', 12, 'ž'), 14: ('Tina', 12, 'ž'), 7: ('Aleksandra', 7, 'ž'), 6: ('Lucija', 5, 'ž'), 9: ('Ines', 10, 'ž')}

test_case.assertEqual(vsi_pari(plesalci, 1), {(3, 15), (1, 3), (3, 12), (10, 11), (0, 15), (4, 8), (12, 13), (1, 13), (13, 15), (10, 12), (8, 10), (2, 10), (0, 7), (3, 11), (0, 6), (4, 12), (3, 6), (6, 13), (1, 10), (2, 4), (11, 13)})