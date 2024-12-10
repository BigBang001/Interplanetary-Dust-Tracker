"""
SPICE Helper Functions
Handles loading SPICE kernels and retrieving planetary positions.
"""

import spiceypy as spice

def load_spice_kernels():
    """
    Load necessary SPICE kernels for planetary data.
    """
    spice.furnsh("https://naif.jpl.nasa.gov/pub/naif/generic_kernels/lsk/naif0012.tls")
    spice.furnsh("https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/de430.bsp")
    print("SPICE kernels successfully loaded.")

def get_planet_positions(planets, reference_frame="ECLIPJ2000", observer="SUN", epoch="2024-01-01T00:00:00"):
    """
    Fetch the positions of specified planets relative to the Sun at a given epoch.

    Args:
        planets (list): List of planet names (e.g., "Earth", "Mars").
        reference_frame (str): The reference frame for coordinates.
        observer (str): The observing body (e.g., "SUN").
        epoch (str): Time in ISO 8601 format.

    Returns:
        dict: Planetary positions in Cartesian coordinates.
    """
    et = spice.str2et(epoch)  # Convert epoch to ephemeris time
    positions = {}

    for planet in planets:
        state, _ = spice.spkezr(planet, et, reference_frame, "NONE", observer)
        positions[planet] = state[:3]  # Extract x, y, z coordinates

    return positions
