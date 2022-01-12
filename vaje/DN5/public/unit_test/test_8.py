import unittest
from DN5 import *
from numpy import array, ndarray, nan, allclose
from pandas import DataFrame

test_case = unittest.TestCase()
results=vrni_dneve_najvisje_onesnazenosti(preberi_podatke("public/data/februar.csv"))
if type(results) is DataFrame:
    results = results.values

expected = array([ 1,  1,  1, 13,  1,  1,  1,  1, 12,  1,  1, 22, 12, 23])
    
test_case.assertTrue(allclose(results, expected))
