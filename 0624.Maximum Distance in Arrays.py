class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        """Find maximum distance between elements from different sorted arrays.

        Intuition:
            Since each array is sorted, the min is the first element and max
            is the last. Track running global min and max, computing the distance
            against each new array to ensure elements come from different arrays.

        Approach:
            1. Initialize global min and max from the first array.
            2. For each subsequent array, compute distance using current array's
               endpoints against the running global min/max.
            3. Update the global min and max after computing distances.

        Complexity:
            Time: O(n) where n is the number of arrays
            Space: O(1)
        """
        result = 0
        current_min, current_max = arrays[0][0], arrays[0][-1]
        for arr in arrays[1:]:
            dist_from_max = abs(arr[0] - current_max)
            dist_from_min = abs(arr[-1] - current_min)
            result = max(result, dist_from_max, dist_from_min)
            current_min = min(current_min, arr[0])
            current_max = max(current_max, arr[-1])
        return result
