import unittest
from DN5 import *
from numpy import array, ndarray, nan, allclose
from pandas import DataFrame

test_case = unittest.TestCase()
results=vrni_povprecja_po_krajih(preberi_podatke("public/data/maj.csv"))
if type(results) is DataFrame:
    results = results.values

expected = array([ 15.38709677,  19.35483871,  18.32258065,  10.58064516,  16.        ,  14.56666667,  15.05555556,  15.        ,  14.77419355,  14.19354839,  12.66666667,  14.41935484])
    
test_case.assertTrue(allclose(results, expected))