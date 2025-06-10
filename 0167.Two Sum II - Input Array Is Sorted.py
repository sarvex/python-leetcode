from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """Two-pointer approach for finding two numbers that add up to target.

        Intuition: Since the array is sorted, we can use two pointers from both ends
        and move them based on comparison with the target.

        Approach: Use left pointer at start and right pointer at end. Adjust pointers
        based on sum comparison with target until finding the exact match.

        Complexity:
        Time: O(n) where n is the length of the array
        Space: O(1) as we only use two pointers
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left + 1, right + 1]  # 1-indexed array in problem
            if curr_sum < target:
                left += 1
            else:
                right -= 1
        return []  # Problem guarantees a solution
