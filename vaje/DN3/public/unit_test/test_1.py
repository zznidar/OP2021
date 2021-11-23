'''pretvori_v_sekunde'''
import unittest
from DN3 import *

test_case = unittest.TestCase()
test_case.assertEqual(pretvori_v_sekunde('5:32'), 332)
