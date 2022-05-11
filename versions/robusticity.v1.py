import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

#filename to be read
filename = "femur_gt.xlsx"
#bone number
bone_number = "fe1"
#filename, sheet#
df = pd.read_excel(filename, sheet_name = 0, header = 0)
#column name
column_name = 'original'

df[column_name+"_stats"] = stats.zscore(df[column_name])
df[[column_name, column_name+"_stats"]].describe().round(3)

def find_outliers(col):
    from scipy import stats
    z = np.abs(stats.zscore(col))
    idx_outliers = np.where(z>3, True, False)
    return pd.Series(idx_outliers, index=col.index)

#loops through all colums and defines any outliers as 'True'
df_outliers = pd.DataFrame()
for col in df.describe().columns:
    df_outliers[col] = find_outliers(df[col])
df_outliers.head()

#indicates rows (across all columns) that have at least one outlier
test_outs = df_outliers.apply(lambda x: np.any(x), axis=1)
print(len(test_outs), df_outliers.shape)
test_out
np.sum(test_outs)

#filter out all outliers
df_clean = df.loc[test_outs==False]
df_clean.describe()
