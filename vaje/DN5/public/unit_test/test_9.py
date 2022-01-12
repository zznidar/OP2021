import unittest
from DN5 import *
from numpy import array, ndarray, nan, allclose
from pandas import DataFrame

test_case = unittest.TestCase()
results=vrni_dneve_najvisje_onesnazenosti(preberi_podatke("public/data/marec.csv"))
if type(results) is DataFrame:
    results = results.values

expected = array([17, 18, 16, 17, 17, 17, 15, 17, 18, 18, 18, 17, 18, 17])
    
test_case.assertTrue(allclose(results, expected))