class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """Count stones that are jewels using a set for O(1) lookup.

        Intuition:
            Convert jewels to a set for fast membership testing, then count
            how many stones appear in that set.

        Approach:
            1. Create a set from the jewels string
            2. Iterate through stones, counting matches

        Complexity:
            Time: O(j + s) where j is jewels length and s is stones length
            Space: O(j) for the jewel set
        """
        jewel_set = set(jewels)
        return sum(stone in jewel_set for stone in stones)
