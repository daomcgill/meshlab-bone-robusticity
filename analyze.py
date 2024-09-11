import sys
import trimesh
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import scipy

def analyze_curvature():
    try:
        # Load the PLY file using trimesh
        mesh = trimesh.load('femur.ply')

        # Extract vertex data
        vertices = mesh.vertices

        # Access the curvature data from the 'quality' attribute in the raw PLY data
        vertex_data = mesh.metadata['_ply_raw']['vertex']['data']
        curvature = vertex_data['quality'].flatten()  # Flatten the array to 1D

        # Original Curvature Analysis
        mean_curvature = np.mean(curvature)
        max_curvature = np.max(curvature)
        min_curvature = np.min(curvature)
        std_curvature = np.std(curvature)

        print(f"Original Curvature Analysis:")
        print(f"Mean Curvature: {mean_curvature}")
        print(f"Max Curvature: {max_curvature}")
        print(f"Min Curvature: {min_curvature}")
        print(f"Standard Deviation of Curvature: {std_curvature}")

        # Calculate RMS curvature
        rms_curvature = np.sqrt(np.mean(curvature**2))

        # Calculate mean absolute curvature
        mean_absolute_curvature = np.mean(np.abs(curvature))

        print(f"Additional Curvature Analysis:")
        print(f"RMS Curvature: {rms_curvature}")
        print(f"Mean Absolute Curvature: {mean_absolute_curvature}")

        # Surface Roughness Calculation
        roughness_rms = np.sqrt(np.mean((curvature - mean_curvature)**2))

        print(f"Surface Roughness (RMS height): {roughness_rms}")

        # Visualize curvature distribution
        plt.figure()
        plt.hist(curvature, bins=100)
        plt.xlabel('Curvature')
        plt.ylabel('Frequency')
        plt.title('Curvature Distribution')
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")

        sys.exit(1)

if __name__ == "__main__":
    analyze_curvature()
