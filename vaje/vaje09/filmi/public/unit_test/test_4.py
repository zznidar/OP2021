'''oblikovan_izpis'''
import unittest
from filmi import *

test_case = unittest.TestCase()
from unittest.mock import patch
import io

expected = "Naslov filma             Leto\n-----------------------------\nThe Godfather            1972\nSchindler's List         1993\nCasablanca               1942\nForrest Gump             1994\nThe Sound of Music       1965\nGladiator                2000\nTitanic                  1997\nSaving Private Ryan      1998\n"

@patch('sys.stdout', new_callable=io.StringIO)
def test_oblikovan_izpis(mock_stdout):
    oblikovan_izpis('podatki/filmi.txt')
    test_case.assertEqual(mock_stdout.getvalue().rstrip(), expected.rstrip())

test_oblikovan_izpis()