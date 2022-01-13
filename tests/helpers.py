import grblogtools as glt

def read_single(filename):
    summary, timelines = glt.get_dataframe([f'data/{filename}'], timelines=True)
    rows = summary.to_dict(orient='records')
    return rows[0], timelines
