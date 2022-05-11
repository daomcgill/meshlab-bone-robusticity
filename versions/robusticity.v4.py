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
df.dropna(inplace = True)


def calculate_z_scores():
    z_score = scipy.stats.zscore(df)
    abs_z_score = np.abs(z_score)
    filtered_entries = (abs_z_score < 3).all(axis=1)
    no_outliers = df[filtered_entries]
    return no_outliers


def print_menu():
    print("1: null")
    print("2: null")
    print("3: null")
    print("4: Value Count")
    print("5: Exit")

print("ORIGINAL VALUES:\n")
print(df.describe())
print(df.info())
new_df = calculate_z_scores()
print("VALUES WITH NO OUTLIERS:\n")
print(new_df.describe())
print(new_df.info())

# menu options
loop = True
while loop:
    print_menu()
    try:
        choice = int(input("Choose a menu option (1-5): "))
    except ValueError:
        print('Enter a valid integer')

    # noinspection PyUnboundLocalVariable

    if choice == 4:
        print("Option 4 has been selected.")
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
    elif choice == 5:
        print("Option 5 has been selected.")
        print("Program exit.")
        loop = False
    else:
        print("Wrong option selection. Try again.")
