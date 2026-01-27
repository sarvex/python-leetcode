class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        """Build target array by inserting elements at specified indices.

        Intuition:
            Simulate the process by inserting each element at the given index
            position in the target array.

        Approach:
            Iterate through nums and index simultaneously, using list insert
            to place each value at the corresponding position.

        Complexity:
            Time: O(n^2) due to list insert shifting elements
            Space: O(n) for the target array
        """
        target: list[int] = []
        for value, position in zip(nums, index):
            target.insert(position, value)
        return target
