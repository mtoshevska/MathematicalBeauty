from chi_square_independence import read_contingency_table, test_independence
from pearson_correlation import read_series, calculate_correlation


data_directory = 'data'
technical_subjects = 'Technical.csv'
non_technical_subjects = 'Non-technical.csv'

print('============== Technical subjects ==============')
calculate_correlation(read_series(data_directory + '/' + technical_subjects))
res = test_independence(read_contingency_table(data_directory + '/' + technical_subjects))
if res:
    print('Null hypothesis is rejected')
else:
    print('Null hypothesis is accepted')

print('\n\n')
print('============ Non-technical subjects ============')
calculate_correlation(read_series(data_directory + '/' + non_technical_subjects))
res = test_independence(read_contingency_table(data_directory + '/' + non_technical_subjects))
if res:
    print('Null hypothesis is rejected')
else:
    print('Null hypothesis is accepted')
