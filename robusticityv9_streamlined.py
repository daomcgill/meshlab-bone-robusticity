import numpy as np
import pandas as pd
from scipy import stats
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from plyfile import PlyData, PlyElement
import os
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# menu options
loop = True
while loop:
    print("1: Load a new bone ROI from .ply files ")
    print("2: Exit")
    try:
        choice = int(input("Choose a menu option (1-5): "))
    except ValueError:
        print('Enter a valid integer')

    # LOAD .PLY FILE
    if choice == 1:
        print("Option 1 has been selected.")
        print("Load a new bone as a .ply file format (x, y, z, quality/ curvature value): ")
        print("Enter the name of the .ply file to be loaded (e.g. fe1_gt.ply) ")
        input_file = input("Format of the .ply file must be x, y, z, float quality (curvature): ")
        assert(os.path.isfile(input_file))
        with open(input_file, 'rb') as f:
            plydata = PlyData.read(f)
            num_verts = plydata['vertex'].count
            print("Number of vertices: ")
            print(num_verts)
            print("Preview of ply file: ")
            # create numpy array for .ply data
            elems = np.zeros(shape=[num_verts, 4], dtype=np.float32)
            elems[:, 0] = plydata['vertex'].data['x']
            elems[:, 1] = plydata['vertex'].data['y']
            elems[:, 2] = plydata['vertex'].data['z']
            elems[:, 3] = plydata['vertex'].data['quality']
        # convert to pandas DataFrame
        df = pd.DataFrame(elems)
        # rename columns
        df.columns = ['x', 'y', 'z', 'quality']
        # print DataFrame
        print(df.head())
        print("DataFrame loaded as df.")
        # abs val
        df = df.abs()
        # print(df.describe())
        # stats
        print("Basic statistics for loaded .ply file: ")
        df = df.dropna()
        out_df = pd.DataFrame(df['quality'])
        out_df = out_df.dropna()
        z_scores = stats.zscore(out_df)
        abs_z_scores = np.abs(z_scores)
        filtered_entries = (abs_z_scores < 3).all(axis=1)
        out_df = out_df[filtered_entries]
        print("(Absolute values taken. Outliers removed.)")
        print(out_df.describe())
        stats_no_outliers = out_df.describe()
        df = out_df

    elif choice == 2:
        print("Program exit.")
        loop = False
#%%
