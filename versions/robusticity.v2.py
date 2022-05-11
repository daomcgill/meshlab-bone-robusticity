import numpy as np
import pandas as pd
from scipy import stats

#filename to be read
filename = "femur_gt.xlsx"
#bone number
bone_number = "fe1"
#filename, sheet#
df = pd.read_excel(filename, sheet_name = 0, header = 0)
#column name
column_name = 'original'

mean = np.mean(df[column_name])
std = np.std(df[column_name])
print('mean of the dataset is', mean)
print('std. deviation is', std)

threshold = 3
outlier = []
for i in df[column_name]:
    z = (i-mean)/std
    if z > threshold:
        outlier.append(i)
print('outlier in dataset is', outlier)

#how remove outliers??