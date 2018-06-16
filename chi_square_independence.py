from scipy.stats import chi2_contingency
import pandas as pd
import numpy as np


def read_contingency_table(file_name):
    data = pd.read_csv(file_name)
    table = np.zeros((4, 11), dtype=np.int)
    for i, row in data.iterrows():
        table[row['1.1.']][row['1.2.']] += 1
        table[row['2.1.']][row['2.2.']] += 1
        table[row['3.1.']][row['3.2.']] += 1
        table[row['4.1.']][row['4.2.']] += 1
        table[row['5.1.']][row['5.2.']] += 1
        table[row['6.1.']][row['6.2.']] += 1
        table[row['7.1.']][row['7.2.']] += 1
        table[row['8.1.']][row['8.2.']] += 1
        table[row['9.1.']][row['9.2.']] += 1
        table[row['10.1.']][row['10.2.']] += 1
        table[row['11.1.']][row['11.2.']] += 1
        table[row['12.1.']][row['12.2.']] += 1
        table[row['13.1.']][row['13.2.']] += 1
        table[row['14.1.']][row['14.2.']] += 1
        table[row['15.1.']][row['15.2.']] += 1
    return table


def test_independence(contingency_table):
    print(' ============== Contingency table ==============')
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in contingency_table]))
    chi2, p, dof, ex = chi2_contingency(contingency_table)
    print(' ============ Chi-square statistics ============')
    print(chi2)
    print(' =================== P-value ===================')
    print(p)
    print(' ============== Degrees of freedom =============')
    print(dof)
    return p <= 0.05
