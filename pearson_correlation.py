from scipy.stats import pearsonr
import pandas as pd
import numpy as np


def read_series(file_name):
    data = pd.read_csv(file_name)
    u = []
    b = []
    for i, row in data.iterrows():
        u.append(row['1.1.'])
        b.append(row['1.2.'])
        u.append(row['2.1.'])
        b.append(row['2.2.'])
        u.append(row['3.1.'])
        b.append(row['3.2.'])
        u.append(row['4.1.'])
        b.append(row['4.2.'])
        u.append(row['5.1.'])
        b.append(row['5.2.'])
        u.append(row['6.1.'])
        b.append(row['6.2.'])
        u.append(row['7.1.'])
        b.append(row['7.2.'])
        u.append(row['8.1.'])
        b.append(row['8.2.'])
        u.append(row['9.1.'])
        b.append(row['9.2.'])
        u.append(row['10.1.'])
        b.append(row['10.2.'])
        u.append(row['11.1.'])
        b.append(row['11.2.'])
        u.append(row['12.1.'])
        b.append(row['12.2.'])
        u.append(row['13.1.'])
        b.append(row['13.2.'])
        u.append(row['14.1.'])
        b.append(row['14.2.'])
        u.append(row['15.1.'])
        b.append(row['15.2.'])
    return np.array(u), np.array(b)


def calculate_correlation(series):
    u = series[0]
    b = series[1]
    r, p = pearsonr(u, b)
    print(' ======= Pearson correlation coefficient =======')
    print(r)
