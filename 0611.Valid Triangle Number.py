from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """Sorted two-pointer with early pruning

        Intuition:
        - After sorting, for each potential largest side c, we need pairs (a, b) with a + b > c.
        - Using two pointers on the prefix [0..i-1] efficiently counts valid pairs.

        Approach:
        - Sort nums. Iterate i from n-1 downto 2 treating nums[i] as the largest side c.
        - Early all-valid pruning: if the two smallest sum > c, then any 3 picked from 0..i form a triangle; add C(i+1, 3) and break.
        - Early skip: if the two largest before i sum < c, no pair can work; continue.
        - Otherwise, two-pointer over [0, i-1]: if nums[l] + nums[r] > c, then all indices in [l..r-1] with r form valid triangles; count r-l and move r--. Else move l++.

        Complexity:
        - Time: O(n^2) in worst case; best-case early break improves constants.
        - Space: O(1) extra beyond sorting in-place.
        """
        nums.sort()
        n: int = len(nums)
        ans: int = 0

        for i in range(n - 1, 1, -1):
            c = nums[i]

            # If the two smallest already exceed c, all triplets among 0..i are valid
            if n >= 3 and nums[0] + nums[1] > c:
                ans += (i + 1) * i * (i - 1) // 6  # C(i+1, 3)
                break

            # If even the two largest before i can't exceed c, skip this c
            if i >= 2 and nums[i - 2] + nums[i - 1] < c:
                continue

            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] > c:
                    ans += right - left
                    right -= 1
                else:
                    left += 1

        return ans
