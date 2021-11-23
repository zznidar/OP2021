import unittest
from DN3 import *

test_case = unittest.TestCase()
test_case.assertEqual(vrni_skupno_dolzino(['2:37', '3:02', '3:27', '3:44', '3:41', '22:2:36', '1:38', '2:02', '3:35', '3:00', '25:3:48', '1:44', '3:35', '4:46', '1:34']), 171889)

