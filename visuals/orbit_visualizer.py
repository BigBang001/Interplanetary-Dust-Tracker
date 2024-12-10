"""
Orbit Visualizer
Generates 3D visualizations of planetary and dust orbits.
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualize_orbits(planets, positions, dust_orbits):
    """
    Generate a 3D plot of planetary orbits and interplanetary dust trajectories.

    Args:
        planets (list): List of planet names.
        positions (dict): Dictionary of planetary positions.
        dust_orbits (list): Dust particle trajectories.
    """
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection="3d")

    # Plot planetary positions
    for planet, pos in positions.items():
        ax.scatter(*pos, label=f"{planet} Position", s=100, edgecolors='k')

    # Plot dust orbits
    for dust_trajectory in dust_orbits:
        x, y, z = dust_trajectory
        ax.plot(x, y, z, alpha=0.5, linestyle='--', color='gray')

    # Set plot properties
    ax.set_title("Interplanetary Dust Tracker", fontsize=14)
    ax.set_xlabel("X (km)", fontsize=12)
    ax.set_ylabel("Y (km)", fontsize=12)
    ax.set_zlabel("Z (km)", fontsize=12)
    ax.legend(loc="upper right", fontsize=10)
    plt.show()
