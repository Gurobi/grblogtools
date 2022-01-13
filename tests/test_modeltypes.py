from numpy import NaN, isnan
from helpers import *
from pytest import approx

def test_tree_search():
    row, timelines = read_single('912-glass4-0.log')
    assert row['ModelType'] == 'MIP'