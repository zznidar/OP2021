'''vrni_krajse'''
import unittest
from DN3 import *

test_case = unittest.TestCase()
test_case.assertEqual(vrni_krajse(['2:29', '42', '1:21', '3:11', '3:07', '4:01', '3:41', '1:01:22', '9', '11:39', '1:47'], '4:02'), ['2:29', '42', '1:21', '3:11', '3:07', '4:01', '3:41', '9', '1:47'])