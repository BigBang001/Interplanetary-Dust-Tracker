"""
Interplanetary Dust Tracker
Main file to execute the simulation and visualization of interplanetary dust orbits.
"""

from utils.spice_helper import load_spice_kernels, get_planet_positions
from utils.dust_simulation import simulate_dust_orbits
from visuals.orbit_visualizer import visualize_orbits

def main():
    """
    Main function to coordinate data retrieval, processing, and visualization.
    """
    # Load SPICE kernels
    print("Loading SPICE kernels...")
    load_spice_kernels()

    # Define the planets of interest
    planets = ["Earth", "Mars", "Jupiter"]

    # Retrieve planetary positions
    print("Fetching planetary positions...")
    positions = get_planet_positions(planets)

    # Simulate dust particle orbits
    print("Simulating interplanetary dust orbits...")
    dust_orbits = simulate_dust_orbits(positions)

    # Visualize planetary and dust orbits
    print("Visualizing results...")
    visualize_orbits(planets, positions, dust_orbits)

if __name__ == "__main__":
    main()
