import numpy as np
import pandas as pd
import scipy
from scipy.stats import zscore
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics
import seaborn as sns


def open_file():
    print("This program will remove outliers and perform calculations.")
    print("Enter the filename to be read: ")
    print("(if name is femur_gt.xlsx, enter femur_gt)")
    filename = input()+".xlsx"
    # bone_number = input("Enter the name of the bone (e.g. fe1): ")
    excel_sheet = int(input("Enter the sheet number: "))
    sheet_num = excel_sheet-1
    df_select = pd.read_excel(filename, sheet_name=sheet_num, header=0)
    df_select.dropna(inplace=True)
    return df_select


def print_orig():
    print("ORIGINAL VALUES:\n")
    print(df.describe())


def calculate_z_scores():
    z_score = scipy.stats.zscore(df)
    abs_z_score = np.abs(z_score)
    filtered_entries = (abs_z_score < 3).all(axis=1)
    no_outliers = df[filtered_entries]
    return no_outliers


def print_new():

    print("VALUES WITH NO OUTLIERS:\n")
    print(new_df.describe())


def print_menu():
    print("1: null")
    print("2: null")
    print("3: Value Count")
    print("4: Select another bone")
    print("5: Exit")


def norm_distribution():
    column_choice = input("Enter: original, smooth20, smooth200 or smooth500: ")
    norm_df = new_df[column_choice]
    plt.hist(norm_df)
    plt.show()
    std = np.std(norm_df, ddof=1)
    mean = np.mean(norm_df)
    domain = np.linspace(np.min(norm_df), np.max(norm_df))
    plt.plot(domain, norm.pdf(domain,mean,std))
    plt.hist(norm_df, edgecolor='black', alpha=.5, density=True)
    plt.title("Normal Fit")
    plt.show()


df = open_file()
#femur_gtprint_orig()
new_df = calculate_z_scores()
print_new()
print("NUMBER OF OUTLIERS REMOVED: ")
print(len(df)-len(new_df))
print("Normal distribution:")
norm_distribution()
