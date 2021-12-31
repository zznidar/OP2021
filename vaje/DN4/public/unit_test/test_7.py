'''brez_para'''
import unittest
from plesalci import *

test_case = unittest.TestCase()
plesalci = {1: ('Teja', 4, 'ž'), 5: ('Anja', 12, 'ž'), 10: ('Blaž', 3, 'm'), 12: ('Urška', 3, 'ž'), 14: ('Tina', 12, 'ž'), 0: ('Erik', 6, 'm'), 3: ('Andrej', 4, 'm'), 6: ('Lucija', 5, 'ž'), 9: ('Ines', 10, 'ž'), 13: ('Domen', 4, 'm'), 2: ('Urška', 2, 'ž'), 7: ('Aleksandra', 7, 'ž'), 4: ('Simon', 2, 'm'), 8: ('Karmen', 2, 'ž'), 15: ('Laura', 5, 'ž'), 11: ('Anja', 4, 'ž')}

test_case.assertEqual(brez_para(plesalci, 1), {9, 5, 14})