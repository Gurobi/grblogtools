from helpers import *
from pytest import approx

def test_qafiro():
    row, timelines = read_single('950_qafiro.log')
    root = timelines['rootlp']  
    t = type(root)
    barrier = root.to_dict(orient='records')
    
    assert len(barrier) == 13
    
    line = barrier[0]
    assert line['PObj'] == approx(3.04762508e+05, abs=1e-2)
    assert line['DObj'] == approx(-6.19194374e+05, abs=1e-2)
    assert line['PRes'] == 3.78e+03
    assert line['DRes'] == 3.64e+02
    assert line['Compl'] == 1.01e+06
    assert line['Time'] == 0
        
    line = barrier[12]
    assert line['PObj'] == approx(-1.59078179e+00, abs=1e-2)
    assert line['DObj'] == approx(-1.59078179e+00, abs=1e-2)
    assert line['PRes'] == approx(3.89e-16, abs=1e-18)
    assert line['DRes'] == approx(1.17e-15, abs=1e-13)
    assert line['Compl'] == approx(8.66e-12, abs=1e-14)
    assert line['Time'] == 0

def test_barrier_and_tree_search():
    row, timelines = read_single('950_glass4_Method2.log')
    
    barrier = timelines['rootlp']
    assert len(barrier.index) == 10

    tree = timelines['nodelog']
    assert len(tree.index) == 41

