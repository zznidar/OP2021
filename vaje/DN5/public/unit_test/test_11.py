'''brez_manjkajocih_meritev'''
import unittest
from DN5 import *
from numpy import array, ndarray, nan, allclose
from pandas import DataFrame

test_case = unittest.TestCase()
results=brez_manjkajocih_meritev(preberi_podatke("public/data/januar.csv"))

test_case.assertEqual(results, {'Iskrba', 'Koper', 'Kranj', 'Maribor', 'Murska Sobota', 'Novo mesto', 'Trbovlje', 'Velenje', 'Zagorje'})