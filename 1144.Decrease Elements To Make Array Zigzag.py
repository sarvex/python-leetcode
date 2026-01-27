class Solution:
    def movesToMakeZigzag(self, nums: list[int]) -> int:
        """Find the minimum moves to make the array zigzag.

        Intuition:
            There are two zigzag patterns: even-indexed elements are valleys
            or odd-indexed elements are valleys. Try both and pick the minimum.

        Approach:
            For each pattern, compute the total decreases needed at valley
            positions so that each valley element is strictly less than its
            neighbors. Only decreases are allowed.

        Complexity:
            Time: O(n) where n is the length of nums
            Space: O(1) extra space
        """
        total_moves = [0, 0]
        length = len(nums)
        for parity in range(2):
            for j in range(parity, length, 2):
                decrease = 0
                if j > 0:
                    decrease = max(decrease, nums[j] - nums[j - 1] + 1)
                if j < length - 1:
                    decrease = max(decrease, nums[j] - nums[j + 1] + 1)
                total_moves[parity] += decrease
        return min(total_moves)
