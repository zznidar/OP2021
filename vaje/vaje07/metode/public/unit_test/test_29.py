import unittest
from metode import *

test_case = unittest.TestCase()
kraji = ["Ljubljana", "Maribor", "Celje", "Iskrba"]
februar = [(1, (88, 127, 121, 5)),
     (2, (59, 72, 27, 6)),
     (3, (16, 21, 16, 7)),
     (4, (19, 28, 21, 4)),
     (5, (21, 17, 16, 7)),
     (6, (16, 13, 13, 4)),
     (7, (20, 40, 42, 17)),
     (8, (34, 47, 41, 24)),
     (9, (37, 59, 54, 19)),
     (10, (53, 61, 62, 29)),
     (11, (53, 66, 68, 30)),
     (12, (47, 76, 88, 26)),
     (13, (51, 66, 70, 44)),
     (14, (45, 72, 72, 27)),
     (15, (61, 64, 66, 9)),
     (16, (60, 65, 76, 20)),
     (17, (59, 97, 68, 24)),
     (18, (27, 34, 34, 8)),
     (19, (22, 26, 30, 7)),
     (20, (40, 44, 57, 9)),
     (21, (35, 69, 52, 15)),
     (22, (35, 56, 44, 13)),
     (23, (20, 23, 17, 13)),
     (24, (14, 26, 15, 5)),
     (25, (None, 28, 27, 8)),
     (26, (25, 27, 39, 8)),
     (27, (22, 31, 37, None)),
     (28, (19, 23, 19, None))
]

test_case.assertEqual(najveckrat_onesnazena_mesta(februar, kraji), {'Maribor'})
