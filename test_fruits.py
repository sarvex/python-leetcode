from typing import List

# Test the solution
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        """Sliding window approach to find maximum fruits that can be harvested within k steps

        Intuition:
        We can only move in a limited range from startPos within k steps. The key insight is that
        we should consider all possible paths: going left then right, or going right then left.
        We use a sliding window to efficiently calculate the maximum fruits we can collect.

        Approach:
        1. Use a sliding window technique with two pointers
        2. For each window, calculate the minimum steps needed to collect all fruits in it
        3. If steps exceed k, shrink the window from the left
        4. Track the maximum fruits collected in any valid window

        Complexity:
        Time: O(n) where n is the number of fruit positions
        Space: O(1) only using constant extra space
        """
        # Initialize variables for sliding window
        left = 0
        max_fruits = 0
        current_sum = 0

        # Sliding window approach
        for right in range(len(fruits)):
            # Add current fruit to our collection
            current_sum += fruits[right][1]

            # Calculate minimum steps needed for current window
            # Get positions of leftmost and rightmost fruits in window
            left_pos = fruits[left][0]
            right_pos = fruits[right][0]

            # Calculate steps needed: we can go left then right or right then left
            # Steps = distance to farthest point + distance between endpoints
            while left <= right:
                # Minimum steps to collect all fruits in current window
                steps = min(
                    abs(startPos - left_pos) + (right_pos - left_pos),  # go left then right
                    abs(startPos - right_pos) + (right_pos - left_pos)   # go right then left
                )

                # If within budget, update max and break
                if steps <= k:
                    max_fruits = max(max_fruits, current_sum)
                    break

                # Otherwise, shrink window from left
                current_sum -= fruits[left][1]
                left += 1

                # Update left_pos if window is still valid
                if left <= right:
                    left_pos = fruits[left][0]

        return max_fruits

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    fruits1 = [[2,8],[6,3],[8,6]]
    startPos1 = 5
    k1 = 4
    result1 = solution.maxTotalFruits(fruits1, startPos1, k1)
    print(f"Test 1: {result1}")  # Expected: 9
    
    # Test case 2
    fruits2 = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]]
    startPos2 = 5
    k2 = 4
    result2 = solution.maxTotalFruits(fruits2, startPos2, k2)
    print(f"Test 2: {result2}")  # Expected: 14
    
    # Test case 3
    fruits3 = [[0,3],[6,4],[8,5]]
    startPos3 = 3
    k3 = 2
    result3 = solution.maxTotalFruits(fruits3, startPos3, k3)
    print(f"Test 3: {result3}")  # Expected: 0
