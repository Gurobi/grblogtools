from helpers import *

def test_cuts():
    row, timelines = read_single('912-glass4-0.log')
    cuts = { key: row[key] for key in row.keys() if key.startswith('Cuts: ') }
    assert len(cuts) == 8