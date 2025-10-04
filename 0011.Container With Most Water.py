from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """Optimized two-pointer with aggressive skip strategy

        Intuition:
        The amount of water contained depends on the shorter height and the distance between lines.
        When moving inward doesn't improve the area, we can skip positions until we find a taller line.

        Approach:
        1. Use two pointers starting from both ends of the array
        2. Calculate area and update maximum if it improves
        3. If area doesn't improve, skip positions on the shorter side until finding a taller line
        4. This avoids checking positions that won't yield better results

        Complexity:
        Time: O(n) where n is the length of the height array (amortized single pass)
        Space: O(1) as we only use constant extra space
        """
        ans = i = 0
        j = len(height) - 1

        while j > i:
            temp = (j - i) * min(height[i], height[j])

            if temp > ans:
                ans = temp
            else:
                if height[i] > height[j]:
                    temp = j
                    while j != i:
                        j -= 1
                        if height[j] > height[temp]:
                            break
                else:
                    temp = i
                    while j != i:
                        i += 1
                        if height[i] > height[temp]:
                            break

        return ans
