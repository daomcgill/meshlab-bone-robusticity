import numpy as np
import pandas as pd
import scipy
from scipy.stats import zscore
import matplotlib.pyplot as plt
from scipy.stats import norm
from numpy import exp
from scipy.stats import boxcox
from numpy import append
import seaborn as sns


def open_file():
    filename = input()+".xlsx"
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


def z_scores_no_abs():
    z_score2 = scipy.stats.zscore(df)
    filtered_entries2 = (z_score2 < 3).all(axis=1)
    no_outliers2 = df[filtered_entries2]
    return no_outliers2


def print_new():
    print("VALUES WITH NO OUTLIERS:\n")
    print(new_df.describe())


def print_menu():
    print("1: null")
    print("2: Normal Distribution")
    print("3: Value Count")
    print("4: Select another bone")
    print("5: Exit")


def norm_distribution():
    column_choice2 = input("Enter: original, smooth20, smooth200 or smooth500: ")
    norm_df = new_df[column_choice2]
    print(norm_df.agg(['skew', 'kurtosis']))
    plt.hist(norm_df)
    plt.show()
    std = np.std(norm_df, ddof=1)
    mean = np.mean(norm_df)
    x_data = np.linspace(np.min(norm_df), np.max(norm_df))
    y_data = norm.pdf(x_data, mean, std)
    plt.plot(x_data, y_data)
    plt.hist(norm_df, edgecolor='black', alpha=.5, density=True)
    plt.title("Normal Fit")
    plt.xlabel("Value")
    plt.ylabel("Density")
    plt.legend
    plt.savefig(bone_number+"_"+column_choice2+"_norm.png")
    plt.show()
    # sqrt
    plt.title("Sqrt Transform")
    sqrt_df = np.sqrt(norm_df)
    std = np.std(sqrt_df, ddof=1)
    mean = np.mean(sqrt_df)
    x_data = np.linspace(np.min(sqrt_df), np.max(sqrt_df))
    y_data = norm.pdf(x_data, mean, std)
    plt.plot(x_data, y_data)
    plt.hist(sqrt_df, edgecolor='black', alpha=.5, density=True)
    plt.savefig(bone_number+"_"+column_choice2+"_sqrt.png")
    plt.show()
    # log
    plt.title("Logarithmic Transform")
    log_transform_df = np.log(norm_df+0.000000001)
    log_transform_df.replace([np.inf, -np.inf], np.nan, inplace=True)
    log_transform_df.dropna(inplace=True)
    std = np.std(log_transform_df, ddof=1)
    mean = np.mean(log_transform_df)
    x_data = np.linspace(np.min(log_transform_df), np.max(log_transform_df))
    y_data = norm.pdf(x_data, mean, std)
    plt.plot(x_data, y_data)
    plt.hist(log_transform_df, edgecolor='black', alpha=.5, density=True)
    plt.savefig(bone_number+"_"+column_choice2+"_log.png")
    plt.show()
    # Cube Root
    plt.title("Cube Root Transform")
    cube_df = np.cbrt(norm_df)
    cube_df.replace([np.inf, -np.inf], np.nan, inplace=True)
    cube_df.dropna(inplace=True)
    std = np.std(cube_df, ddof=1)
    mean = np.mean(cube_df)
    x_data = np.linspace(np.min(cube_df), np.max(cube_df))
    y_data = norm.pdf(x_data, mean, std)
    plt.plot(x_data, y_data)
    plt.hist(cube_df, edgecolor='black', alpha=.5, density=True)
    plt.savefig(bone_number+"_"+column_choice2+"_cubert.png")
    plt.show()



def norm_distribution_no_abs():
    column_choice3 = input("Enter: original, smooth20, smooth200 or smooth500: ")
    norm_df2 = no_abs_df[column_choice3]
    plt.hist(norm_df2)
    plt.show()
    std = np.std(norm_df2, ddof=1)
    mean = np.mean(norm_df2)
    domain = np.linspace(np.min(norm_df2), np.max(norm_df2))
    plt.plot(domain, norm.pdf(domain, mean, std))
    plt.hist(norm_df2, edgecolor='black', alpha=.5, density=True)
    plt.title("Normal Fit")
    plt.show()


print("This program will remove outliers and perform calculations.")
print("Enter the filename to be read: ")
print("(if name is femur_gt.xlsx, enter femur_gt)")
# open xlsx file for data
df = open_file()
bone_number = input("Enter the name of the bone (e.g. fe1): ")
# print original data
print_orig()
# calculate z scores and remove outliers
new_df = calculate_z_scores()
# no_abs_df = z_scores_no_abs()
# print new values with no outliers
print_new()
print("NUMBER OF OUTLIERS REMOVED: ")
print(len(df)-len(new_df))
# norm_distribution_no_abs()
# menu options
loop = True
while loop:
    print_menu()
    try:
        choice = int(input("Choose a menu option (1-5): "))
    except ValueError:
        print('Enter a valid integer')

    # noinspection PyUnboundLocalVariable

    if choice == 2:
        print("Option 2 has been selected.")
        print("Normal distribution:")
        norm_distribution()
    elif choice == 3:
        print("Option 3 has been selected.")
        print("Count of unique values. Values have been rounded to 1 decimal point.\n")
        round_df = new_df.round(1)
        print("Which column would you like to see?")
        column_choice = input("Enter: original, smooth20, smooth200 or smooth500: ")
        bins_choice = input("Use bins? Enter y or n:")
        if bins_choice == "n":
            print(round_df[column_choice].value_counts())
        elif bins_choice == "y":
            bin_count = input("Enter number of bins to use: ")
            bin_count = int(bin_count)
            print(round_df[column_choice].value_counts(bins=bin_count))
    elif choice == 4:
        print("Option 4 has been selected.")
        print("Selecting a new bone: \n")
        print("Enter the filename to be read: ")
        print("(if name is femur_gt.xlsx, enter femur_gt)")
        df = open_file()
        bone_number = input("Enter the name of the bone (e.g. fe1): ")
        print_orig()
        new_df = calculate_z_scores()
        print_new()
        print("NUMBER OF OUTLIERS REMOVED: ")
        print(len(df)-len(new_df))
    elif choice == 5:
        print("Option 5 has been selected.")
        print("Program exit.")
        loop = False
    else:
        print("Wrong option selection. Try again.")
