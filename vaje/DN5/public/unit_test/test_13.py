import unittest
from DN5 import *
from numpy import array, ndarray, nan, allclose
from pandas import DataFrame

test_case = unittest.TestCase()
results=brez_manjkajocih_meritev(preberi_podatke("public/data/marec2.csv"))

test_case.assertEqual(results, {'Celje', 'Iskrba', 'Koper', 'Ljubljana', 'Maribor', 'Nova Gorica', 'Zagorje', 'Žerjav'})