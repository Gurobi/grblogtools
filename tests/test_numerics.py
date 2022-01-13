from numpy import NaN, isnan
from helpers import *
from pytest import approx

def test_numerics_general():
    row, timelines = read_single('912-glass4-0.log')

    assert row['MinCoeff'] == 1
    assert row['MaxCoeff'] == 8e6
    assert row['MinObjCoeff'] == 1
    assert row['MaxObjCoeff'] == 1e6
    assert row['MinBound'] == 1
    assert row['MaxBound'] == 8e2
    assert row['MinRHS'] == 1
    assert row['MaxRHS'] == 8e6