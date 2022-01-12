'''preberi_podatke'''
import unittest
from onesnazenost import *
from numpy import array, allclose

test_case = unittest.TestCase()
results = preberi_podatke('podatki/januar.csv')
expected = (array([[152,  88, 134,  35],
       [ 61,  68,  94,  31],
       [ 40,  81,  83,  61],
       [ 57,  69,  86,  51],
       [ 39,  19,  39,  11],
       [ 10,  16,  13,   5],
       [ 19,  34,  43,  14],
       [ 34,  50,  48,  32],
       [ 71,  71,  67,  51],
       [ 37,  47,  47,  31],
       [ 67,  67,  82,  43],
       [ 82,  77,  34,  33],
       [ 11,  15,  19,   5],
       [ 33,  14,  60,  17],
       [ 47,  18,  67,  17],
       [ 29,  23,  36,  15],
       [ 11,  24,  16,  11],
       [ 20,  34,  31,  28],
       [ 42,  56,  51,  46],
       [ 65,  72, 101,  58],
       [ 88, 101, 105,  55],
       [ 79, 138,  93,  74],
       [ 91, 170,  97,  87],
       [104, 106,  97, 111],
       [ 62,  74,  64,  74],
       [ 31,  51,  54,  38],
       [ 53,  62,  75,  36],
       [ 93,  94, 100,  91],
       [124, 100, 112, 120],
       [108,  99, 101, 113],
       [132, 146,  93,  90]]), 
['Ljubljana', 'Maribor', 'Zagorje', 'Velenje']) 

test_case.assertEqual(results[1],expected[1])
test_case.assertTrue(allclose(results[0], expected[0]))