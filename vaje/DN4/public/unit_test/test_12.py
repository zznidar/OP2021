'''najvec_zmag'''
import unittest
from plesalci import *

test_case = unittest.TestCase()
plesalci = {0: ('Benjamin', 12, 'm'), 1: ('Vesna', 4, 'ž'), 2: ('Tamara', 2, 'ž'), 3: ('Sandi', 4, 'm'), 4: ('Kevin', 2, 'm'), 5: ('Nina', 12, 'ž'), 6: ('Hana', 5, 'ž'), 7: ('Aleksandra', 3, 'ž'), 8: ('Monika', 10, 'ž'), 9: ('Anže', 3, 'm'), 10: ('Anja', 4, 'ž'), 11: ('Lea', 3, 'ž')}

zmage = {(0, 1): 0, (2, 7): 3, (4, 7): 0, (1, 3): 0, (4, 6): 0, (5, 6): 0, (7, 8): 2, (5, 7): 4, (3, 5): 0, (1, 7): 0, (3, 8): 0, (2, 6): 0, (0, 5): 0, (0, 4): 1, (2, 3): 3, (1, 6): 3, (0, 8): 4, (3, 4): 1, (0, 2): 4, (6, 8): 3}

test_case.assertEqual({2}, najvec_zmag(plesalci, zmage))