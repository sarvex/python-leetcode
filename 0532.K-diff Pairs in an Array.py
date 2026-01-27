class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        """Single pass with two sets to find unique k-diff pairs.

        Intuition:
            For each number, check if its complement (num - k or num + k)
            has been seen. Use a set to track unique pairs.

        Approach:
            Maintain a visited set and an answer set. For each number, check
            if num - k or num + k exists in visited, adding the smaller
            element to the answer set for uniqueness.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        visited, unique_pairs = set(), set()
        for value in nums:
            if value - k in visited:
                unique_pairs.add(value - k)
            if value + k in visited:
                unique_pairs.add(value)
            visited.add(value)
        return len(unique_pairs)
