import unittest
from DN5 import *
from numpy import array, ndarray, nan, allclose
from pandas import DataFrame

test_case = unittest.TestCase()
results=vrni_povprecja_po_krajih(preberi_podatke("public/data/april.csv"))
if type(results) is DataFrame:
    results = results.values

expected = array([ 17.34482759,  20.46666667,  21.06666667,  11.63333333,  18.4,  15.86666667,  17.7,  16.1,  18.375,  17.,  15.66666667,  16.53333333,  14.13333333,  17.58823529])
test_case.assertTrue(allclose(results, expected))