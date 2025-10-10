class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        """
        Calculate the maximum energy that can be obtained by moving through the dungeon.

        Intuition:
        We can optimize by working backwards and reusing previously computed values.

        Approach:
        1. Create a copy of the energy array to store intermediate results
        2. Traverse the array from right to left
        3. For each position, add the energy from k steps ahead if it exists
        4. The maximum value in the resulting array is our answer

        Complexity:
        - Time: O(n) where n is the length of the energy array
        - Space: O(1) as we modify the input array in place
        """
        dp = energy.copy()
        for i in range(len(energy) - k - 1, -1, -1):
            dp[i] += dp[i + k]
        return max(dp)
