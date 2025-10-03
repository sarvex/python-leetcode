"""Matrix-based water level simulation using NumPy for efficient computation."""

import numpy as np
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        """Calculate total trapped rainwater on a 2D elevation map.

        Intuition:
        Water flows from higher to lower elevation. Instead of simulating individual
        cell flooding (heap-based approach), we can fill the entire interior with water
        initially and then let it flow out iteratively based on boundary constraints.
        Each iteration, water level at each cell is limited by the minimum water level
        of its four neighbors.

        Approach:
        1. Convert heightMap to NumPy array for vectorized operations
        2. Initialize water level: boundaries keep their height, interior filled to max
        3. Iteratively simulate water flowing out:
           - Pad water level array to handle boundaries
           - Each cell's new water level = max(height, min(all 4 neighbors' water levels))
           - Stop when water level stabilizes (no change between iterations)
        4. Return total water volume = sum(water_level - heightMap)

        Complexity:
        Time: O(m * n * k) where k is iterations until convergence
        Space: O(m * n) for NumPy arrays
        """
        water_level = np.array(heightMap, dtype=int)
        height_map_array = np.array(heightMap, dtype=int)
        water_level[1:-1, 1:-1] = np.max(height_map_array)

        previous_water_volume = 0
        while True:
            padded_water_level = np.pad(water_level, ((1, 1), (1, 1)))
            water_level = np.maximum(
                np.minimum(
                    np.minimum(
                        padded_water_level[0:-2, 1:-1],
                        padded_water_level[2:, 1:-1]
                    ),
                    np.minimum(
                        padded_water_level[1:-1, 0:-2],
                        padded_water_level[1:-1, 2:]
                    ),
                ),
                height_map_array,
            )
            current_water_volume = np.sum(water_level - height_map_array)
            if previous_water_volume == current_water_volume:
                return int(current_water_volume)
            previous_water_volume = current_water_volume
