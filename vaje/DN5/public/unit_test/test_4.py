'''vrni_povprecja_po_krajih'''
import unittest
from DN5 import *
from numpy import array, ndarray, nan, allclose
from pandas import DataFrame

test_case = unittest.TestCase()
results=vrni_povprecja_po_krajih(preberi_podatke("public/data/marec.csv"))
if type(results) is DataFrame:
    results = results.values

expected = array([ 26.41935484,  28.32258065,  34.58064516,  13.72413793,  33.4516129 ,  24.58064516,  30.58064516,  29.09090909,  26.58064516,  27.51612903,  21.87096774,  26.64516129,  24.58064516,  23.74193548])
    
test_case.assertTrue(allclose(results, expected))
