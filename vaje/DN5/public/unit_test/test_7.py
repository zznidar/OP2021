'''vrni_dneve_najvisje_onesnazenosti'''
import unittest
from DN5 import *
from numpy import array, ndarray, nan, allclose
from pandas import DataFrame

test_case = unittest.TestCase()
results=vrni_dneve_najvisje_onesnazenosti(preberi_podatke("public/data/januar.csv"))
if type(results) is DataFrame:
    results = results.values

expected = array([ 1, 23, 23, 24,  1, 31,  1, 31, 31, 21, 28, 31, 29, 30])
    
test_case.assertTrue(allclose(results, expected))
