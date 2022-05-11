import numpy as np
import pandas as pd
import scipy
from scipy.stats import zscore
import seaborn as sns
import matplotlib.pyplot as plt

print("This program will remove outliers and perform calculations.")
print("Enter the filename to be read: ")
print("(if name is femur_gt.xlsx, enter femur_gt)")
filename = input()+".xlsx"
bone_number = input("Enter the name of the bone (e.g. fe1): ")
excel_sheet = int(input("Enter the sheet number: "))
sheet_num = excel_sheet-1
df = pd.read_excel(filename, sheet_name=sheet_num, header=0)


def calculate_z_scores():
    z_score = scipy.stats.zscore(df)
    abs_z_score = np.abs(z_score)
    filtered_entries = (abs_z_score < 3).all(axis=1)
    no_outliers = df[filtered_entries]
    return no_outliers


def box_plot():
    # plot original
    column_name = 'original'
    sns.boxplot(x=new_df[column_name])
    plt.savefig("boxplot_"+bone_number+"_"+column_name+".jpg")
    # plot smooth20
    column_name = 'smooth20'
    sns.boxplot(x=new_df[column_name])
    plt.savefig("boxplot_"+bone_number+"_"+column_name+".jpg")
    # plot smooth200
    column_name = 'smooth200'
    sns.boxplot(x=new_df[column_name])
    plt.savefig("boxplot_"+bone_number+"_"+column_name+".jpg")
    # plot smooth500
    column_name = 'smooth500'
    sns.boxplot(x=new_df[column_name])
    plt.savefig("boxplot_"+bone_number+"_"+column_name+".jpg")


new_df = calculate_z_scores()

# box plot
box_plot()
# mean
mean = new_df.mean(axis=0)
print(mean)
# describe
new_df.describe()






