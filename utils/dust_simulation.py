"""
Dust Simulation Functions
Simulate the orbits of interplanetary dust particles.
"""

import numpy as np

def simulate_dust_orbits(positions, num_particles=500):
    """
    Simulate the orbits of interplanetary dust particles.

    Args:
        positions (dict): Dictionary of planetary positions.
        num_particles (int): Number of dust particles to simulate.

    Returns:
        list: List of dust particle trajectories (x, y, z coordinates).
    """
    dust_orbits = []

    for planet, planet_pos in positions.items():
        # Assume dust originates near the planet's orbit
        radius = np.linalg.norm(planet_pos)
        theta = np.linspace(0, 2 * np.pi, num_particles)

        # Simulate circular orbits (can be extended to elliptical orbits)
        x = radius * np.cos(theta) + np.random.normal(scale=1e4, size=num_particles)
        y = radius * np.sin(theta) + np.random.normal(scale=1e4, size=num_particles)
        z = np.random.normal(scale=1e3, size=num_particles)  # Small perturbations in the z-plane

        dust_orbits.append((x, y, z))

    return dust_orbits
