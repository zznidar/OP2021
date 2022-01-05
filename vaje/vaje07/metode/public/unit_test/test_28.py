'''najveckrat_onesnazena_mesta'''
import unittest
from metode import *

test_case = unittest.TestCase()
kraji = ["Ljubljana", "Maribor", "Celje", "Iskrba"]
januar = [(1, (126, 88, None, 12)),
     (2, (53, 68, 77, 13)),
     (3, (34, 81, 96, 8)),
     (4, (None, 69, 117, 12)),
     (5, (31, 19, 51, 6)),
     (6, (13, 16, 16, 5)),
     (7, (22, 34, 42, 11)),
     (8, (39, 50, 58, 8)),
     (9, (66, 71, 90, 16)),
     (10, (41, 50, 52, 28)),
     (11, (62, 67, 82, 18)),
     (12, (73, 77, 29, 5)),
     (13, (12, 15, 19, 3)),
     (14, (34, 14, 57, 8)),
     (15, (48, 18, 82, 11)),
     (16, (32, 23, 72, 12)),
     (17, (15, 24, 28, 19)),
     (18, (23, 34, 36, 22)),
     (19, (38, 56, 65, 27)),
     (20, (51, 72, None, 17)),
     (21, (67, 101, None, 25)),
     (22, (70, 138, 142, 40)),
     (23, (78, 170, 146, 67)),
     (24, (96, 106, 105, 82)),
     (25, (56, 74, 73, 26)),
     (26, (31, 51, 75, 22)),
     (27, (40, 62, 66, 22)),
     (28, (81, 94, 116, 29)),
     (29, (101, 100, 109, 68)),
     (30, (83, 99, 102, 42)),
     (31, (110, 146, 115, 5))
]

test_case.assertEqual(najveckrat_onesnazena_mesta(januar, kraji), {'Celje', 'Maribor'})