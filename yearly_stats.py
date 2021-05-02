import numpy as np
import pandas as pd

def get_yearly_stats(files):
    files = [pd.read_csv(file) for file in files]
    results = []
    for file in files:
        file['date'] = pd.to_datetime(file['date'])
        idx =file.groupby(file.date.dt.year)['vol'].transform(max) == file['vol']
        df = file[idx]
        idx =file.groupby(file.date.dt.year)['close'].transform(max) == file['close']
        df2 = file[idx]
        results.append([df, df2])
    return results