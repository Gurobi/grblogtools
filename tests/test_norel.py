from numpy import NaN, isnan
from helpers import *
from pytest import approx

def test_tree_search():
    row, timelines = read_single('912-NoRelHeurWork60-glass4-0.log')
    norel = timelines['norel']

    assert len(norel.index) == 15
    rows = norel.to_dict(orient='records')

    row = rows[0]
    assert isnan(row['Incumbent'])

    row = rows[1]
    assert row['Time'] == 10
    assert row['Incumbent'] == approx(1.450014e+09)

    row = rows[3]
    assert row['Time'] == 21
    assert row['Incumbent'] == approx(1.200013e+09)

    row = rows[14]
    assert row['Time'] == 93
    assert row['Incumbent'] == approx(1.200013e+09)
    assert row['BestBd'] == approx(8.00002e+08)