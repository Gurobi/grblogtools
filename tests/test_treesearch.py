from numpy import NaN, isnan
from helpers import *
from pytest import approx

def test_tree_search():
    row, timelines = read_single('912-glass4-0.log')
    tree = timelines['nodelog']
    assert len(tree.index) == 35

    rows = tree.to_dict(orient='records')

    heur = rows[33]
    assert heur['CurrentNode'] == 187961
    assert heur['RemainingNodes'] == 3679
    assert heur['Incumbent'] == 1.200013e+09
    assert heur['BestBd'] == 1.2000e+09
    assert heur['Gap'] == 0
    assert heur['ItPerNode'] == 7.3
    assert heur['Time'] == 35

    pruned = rows[30]
    assert pruned['CurrentNode'] == 177203
    assert pruned['RemainingNodes'] == 30607
    assert pruned['Incumbent'] == 1.4e+09
    assert pruned['BestBd'] == 1.2e+09
    assert pruned['Gap'] == approx(0.143, 1e-5)
    assert pruned['ItPerNode'] == 7.4
    assert pruned['Time'] == 35 

    final = rows[34]
    
    # Explored 188145 nodes (1383139 simplex iterations) in 35.66 seconds
    assert final['Time'] == 35.66
    assert final['CurrentNode'] == 188145
    assert isnan(final['RemainingNodes'])

    # Best objective 1.200012600000e+09, best bound 1.200007800000e+09, gap 0.0004%
    assert final['Incumbent'] == approx(1.200012e9)
    assert final['BestBd'] == approx(1.200008e9)
    assert final['Gap'] == 0.000004
    