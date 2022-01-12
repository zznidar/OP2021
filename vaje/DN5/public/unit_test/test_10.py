import unittest
from DN5 import *
from numpy import array, ndarray, nan, allclose
from pandas import DataFrame

test_case = unittest.TestCase()
results=vrni_dneve_najvisje_onesnazenosti(preberi_podatke("public/data/april.csv"))
if type(results) is DataFrame:
    results = results.values

expected = array([ 3, 11,  3,  3,  3,  3,  3,  3,  3, 16,  3,  3,  3,  8])
    
test_case.assertTrue(allclose(results, expected))