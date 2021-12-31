import unittest
from plesalci import *

test_case = unittest.TestCase()
plesalci = {2: ('Tamara', 2, 'ž'), 10: ('Neža', 12, 'ž'), 3: ('Urban', 7, 'm'), 4: ('Nastja', 1, 'ž'), 15: ('Nik', 8, 'm'), 1: ('Vesna', 4, 'ž'), 8: ('Lucija', 4, 'ž'), 13: ('Saša', 5, 'ž'), 11: ('Matjaž', 1, 'm'), 12: ('Denis', 3, 'm'), 0: ('Benjamin', 12, 'm'), 5: ('Hana', 5, 'ž'), 14: ('Karin', 2, 'ž'), 7: ('Anže', 3, 'm'), 6: ('Domen', 2, 'm'), 9: ('Urša', 6, 'ž'), 22: ('Jakob', 9, 'm'), 24: ('Peter', 1, 'm'), 27: ('Ines', 11, 'ž'), 29: ('Ines', 8, 'ž'), 21: ('Mateja', 2, 'ž'), 23: ('Mihael', 2, 'm'), 19: ('Vid', 7, 'm'), 25: ('Lucija', 6, 'ž'), 28: ('Jaka', 2, 'm'), 20: ('Jasmina', 1, 'ž'), 26: ('Tadej', 6, 'm'), 16: ('Jernej', 8, 'm'), 17: ('Eva', 5, 'ž'), 18: ('Filip', 1, 'm')}

test_case.assertEqual(brez_para(plesalci, 0), {1, 3, 5, 7, 8, 12, 13, 17, 19, 22, 27})