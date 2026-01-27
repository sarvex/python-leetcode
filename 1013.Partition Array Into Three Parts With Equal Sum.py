class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        """Determine if array can be partitioned into three parts with equal sum.

        Intuition:
            Each part must sum to total/3. Find the first prefix reaching that
            target and the last suffix reaching it; they must not overlap.

        Approach:
            Compute total sum. If not divisible by 3, return False. Scan from
            the left to find the first partition and from the right for the
            third. The partitions are valid if the left index is strictly less
            than right index minus one.

        Complexity:
            Time: O(n) with two linear scans
            Space: O(1)
        """
        total = sum(arr)
        if total % 3 != 0:
            return False
        target = total // 3
        left, right = 0, len(arr) - 1
        left_sum = right_sum = 0
        while left < len(arr):
            left_sum += arr[left]
            if left_sum == target:
                break
            left += 1
        while right >= 0:
            right_sum += arr[right]
            if right_sum == target:
                break
            right -= 1
        return left < right - 1
