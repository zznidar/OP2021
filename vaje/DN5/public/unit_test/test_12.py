import unittest
from DN5 import *
from numpy import array, ndarray, nan, allclose
from pandas import DataFrame

test_case = unittest.TestCase()
results=brez_manjkajocih_meritev(preberi_podatke("public/data/februar.csv"))

test_case.assertEqual(results, {'Celje', 'Hrastnik', 'Koper', 'Kranj', 'Maribor', 'Murska Sobota', 'Nova Gorica', 'Trbovlje', 'Velenje', 'Zagorje'})